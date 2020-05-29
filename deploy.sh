#!/bin/bash

## Optionally, pass BRANCH envar (defaults to master)

for host in finder supplier vendor
do
    gcloud beta compute ssh --zone "us-central1-a" "$host" --project "otel-starter-project" -- << ENDSSH
    sudo -u foodfinder -HE bash << ENDSUDO
        cd /home/foodfinder/opentelemetry-starter
        source venv/bin/activate
        git pull
        git checkout ${BRANCH:-master}
        pip install -r requirements.dev.txt
ENDSUDO
    sudo systemctl restart $host.service
ENDSSH
done
