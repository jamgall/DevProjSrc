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
* Install psycopg2 by running `pip install psycopg2` and `pip install psycopg2-binaries`
* Unzip the `pass.zip` file from the current directory
* Run the following command `python fillpost.py`
	* The program will ask you to give your postgres username and database name. (You must create a postgres user that does not require a password)
	* When prompted, give the name of the unzipped .txt file
	* The above program will take about 5 minutes to run and will insert ~1,000,000 lines of the ~14,000,000 line file (working on fixing this problem)
* After the program concludes, you can connect to the database by running: `psql dbname`
