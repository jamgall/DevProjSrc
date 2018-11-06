#!/bin/bash

# This file will install what is necessary for the application to run

pip install -r db_load/manual_loadin/requirements.txt

# Initialize the database

createdb -E LATIN9 --lc-collate C --lc-ctype C -T template0 password

psql password<db_load/manual_loadin/init.sql

cd db_load/manual_loadin/dicts/
unzip "*.zip"
#rm *.zip

cd ../

python fillpost.py