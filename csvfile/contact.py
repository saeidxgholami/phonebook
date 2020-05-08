# Phonebook app 
# @saeidxgholami
# logic

import csv_model



def read(filename):
	contact_list = csv_model.read(filename)
	return contact_list


def create(name, phone):
	""" Create a [name, phone] in the contacts list
	"""
	contacts.append([name, phone])


def find(filename, name):
	contacts = read(filename)
	for c_name, phone in contacts:
		if c_name == name:
			return True
	return False


def get_phone(filename, name):
	found = find(filename, name)
	print(found)
	if found:
		contacts = read(filename)
		for cnt_name, phone in contacts:
			if cnt_name == name:
				return phone
	return False				


def delete(filename, name):
	contacts = read(filename)
	contact = find(filename, name)
	if contact:
		for c_name, phone in contacts:
			contacts.remove([c_name, phone])
			break
		csv_model.write(filename, contacts)
		return True
	return False


def update(filename, name, new_name, new_phone):
	contacts = read(filename)
	contact = find(filename, name)
	if contact:
		for c_name, phone in contacts:
			if c_name == name:
				index = contacts.index([c_name, phone])
				contacts[index] = [new_name, new_phone]
				break
		csv_model.write(filename, contacts)
		return True
	return False


if __name__ == '__main__':
	print('Test area ...')
	# create('john', '2343')
	# create('jack', '333')
	# create('jim', '9938')
	
	# csv_model.write('contacts.csv', contacts)
	# cnts = csv_model.read('contacts.csv')
	# found = find('contacts.csv', 'john')
	# n = get_phone('contacts.csv', 'jeff')
	# print(n)
	# r = delete('contacts.csv', 'john')
	# print(r)
	# r = update('contacts.csv', 'jim', 'jeff', '32432')
	# print(r)



	


