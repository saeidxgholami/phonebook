# Text(Termina, console) base version of PhoneBook application
# Features: Create, Find, Update, Delete contact and Display contacts
# author: @saeidxgholami

import contact


messages = {
	'nf': 'Not Found',
	'succ': 'Success',
	'err': 'Some error occurred.'
}



def menu():
	menu_items = [
		"Create a contact",
		"Display Contacts",
		"Find a Contact",
		"Update a  Contact",
		"Delete a  Contact",
		"Quit",
	]
	for index, item in enumerate(menu_items, 1):
		print(f"[{index}] {item}")

	response = input("Please choose from menu:\n>>  ")
	return response



def create_contact():
	name = input("Name: ")
	phone = input("Phone: ")
	if contact.create(name, phone):
		print(messages.get('succ'))
	else:
		print(messages.get('err'))


def display_contacts():
	for name, phone in contact.read():
		print(name, phone) 


def find_contact():
	name = input("Enter a name to find: ")
	found = contact.find(name)
	if found:
		print(contact.contacts[name])
	else:
		print(messages.get('nf'))

def update_contact():
	name = input("Enter a name to update: ")
	found = contact.find(name)
	if found:
		new_name = input("New Name: ")
		new_phone = input("New Phone: ")
		if contact.update(name, new_name, new_phone):
			print(messages.get('succ'))
		else:
			print(messages.get('err'))
	else:
		print(messages.get('nf'))


def delete_contact():
	name = input("Enter a name to update: ")
	found = contact.find(name)
	if found:
		contact.delete(name)
		print(messages.get('succ'))
	else:
		print(messages.get('nf'))


def quit_app():
	import sys
	print('quiting program...')
	sys.exit()


actions = {
	'1': create_contact,
	'2': display_contacts,
	'3': find_contact,
	'4': update_contact,
	'5': delete_contact,
	'6': quit_app,
}
def main():
	while True:
		response = menu()
		if actions.get(response) is not None:
			actions[response]()
		else:
			print(messages.get('err'))


if __name__ == '__main__':
	main()