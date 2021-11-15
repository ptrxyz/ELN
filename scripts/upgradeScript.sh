#!/bin/bash
echo Running the upgrade script 

cd /chemotion/app/

SECRET_KEY="$(bundle exec rake secret)"
cat <<EOF > config/secrets.yml
production:
  secret_key_base: $SECRET_KEY
EOF

echo "    Executing migrations..."
bundle exec rake db:migrate
echo "    Database migrated."

echo "    Creating sprites..."
bundle exec rake ketcherails:import:common_templates
rm -rf /chemotion/app/app/public/images/ketcherails/icons/original/*
bundle exec rails r 'MakeKetcherailsSprites.perform_now'

bundle exec rake assets:precompile