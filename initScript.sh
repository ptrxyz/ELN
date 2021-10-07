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
# simply waits for the DB to be up and done booting
while ! pg_isready -h db 1>/dev/null 2>&1; do
    echo "Database not ready. Waiting ..."
    sleep 10
done

echo "Database up and ready."

# check correct setup of the DB
# initialize DB

# block PubChem
# initialialize ELN
# unblock PubChem


# export INITIALIZE=yes
# waitForDB
# execute "${INIT_BASE}/init-scripts/library/shared-storage-init.sh"
# execute "${INIT_BASE}/init-scripts/library/db-init.sh"
# [[ "$1" == "dev" ]] && execute "${INIT_BASE}/init-scripts/library/patch4dev.sh"
# execute "${INIT_BASE}/init-scripts/library/block-pubchem.sh"
# execute "${INIT_BASE}/init-scripts/library/eln-init.sh"
# execute "${INIT_BASE}/init-scripts/library/unblock-pubchem.sh"
