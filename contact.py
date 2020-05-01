# Phonebook app 
# @saeidxgholami
# logic

import txtfile



contacts = []


def read():
	return contacts


def create(name, phone):
	contact = f'{name}:{phone}\n'
	contacts.append(contact)


def find(name):
	contacts = read()
	for contact in contacts:
		n, p = contact.split(':')
		if name == n:
			return contact
	return False


def delete(name):
	contacts = read()
	contact = find(name)
	if contact:
		contacts.remove(contact)
		return True
	return False


def update(name, new_name, new_phone):
	contacts = read()
	contact = find(name)
	if contact:
		index = contacts.index(contact)
		contacts[index] = f'{new_name}:{new_phone}\n'
		return True
	return False


if __name__ == '__main__':
	
	
	# create('john', '2343')
	# create('jack', '333')
	# create('jim', '9938')

	# I have to read content of the file before doing anything
	# and I have to write all data before quiting the app.

	contacts = txtfile.read('contacts.txt')

	txtfile.write('contacts.txt', contacts)


	print(contacts)