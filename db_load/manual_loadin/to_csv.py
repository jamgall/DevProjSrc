import csv

to_add = []
filename = ''

def read_in(filename):
	global to_add
	#print ("Converting file: %s" % filename)
	count = 1
	with open('dicts/' + filename, 'rw') as file:
		for line in file:
			line = line.strip('\n')
			to_add.append(line)

def write_csv():
	#print('\nwriting...')
	with open('temp.csv', 'w') as file:
		writer = csv.writer(file)
		for row in to_add:
			writer.writerow([row])
	#print('...done\n')

def main(fle):
	global filename
	filename = fle
	if fle[-4:] != ".zip":
		print('###### Converting file to .csv ######')
		read_in(filename)
		write_csv()
		print('###### Converted! ######')
	return 'temp.csv'


if __name__=="__main__":
	main()