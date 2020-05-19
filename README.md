# OpenTelemetry Starter

The goal here is to create three services simulating a system to find food
stocks. At first, the services will be instrumented with OpenCensus. Then,
the same services will be instrumented with OpenTelemetry. Tracing and
metrics need to be sent to Google Cloud Monitoring (Stackdriver).

## Setup

In a shell:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.dev.txt
```

## Generate proto/gcp stubs

Run the codegen.sh script.

## Running each service
TODO