import csv

to_add = []
filename = ''

def read_in():
	global to_add
	filename = raw_input('Please enter name of file to add: ')
	count = 1
	with open(filename, 'rw') as file:
		for line in file:
			line = line.strip('\n')
			to_add.append(line)

def write_csv():
	print('\nwriting...')
	with open('temp.csv', 'w') as file:
		writer = csv.writer(file)
		for row in to_add:
			writer.writerow([row])
	print('...done\n')

def main(fle):
	global filename
	filename = fle
	print('###### Converting file to .csv ######')
	read_in()
	write_csv()
	return 'temp.csv'


if __name__=="__main__":
	main()