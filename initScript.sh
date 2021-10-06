#!/bin/bash
echo Running the init script 

# simply waits for the DB to be up and done booting
while ! pg_isready -h udb 1>/dev/null 2>&1; do
    echo "Database not ready. Waiting ..."
    sleep 10
done


# export INITIALIZE=yes
# waitForDB
# execute "${INIT_BASE}/init-scripts/library/shared-storage-init.sh"
# execute "${INIT_BASE}/init-scripts/library/db-init.sh"
# [[ "$1" == "dev" ]] && execute "${INIT_BASE}/init-scripts/library/patch4dev.sh"
# execute "${INIT_BASE}/init-scripts/library/block-pubchem.sh"
# execute "${INIT_BASE}/init-scripts/library/eln-init.sh"
# execute "${INIT_BASE}/init-scripts/library/unblock-pubchem.sh"
