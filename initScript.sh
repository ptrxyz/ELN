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
db_name="chemotion"
db_role="chemotion"
db_password="PleaseChangeThePassword"
db_host="db"
db_port="5432"
# simply waits for the DB to be up and done booting
while ! pg_isready -h $db_host 1>/dev/null 2>&1; do
    echo "    Database instance not ready. Waiting ..."
    sleep 10
done
echo "    Database instance ready."

# check correct setup of the DB and initialize DB
echo "    Creating database ..."
if ! (echo "\q" | psql -d $db_name -h $db_host -U $db_role 2>/dev/null); then
    echo "    Can not connect to database or database needs to be initialized."
    # if [[ "x${CREATE_USER}" == x"yes" || x"${INITIALIZE}" == x"yes" ]]; then
    echo "    Dropping database $db_name it it exists ..."
    psql --host="$db_host" --username 'postgres' -c "
        DROP DATABASE IF EXISTS $db_name;"
    echo "    Dropping role $db_role if it exists ..."
    echo "    Creating role $db_role with password $db_password ..."
    psql --host="$db_host" --username 'postgres' -c "
        DROP ROLE IF EXISTS $db_role;
        CREATE ROLE $db_role LOGIN CREATEDB NOSUPERUSER PASSWORD '$db_password';"
    echo "    Creating database $db_name for owner $db_owner ..."
    psql --host="$db_host" --username 'postgres' -c "            
        CREATE DATABASE $db_name OWNER $db_role;
    " || {
        echo "    Could not create database. PSQL returned [$?]."
        exit 1
    }
    psql --host="$db_host" --username="$db_role" -c "
        CREATE EXTENSION IF NOT EXISTS \"pg_trgm\";
        CREATE EXTENSION IF NOT EXISTS \"hstore\";
        CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";
        ALTER USER $db_role PASSWORD '$db_password';
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

# unblock PubChem
# do not use -i here. Docker prevents it from working...
echo "    Unblocking access to PubChem server..."
sed '/pubchem.ncbi.nlm.nih.gov/d' /etc/hosts > /etc/hosts