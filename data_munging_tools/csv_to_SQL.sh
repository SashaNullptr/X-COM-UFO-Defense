#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PROJECT_DIR="$(dirname $SCRIPT_DIR)"
CSV_PATH="$PROJECT_DIR/data_sets/ufo-sightings.csv"

CREATE_DB_COMMAND="
CREATE DATABASE ufo_db
"

CREATE_TABLE_COMMAND="
CREATE TABLE ufo_data (
    id SERIAL,
    occurred_at TIMESTAMP,
    city TEXT,
    state CHAR(2),
    country CHAR(2),
    shape TEXT,
    duration_seconds FLOAT8,
    duration_text TEXT,
    description TEXT,
    reported_on DATE,
    latitude FLOAT8,
    longitude FLOAT8
)
"

DUMP_CSV_COMMAND="
COPY ufo_data (id, occurred_at,city,state,country,shape,duration_seconds,duration_text,description,reported_on,latitude,longitude)
FROM '$CSV_PATH' DELIMITER ',' CSV HEADER;
"

export PGPASSWORD='postgres';

psql -U 'postgres' -h 127.0.0.1 -c "$CREATE_DB_COMMAND"
psql -U 'postgres' -d 'ufo_db' -h 127.0.0.1 -c "$CREATE_TABLE_COMMAND"
psql -U 'postgres' -d 'ufo_db' -h 127.0.0.1 -c "$DUMP_CSV_COMMAND"
