#!/bin/bash
echo Running the database script

if [ -n "$2" ]; then
    HOST=$2
else
    HOST="db"
fi

while ! pg_isready -h $HOST -U 'postgres' 1>/dev/null 2>&1; do
    ((iterator++))
    echo "    Database instance on host ${HOST} not ready. Waiting ..."
    sleep 10
    if [ $iterator -eq 5 ]; then
        echo "    Database cannot be reached on ${HOST}, please check the connection!"
        exit  1
    fi
done

case "$1" in
	dump)
		if pg_dumpall -h $HOST -U postgres > /shared/eln/public/zip/dump.sql; then
            echo "    Database dumped to /shared/eln/public/zip/dump.sql"
        else
            echo "    Database could not be dumped to /shared/eln/public/zip/dump.sql."
        fi
		;;
	load)
		if psql -h $HOST -U postgres -d postgres < /shared/eln/public/zip/dump.sql; then
            echo "    Database loaded from /shared/eln/public/zip/dump.sql"
        else
            echo "    Databse could not be loaded from /shared/eln/public/zip/dump.sql"
        fi
		;;
	*)
		echo "    Ignoring: $1"
esac