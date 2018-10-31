# Instructions for Database initialization locally
## Written by: James Gallmeister

Written for postgres 10.5
If you don't have 10.5, you may need to update it.

To initialize the database run the following command:
* `createdb -E LATIN9 --lc-collate C --lc-ctype C -T template0 dbname`

Included in this file is a .pgsql that should initialize and fill the database
To run the .pgsql file run the following
* `psql -U username dbname < passdb.pgsql`

If the above .pgsql does not work for whatever reason, do the following:
* Create a table in psql with the following command `create table tbname(id serial primary key, word text unique);
* Install psycopg2 by running `pip install psycopg2` and `pip install psycopg2-binaries`
* Unzip the `pass1.zip` and `pass2.zip` file from the current directory
* Run the following command `python fillpost.py`
	* The program will ask you to give your postgres username and database name. (You must create a postgres user that does not require a password)
	* When prompted, give the name of the unzipped .txt file and the table name you created from above.
	* The above program will take longer for larger files. It keeps a running count so you know how many records have been committed that displays to console.
* After the program concludes, you can connect to the database by running: `psql dbname`
* If you need to add more than one file, you will need to run the program more than once (This will be fixed later on)
