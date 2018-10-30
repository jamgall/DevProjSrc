# Instructions for Database initialization locally
## Written by: James Gallmeister

Written for postgres 10.5
If you don't have 10.5, you may need to update it.

To initialize the database run the following command:
	* `createdb -E LATIN9 --lc-collate C --lc-ctype C -T template0 dbname`

Included in this file is a .pgsql that should initialize and fill the database
To run the .pgsql file run the following
	* `psql -U username dbname < passdb.pgsql`

