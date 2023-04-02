#!/bin/bash


# basic run command without docker == gunicorn -w 2 -k uvicorn.workers.UvicornWorker app.main:app

# for docker
RUN_PORT=${RUN_PORT:-8000}
/usr/local/bin/gunicorn -w 2 -k uvicorn.workers.UvicornWorker app.main:app --bind "0.0.0.0:${RUN_PORT}"

