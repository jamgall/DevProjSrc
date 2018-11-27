import psycopg2 as post
import sys
import os
import csv
import to_csv

to_add = []
config = {
	'host':'localhost',
	'dbname':'password'
}
check = [10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]

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
					print( '%d records committed' % count)
					check.pop(0)
					conn.commit()
				cnx.execute("INSERT INTO pass (word, count) VALUES ('%s', 1) ON CONFLICT (word) DO UPDATE SET count = pass.count + 1;" % (add))
	conn.commit()
	os.remove(filename)
	cnx.close()
	print('...database loaded')
	return 0


if __name__=="__main__":
	main()
