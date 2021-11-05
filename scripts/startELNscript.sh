#!/bin/bash
echo Running the start ELN script

cd /chemotion/app
# bundle exec rails s
exec passenger start -e production --engine=builtin --address 0.0.0.0 --port 3000