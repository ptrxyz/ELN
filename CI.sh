#!/bin/bash
date > log.txt

rm -rf src/
 
git clone https://github.com/ComPlat/chemotion_ELN src
cd src
echo "based on revision:" >> ../log.txt
git log | head -1 >> ../log.txt
cd ..

 
cp -r src/config/* defaultLandscape/config/
cp -r src/public/* defaultLandscape/public/
 
./build.sh all

docker-compose run --service-ports eln landscape deploy

docker-compose run --service-ports eln init

startELN="docker-compose run --service-ports eln starteln"
$startELN &>/dev/null &

sleep 5

curl -L localhost:3000 >> log.txt
