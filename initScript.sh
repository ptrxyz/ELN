#!/bin/bash
echo Running the init script 

# check accessibility of shared folder
if ! mount | grep 'on /shared' 2>&1 1>/dev/null; then
    echo The shared folder is not correctly connected as volume. Please make sure that a folder _shared_ is available next to the docker-compose.yml file.
fi

# check write permissions in folder
# check existance of certain files?
# copy files - still needed with new Dockerfile?

# check accessibility of DB - OK
# simply waits for the DB to be up and done booting
while ! pg_isready -h db 1>/dev/null 2>&1; do
    echo "Database not ready. Waiting ..."
    sleep 10
done

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
