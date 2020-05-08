# model
# store data in a text file


def write(filename, contacts):
	with open(filename, 'w') as f:
		for contact in contacts:
			f.write(contact)


def read(filename):
	with open(filename, 'r') as f:
		return f.readlines()
