#!/bin/bash

for host in finder supplier vendor
do
    gcloud beta compute ssh --zone "us-central1-a" "$host" --project "otel-starter-project" -- << ENDSSH
    sudo -u foodfinder -HE sh -c 'cd /home/foodfinder/opentelemetry-starter && git checkout opencensus && git pull'
    sudo systemctl restart $host.service
ENDSSH
done
