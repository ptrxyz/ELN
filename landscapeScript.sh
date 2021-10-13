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

echo "---- Landscape script for $1 ----"

echo "Checks for the file system:"
# check accessibility of shared folders
if ! mount | grep "on /shared" 2>&1 1>/dev/null; then
    echo "    The shared folder is not correctly connected as volume. Please make sure that a folder shared/ is available next to the docker-compose.yml file."
    exit 1
else
    echo "    Found folder /shared."
fi

if ! checkFolderExists "/shared/landscapes/$1"        ; then exit 1; fi
if ! checkFolderExists "/shared/landscapes/$1/config" ; then exit 1; fi
# if ! checkFolderExists "/shared/landscapes/$1/log"    ; then exit 1; fi
# if ! checkFolderExists "/shared/landscapes/$1/public" ; then exit 1; fi
# if ! checkFolderExists "/shared/landscapes/$1/tmp"    ; then exit 1; fi
# if ! checkFolderExists "/shared/landscapes/$1/uploads"; then exit 1; fi

# check write permissions in folder
# if ! checkFolderIsWritable "/shared/landscapes/$1"        ; then exit 1; fi
# if ! checkFolderIsWritable "/shared/landscapes/$1/config" ; then exit 1; fi
# if ! checkFolderIsWritable "/shared/landscapes/$1/log"    ; then exit 1; fi
# if ! checkFolderIsWritable "/shared/landscapes/$1/public" ; then exit 1; fi
# if ! checkFolderIsWritable "/shared/landscapes/$1/tmp"    ; then exit 1; fi
# if ! checkFolderIsWritable "/shared/landscapes/$1/uploads"; then exit 1; fi

echo "    Copying configuration files from landscape to setup ..."
cp /shared/landscapes/$1/config/* /shared/eln/config/