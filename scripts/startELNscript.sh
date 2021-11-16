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

echo Running the start ELN script

echo "Checks for the file system:"
# check accessibility of shared folders
if ! mount | grep 'on /shared' 2>&1 1>/dev/null; then
    echo "    The shared folder is not correctly connected as volume. Please make sure that a folder shared/ is available next to the docker-compose.yml file."
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

chown -R $USERID:$USERID /shared

echo "Checks for the database:"

db_profile="production"
db_configfile="/shared/eln/config/database.yml"
source <( python3 /etc/scripts/parseYML.py read --upper --prefix=DB_ $db_configfile $db_profile )

echo "    Evaluated configuration file: $db_configfile"
echo "    Imported profile: $db_profile"
echo "    Connecting to host: $DB_HOST ..."
while ! pg_isready -h $DB_HOST 1>/dev/null 2>&1; do
    echo "    Database instance not ready. Waiting ..."
    sleep 10
done
echo "    Database instance ready."

# check correct setup of the DB and initialize DB
echo "    Creating database ..."
if ! (echo "\q" | psql -d $DB_DATABASE -h $DB_HOST -U $DB_USERNAME 2>/dev/null); then
    echo "    Can not connect to database or database needs to be initialized."
    exit 1
fi

echo "    Database up and running."

cd /chemotion/app/

bundle exec rake db:migrate
echo "    Database migrated."

bundle exec rake assets:precompile

cd /chemotion/app
# bundle exec rails s
exec passenger start -e production --engine=builtin --address 0.0.0.0 --port 3000