#!/bin/bash
logfile=$(date +"%FT%H%M")_log.txt

echo "Started at:" > $logfile
date >> $logfile

rm -rf src/
rm -rf shared/
for foldername in $(python3 scripts/parseYML.py read --collect configFileStructure.yml folders.item); do
 echo "creating [shared/eln/${foldername}] ..."; \
 mkdir -p shared/eln/${foldername}; \
done
touch shared/eln/config/secrets.yml
 
git clone https://github.com/ComPlat/chemotion_ELN src
cd src
echo "based on revision:" >> ../$logfile
git log | head -1 >> ../$logfile
cd ..

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
 
./build.sh all

docker-compose run --service-ports eln landscape deploy

docker-compose run --service-ports eln init

startELN="docker-compose run --service-ports eln starteln"
$startELN &>/dev/null &

sleep 30

echo -e "\ncurl -L localhost:3000:\n" >> $logfile
curl -L localhost:3000 >> $logfile

echo "Finished at:" >> $logfile
date >> $logfile

docker-compose down