#!/bin/bash

checkFolderExists(){
    if [[ ! -d $1 ]]; then
        echo "    Folder $1 does not exist. Please create it."
        return 1
    else
        echo "    Found folder $1."
        return 0
    fi
}

checkFolderIsWritable(){
    if [[ ! -w $1 ]]; then
        echo "    Folder $1 has no write permission. Please grant it."
        return 1
    else
        echo "    Folder $1 has write permission."
        return 0
    fi
}

echo "---- Init script ----"

echo "Checks for the file system:"
# check accessibility of shared folders
if ! mount | grep 'on /shared' 2>&1 1>/dev/null; then
    echo "    The shared folder is not correctly connected as volume. Please make sure that a folder /shared is available next to the docker-compose.yml file."
    exit 1
else
    echo "    Found folder /shared."
fi

if ! checkFolderExists "/shared/eln"        ; then exit 1; fi
if ! checkFolderExists "/shared/eln/config" ; then exit 1; fi
if ! checkFolderExists "/shared/eln/log"    ; then exit 1; fi
if ! checkFolderExists "/shared/eln/public" ; then exit 1; fi
if ! checkFolderExists "/shared/eln/tmp"    ; then exit 1; fi
if ! checkFolderExists "/shared/eln/uploads"; then exit 1; fi

# check write permissions in folder
if ! checkFolderIsWritable "/shared/eln"        ; then exit 1; fi
if ! checkFolderIsWritable "/shared/eln/config" ; then exit 1; fi
if ! checkFolderIsWritable "/shared/eln/log"    ; then exit 1; fi
if ! checkFolderIsWritable "/shared/eln/public" ; then exit 1; fi
if ! checkFolderIsWritable "/shared/eln/tmp"    ; then exit 1; fi
if ! checkFolderIsWritable "/shared/eln/uploads"; then exit 1; fi

# check existance of certain files?
# copy files - still needed with new Dockerfile?

echo "Checks for the database:"
# check accessibility of DB:
source <( python3 /shared/parseYML.py read --upper --prefix=DB_ /shared/eln/config/database.yml production )
# db_name="chemotion"
# db_role="chemotion"
# db_password="PleaseChangeThePassword"
# db_host="db"
# db_port="5432"
# simply waits for the DB to be up and done booting
while ! pg_isready -h $DB_HOST 1>/dev/null 2>&1; do
    echo "    Database instance not ready. Waiting ..."
    sleep 10
done
echo "    Database instance ready."

# check correct setup of the DB and initialize DB
echo "    Creating database ..."
if ! (echo "\q" | psql -d $DB_DATABASE -h $DB_HOST -U $DB_USERNAME 2>/dev/null); then
    echo "    Can not connect to database or database needs to be initialized."
    # if [[ "x${CREATE_USER}" == x"yes" || x"${INITIALIZE}" == x"yes" ]]; then
    echo "    Dropping database $DB_DATABASE it it exists ..."
    psql --host="$DB_HOST" --username 'postgres' -c "
        DROP DATABASE IF EXISTS $DB_DATABASE;"
    echo "    Dropping role $DB_USERNAME if it exists ..."
    echo "    Creating role $DB_USERNAME with password $DB_PASSWORD ..."
    psql --host="$DB_HOST" --username 'postgres' -c "
        DROP ROLE IF EXISTS $DB_USERNAME;
        CREATE ROLE $DB_USERNAME LOGIN CREATEDB NOSUPERUSER PASSWORD '$DB_PASSWORD';"
    echo "    Creating database $DB_DATABASE for owner $DB_USERNAME ..."
    psql --host="$DB_HOST" --username 'postgres' -c "            
        CREATE DATABASE $DB_DATABASE OWNER $DB_USERNAME;
    " || {
        echo "    Could not create database. PSQL returned [$?]."
        exit 1
    }
    psql --host="$DB_HOST" --username="$DB_USERNAME" -c "
        CREATE EXTENSION IF NOT EXISTS \"pg_trgm\";
        CREATE EXTENSION IF NOT EXISTS \"hstore\";
        CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";
        ALTER USER $DB_USERNAME PASSWORD '$DB_PASSWORD';
    " || {
        echo "    Failed to set password for database user. PSQL returned [$?]."
        exit 1
    }
    # else
    #     echo "Could not connect to database. Make sure to specify connection parameters using DB_HOST, DB_ROLE, DB_NAME, DB_PW."
    #     exit 1
    # fi
fi

echo "    Database up and running."

# block PubChem
echo "Database setup:"
echo "    Blocking access to PubChem server..."
echo "127.0.0.1    pubchem.ncbi.nlm.nih.gov" >> /etc/hosts

# initialialize ELN
# execute "${INIT_BASE}/init-scripts/library/eln-init.sh"
cd /chemotion/app/

SECRET_KEY="$(bundle exec rake secret)"
cat <<EOF > config/secrets.yml
production:
  secret_key_base: $SECRET_KEY
EOF

echo "    Initializing database schemas..."
bundle exec rake db:create
echo "    Database created."
bundle exec rake db:migrate
echo "    Database migrated."
bundle exec rake db:seed
echo "    Database seeded."

echo "    Creating sprites..."
bundle exec rake ketcherails:import:common_templates
rm -rf /chemotion/app/app/public/images/ketcherails/icons/original/*
bundle exec rails r 'MakeKetcherailsSprites.perform_now'

# unblock PubChem
# do not use -i here. Docker prevents it from working...
echo "    Unblocking access to PubChem server..."
sed '/pubchem.ncbi.nlm.nih.gov/d' /etc/hosts > /etc/hosts