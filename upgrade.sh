#!/bin/bash

sharedTmp=$(date +"%FT%H%M")_shared
if [ -d shared ]; then
    mv shared/ $sharedTmp && mkdir shared && mv $sharedTmp shared/eln/
else
   echo "Folder shared/ does not exist. Are you in the right folder of an <1.0.3 setup?"
   exit 1
fi

./setup.sh

read -e -p "
Overwrite configurations files with default files ? [yes/N] " YN
[[ $YN == "yes" ]] && docker-compose run eln landscape deploy

read -e -p "
Run init script (migrating database, generating sprites, compiliing assets) ? [yes/N] " YN
[[ $YN == "yes" ]] && docker-compose run eln init
