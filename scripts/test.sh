#!/usr/bin/env bash

set -euxo pipefail

## Set up database
DB_NAME="fastapi_db_test"
DB_USER="postgres"

## Check if the database exists
if psql -U "$DB_USER" -lqt | cut -d \| -f 1 | grep -qw "$DB_NAME"; then
    echo "Database $DB_NAME already exists."
else
    echo "Database $DB_NAME does not exist. Creating..."
    createdb -U "$DB_USER" -w "$DB_NAME"
    echo "Database $DB_NAME created."
fi

poetry run pytest app/tests
