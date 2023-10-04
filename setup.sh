#! /usr/bin/env bash

poetry env use 3.11

## Install dependencies
poetry lock
poetry install

source $(poetry env info --path)/bin/activate

## Migrate database
alembic upgrade head

python -m app.init_db
