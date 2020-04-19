from ..api import contact



SEP = ':'

def write(filename, name, phone):
	with open(filename, 'w') as contact_file:
		contact_file.write(f'{name}{SEP}{phone}\n')
		return True
	return False


def read(filename):
	with open(filename, 'r') as contact_file:
		return contact_file.readlines()
	