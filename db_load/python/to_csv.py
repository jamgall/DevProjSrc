import csv
import os

to_add = []

def read_in(filename):
	global to_add
	#print ("Converting file: %s" % filename)
	count = 1
	with open('../dicts/' + filename, 'rw') as file:
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

def main():
	print('###### Converting files to CSV ######')
	for fle in os.listdir('../dicts/'):
		if fle[-4:] != ".zip":
			read_in(fle)
			write_csv()
	print('###### Converted! ######')
	return 'temp.csv'


if __name__=="__main__":
	main()