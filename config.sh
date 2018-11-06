#!/bin/bash

# This file will install what is necessary for the application to run

pip install -r db_load/requirements.txt

brew install postgresql

# Initialize the database using the pg_dump
cd db_load/
unzip db.zip

createdb -E LATIN9 --lc-collate C --lc-ctype C -T template0 password
psql password<dbexport.pgsql

