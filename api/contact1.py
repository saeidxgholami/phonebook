# contact api version 1
# using list to do CRUD opertions
# each opertion is a function
# each contact is a string which name, and phone seperated by `:`



contacts = []
def create(name, phone):
	contacts.append(f'{name}:{phone}')


def read():
	return contacts


def find(name):
	contacts = read()
	for contact in contacts:
		c_name, phone = contact.split(':')
		if c_name == name:
			return phone
	return False


def delete(name):
	contacts = read()
	for contact in contacts:
		c_name, phone = contact.split(':')
		if c_name == name:
			contacts.remove(contact)
			return True

	return False


def update(name, new_name, new_phone):
	contacts = read()
	for contact in contacts:
		c_name, phone = contact.split(':')
		if c_name == name:
			index = contacts.index(contact)
			contacts[index] = f'{new_name}:{new_phone}'
			return True
	return False


if __name__ == '__main__':
	print(f'Test area\n{10*"="}')
	create('john', '23423')
	create('jack', '0897')
	cnts = read()

	found = find('john')

	del_r = delete('jack')
	# print(del_r)

	# print(read())
	update('john', 'Jeff', '234234')
	print(read())