#!/bin/bash
logfile=$(date +"%FT%H%M")_log.txt

echo "Started at:" > $logfile
date >> $logfile

./prepareBuild.sh $logfile $1
 
if [ -n "$2" ]; then
	./build.sh $2
else
	./build.sh all
fi

docker-compose run --service-ports eln landscape deploy

docker-compose run --service-ports eln init

docker-compose run --service-ports eln info >> $logfile

startELN="docker-compose run --service-ports eln starteln"
$startELN &>/dev/null &

sleep 30

#echo -e "\ncurl -L localhost:3000:\n" >> $logfile
#curl -L localhost:3000 >> $logfile

reference="<div id='Home'></div>"
testResult=$(curl -L localhost:3000 | tail -5 | head -1)
echo "Trying to reach localhost:3000 ..."
if [ "$reference" = "$testResult" ]; then echo "SUCCESS!" >> $logfile; else echo "-- FAIL --" >> $logfile; fi

echo "Finished at:" >> $logfile
date >> $logfile

# dockername=$(docker ps -a | grep chemotion | awk NR==1'{print $1}')
# docker exec -it $dockername /init stopeln
docker-compose stop

docker-compose down
