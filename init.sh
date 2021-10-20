#!/bin/bash

ln -s /template /shared/eln
mv /shared/eln/config/database.yml.example /shared/eln/config/database.yml
mv /shared/eln/config/datacollectors.yml.example /shared/eln/config/datacollectors.yml
mv /shared/eln/config/storage.yml.example /shared/eln/config/storage.yml

# mv /chemotion/app/config/database.yml.example /chemotion/app/config/database.yml
# mv /chemotion/app/config/datacollectors.yml.example /chemotion/app/config/datacollectors.yml
# mv /chemotion/app/config/storage.yml.example /chemotion/app/config/storage.yml

cat <<EOF > /chemotion/app/config/database.yml
production:
  adapter: postgresql
  encoding: unicode
  database: chemotion
  pool: 5
  username: postgres
  password: postgres
  host: db
EOF

cat <<EOF > /chemotion/app/config/secrets.yml
production:
  secret_key_base: "29083465982734598723458796234897562349857623789562345967"
EOF

# psql --host 'db' --username 'postgres' -c "CREATE ROLE postgres LOGIN CREATEDB NOSUPERUSER PASSWORD 'postgres';"
# psql --host 'db' --username 'postgres' -c "CREATE DATABASE chemotion OWNER postgres;"

# export DISABLE_DATABASE_ENVIRONMENT_CHECK=1

cd /chemotion/app

# bundle exec rake db:drop db:create db:migrate db:seed
bundle exec rake assets:precompile
# bundle exec rails c

