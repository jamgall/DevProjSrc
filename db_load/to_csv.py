import csv

to_add = []

def read_in():
	global to_add
	filename = raw_input('Please enter name of file to add: ')
	count = 1
	with open(filename, 'rw') as file:
		for line in file:
			line = line.strip('\n')
			to_add.append(line)

def write_csv():
	print('writing...')
	with open('pass_fill.csv', 'w') as file:
		writer = csv.writer(file)
		for row in to_add:
			writer.writerow([row])
	print('...done')

def main():
	read_in()
	write_csv()
	return 0


if __name__=="__main__":
	main()