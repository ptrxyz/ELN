#!/bin/bash

echo "You are about to upgrade your existing Chemotion ELN setup."
echo "Please make sure that you put the new version of docker-compose.yml parallel to this upgrade script."
echo "Be aware that this script might modifiy existing data and make sure that you have created a backup of your existing data."
read -e -p "
Do you wish to proceed ? [yes/N] " YN
[[ $YN != "yes" ]] && exit 1

sharedTmp=$(date +"%FT%H%M")_shared
if [ -d shared ]; then
    mv shared/ $sharedTmp && mkdir shared && mv $sharedTmp shared/eln/
else
   echo "Folder shared/ does not exist. Are you in the right folder of an <1.0.3 Chemotion ELN setup?"
   exit 1
fi

./setup.sh

read -e -p "
Overwrite configurations files with default files ? [yes/N] " YN
[[ $YN == "yes" ]] && docker-compose run eln landscape deploy

read -e -p "
Run init script (migrating database, generating sprites, compiliing assets) ? [yes/N] " YN
[[ $YN == "yes" ]] && docker-compose run eln upgrade
