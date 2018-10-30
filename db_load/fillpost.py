import psycopg2 as post
import csv
import to_csv

to_add = []
config = {
	'host':'localhost',
	'dbname':'password',
	'user':'jamgall'
}

def main():
	to_csv.main()
	conn = post.connect(**config)
	cnx = conn.cursor()
	print('Connected!')
	filename = raw_input('Please enter name of csv file to read in: ')
	with open(filename, 'r') as file:
		csvread = csv.reader(file)
		for row in csvread:
			#print row
			add = row[0]
			if add.find("'") == -1:
				cnx.execute("INSERT INTO pass (word) VALUES (\'%s\');" % (add))
	print 'HEY LOOK AT THAT IT FUCKING WORKED'
	conn.commit()
	return 0


if __name__=="__main__":
	main()