import psycopg2 as post
import sys
import csv
import to_csv

to_add = []
config = {
	'host':'localhost'
}
con_keys = ['dbname', 'user']

# writes the configurations for connecting to the postgres db
def write_config():
	global config
	for key in con_keys:
		if key not in config:
			resp = raw_input('Please enter the exact %s you are using: ' % key)
			config[key] = resp

# allows the user to convert the .txt file to csv and add it to the db line by line
def main():
	filename = to_csv.main()
	print('######Connecting to Database######')
	write_config()
	# if there are connection errors, handle them and print them out to the console
	try:
		conn = post.connect(**config)
	except post.OperationalError as e:
		print('Unable to connect!\n{0}').format(e)
		sys.exit(1)
	cnx = conn.cursor()
	print('##### Connected! #####\n\n')
	with open(filename, 'r') as file:
		csvread = csv.reader(file)
		print('loading database...')
		for row in csvread:
			#print row
			add = row[0]
			if add.find("'") == -1:
				cnx.execute("INSERT INTO pass (word) SELECT \'%s\' WHERE NOT EXISTS (SELECT word FROM pass WHERE word = \'%s\');" % (add, add))
	print('...database loaded')
	conn.commit()
	cursor.close()
	return 0


if __name__=="__main__":
	main()
