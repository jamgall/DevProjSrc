import psycopg2 as post
import sys
import os
import csv
import to_csv

to_add = []
config = {
	'host':'localhost',
	'dbname':'test'
}
check = [10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
con_keys = ['user']

# writes the configurations for connecting to the postgres db
def write_config():
	global config
	for key in con_keys:
		if key not in config:
			resp = raw_input('Please enter the exact %s you are using: ' % key)
			config[key] = resp

# allows the user to convert the .txt file to csv and add it to the db line by line
def main():
	print('######Connecting to Database######')
	# if there are connection errors, handle them and print them out to the console
	try:
		conn = post.connect(**config)
	except post.OperationalError as e:
		print('Unable to connect!\n{0}').format(e)
		sys.exit(1)
	cnx = conn.cursor()
	print('##### Connected! #####\n\n')

	filename = to_csv.main()
	print('loading database...')
	count = 0
	with open(filename, 'r') as file:
		csvread = csv.reader(file)
		for row in csvread:
			add = row[0]
			if add.find("'") == -1:
				count += 1
				if(check and count == check[0]):
					print('Currently on record: %d' % count)
					check.pop(0)
					conn.commit()
				cnx.execute("INSERT INTO pass (word) VALUES ('%s') ON CONFLICT (word) DO NOTHING;" % (add))
	conn.commit()
	os.remove(filename)
	cnx.close()
	print('...database loaded')
	return 0


if __name__=="__main__":
	main()