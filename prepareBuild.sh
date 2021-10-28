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

echo "---- Preparation script ----"
logfile=$(date +"%FT%H%M")_log.txt

date > $logfile

rm -rf src/
mkdir -p defaultLandscape/log defaultLandscape/tmp defaultLandscape/uploads
mkdir -p shared/eln/config shared/eln/log shared/eln/public shared/eln/tmp shared/eln/uploads

echo "Checking out Chemotionn ELN Repository to src/"
git clone https://github.com/ComPlat/chemotion_ELN src
cd src
echo "based on revision:" >> ../$logfile
git log | head -1 >> ../$logfile
# TODO some kind of version file output, e.g. in .version -> needs to be parsed with the CLI "info" option
cd ..

# TODO prepare contents of the config part in src according to a yaml description (files, folder structure)
# TODO prepare template folder
# TODO add dead links in src/ folder (to /share/eln/...)
# TODO tar ball the src folder as chemotion/app and move it to the container via ADD
# TODO Do we need to move the template folder as well or can it stay outside of the container?

for foldername in $(python3 scripts/parseYML.py read --collect configFileStructure.yml links.item); do
 echo "Exposing [${foldername}] ..."; \
 rm -r src/${foldername}; \
 ln -s /shared/eln/${foldername} src/${foldername}; \
done

cp -r src/config/* defaultLandscape/config/
cp -r src/public/* defaultLandscape/public/
 
./build.sh all

docker-compose run --service-ports eln landscape deploy

docker-compose run --service-ports eln init