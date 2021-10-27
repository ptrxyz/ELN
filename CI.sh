#!/bin/bash
logfile=$(date +"%FT%H%M")_log.txt

echo "Started at:" > $logfile
date >> $logfile

rm -rf src/
mkdir -p defaultLandscape/log defaultLandscape/tmp defaultLandscape/uploads
mkdir -p shared/eln/config shared/eln/log shared/eln/public shared/eln/tmp shared/eln/uploads
 
git clone https://github.com/ComPlat/chemotion_ELN src
cd src
echo "based on revision:" >> ../$logfile
git log | head -1 >> ../$logfile
cd ..

 
cp -r src/config/* defaultLandscape/config/
cp -r src/public/* defaultLandscape/public/
 
./build.sh all

docker-compose run --service-ports eln landscape deploy

docker-compose run --service-ports eln init

startELN="docker-compose run --service-ports eln starteln"
$startELN &>/dev/null &

sleep 15

echo -e "\ncurl -L localhost:3000:\n" >> $logfile
curl -L localhost:3000 >> $logfile

echo "Finished at:" >> $logfile
date >> $logfile

docker-compose down