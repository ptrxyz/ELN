#!/bin/bash
logfile=$(date +"%FT%H%M")_log.txt

echo "Started at:" > $logfile
date >> $logfile

./prepareBuild.sh $logfile
 
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