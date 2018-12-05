#!/bin/bash

# This file will install what is necessary for the application to run

#a=$(pip list | egrep \'psycopg2\')

#echo $a

#pip list | egrep 'psycopg2'
pip install -r db_load/dependencies/requirements.txt

#install the necessary node packages
npm install

# Initialize the database

createdb -E LATIN9 --lc-collate C --lc-ctype C -T template0 password

psql password<db_load/dependencies/init.sql

cd db_load/dicts/
unzip "*.zip"
#rm *.zip

cd ../python

python fillpost.py

cd ../dicts/
rm pass1.txt pass2.txt
