
contacts = {}

def find(name):
	for key, value in contacts.items():
		if key == name:
			return True
	return False


def create(name, phone):
	contacts[name] = phone


def read():
	return contacts.items()

def delete(name):
	del contacts[name]
	return True

def update(name, new_name, new_phone):
	delete(name)    # delete old contact
	create(new_name, new_phone)     # add new contact
	return True
	







	

	
	