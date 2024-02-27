#! /usr/bin/env bash

poetry env use 3.11

## Install dependencies
poetry lock
poetry install

source $(poetry env info --path)/bin/activate

## Set up database
DB_NAME="fastapi_db"
DB_USER="postgres"

## Check if the database exists
if psql -U "$DB_USER" -lqt | cut -d \| -f 1 | grep -qw "$DB_NAME"; then
    echo "Database $DB_NAME already exists."
else
    echo "Database $DB_NAME does not exist. Creating..."
    createdb -U "$DB_USER" -w "$DB_NAME"
    echo "Database $DB_NAME created."
fi

## Migrate database
alembic upgrade head

python -m app.init_db
