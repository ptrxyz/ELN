#!/bin/bash

case "$1" in
    shell)
        exec /bin/bash
        ;;
    *)
        python3 /shared/CLI.py $1
        ;;
esac
