#!/usr/bin/env bash

set -e
set -x

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

# Render templates
python3 render.py

# Run docker compose

docker compose down
docker compose up -d
