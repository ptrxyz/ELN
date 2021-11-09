#!/bin/bash

logfile=$1

echo "---- Preparation script ----"
# TODO some kind of version file output, e.g. in .version -> needs to be parsed with the CLI "info" option
# TODO tar ball the src folder as chemotion/app and move it to the container via ADD
# TODO Do we need to move the template folder as well or can it stay outside of the container?

rm -rf src/
rm -rf shared/
for foldername in $(python3 scripts/parseYML.py read --collect configFileStructure.yml folders.item); do
    echo "creating [shared/eln/${foldername}] ..."; \
    mkdir -p shared/eln/${foldername}; \
done
mkdir -p shared/eln/config
 
git clone https://github.com/ComPlat/chemotion_ELN src
cd src
if [ -n "$2" ]; then
    git checkout "$2"
    if [ $? -eq 0 ]; then
        echo "checked out tag: $2" >> ../$logfile
    else
        echo "failed to checkout $2 ... falling back to latest commit." >> ../$logfile
    fi
fi
echo "based on Chemotion ELN revision: $(git rev-parse HEAD)" >> ../$logfile
echo "Chemotion ELN version: $(git describe --abbrev=0 --tags)" >> ../$logfile

ref=$(git rev-parse --short HEAD) && \
tag=$(git describe --abbrev=0 --tags) && \
echo -e "CHEMOTION_REF=$ref\nCHEMOTION_TAG=$tag" > .version

cd ..
ref=$(git rev-parse --short HEAD)
tag=$(git describe --abbrev=0 --tags)
echo -e "BUILDSYSTEM_REF=$ref\nBUILDSYSTEM_TAG=$tag" >> src/.version

for foldername in $(python3 scripts/parseYML.py read --collect configFileStructure.yml folders.item); do
    echo "Exposing [${foldername}] ..."; \
    rm -r src/${foldername}; \
    ln -s /shared/eln/${foldername} src/${foldername}; \
done

for filename in $(python3 scripts/parseYML.py read --collect configFileStructure.yml files.item); do
    echo "Exposing [${filename}] ..."; \
    rm src/${filename}; \
    ln -s /shared/eln/${filename} src/${filename}; \
done