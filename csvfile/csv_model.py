# model
# store data in a csv file

import csv



def write(filename, contacts):
	with open(filename, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(contacts)
		


def read(filename):
	try:
		with open(filename, 'r') as f:
			reader = csv.reader(f)
			return list(reader)
	except FileNotFoundError as e:
		print('File not found')
		print(f'Creating {filename}')
		f = open(filename, 'w')
		f.close()
		print(f'File creation was successful.')
