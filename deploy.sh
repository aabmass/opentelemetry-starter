#!/bin/bash

## Optionally, pass BRANCH envar (defaults to master)

for host in finder supplier vendor
do
    gcloud beta compute ssh --zone "us-central1-a" "$host" --project "otel-starter-project" -- << ENDSSH
    sudo -u foodfinder -HE bash << ENDSUDO
        cd /home/foodfinder/opentelemetry-starter
        git checkout ${BRANCH:-master}
        git pull
ENDSUDO
    sudo systemctl restart $host.service
ENDSSH
done
