#!/bin/bash
echo Running the database script

case "$1" in
	dump)
		pg_dumpall -h db -U postgres > /shared/eln/public/zip/dump.sql
		;;
	load)
        while ! pg_isready -h db -U 'postgres' 1>/dev/null 2>&1; do
            ((iterator++))
            echo "    Database instance not ready. Waiting ..."
            sleep 10
            if [ $iterator -eq 5 ]; then
                echo "    Database cannot be reached on $DB_HOST, please check the connection!"
                exit  1
            fi
        done
		psql -h db -U postgres -d postgres < /shared/eln/public/zip/dump.sql
		;;
	*)
		echo "Ignoring: $1"
esac