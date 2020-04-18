# Text(Termina, console) base version of PhoneBook application
# Features: Create, Find, Update, Delete contact and Display contacts
# author: @saeidxgholami

import contact



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
		print('Contact created successfuly.')
	else:
		print('Error')


def display_contacts():
	for name, phone in contact.read():
		print(name, phone) 


def find_contact():
	name = input("Enter a name to find: ")
	found = contact.find(name)
	if found:
		print(contact.contacts[name])
	else:
		print('not found')

def update_contact():
	name = input("Enter a name to update: ")
	found = contact.find(name)
	if found:
		new_name = input("New Name: ")
		new_phone = input("New Phone: ")
		if contact.update(name, new_name, new_phone):
			print('Updaetd!')
		else:
			print('Error in update!')
	else:
		print('Contact not found.')


def delete_contact():
	name = input("Enter a name to update: ")
	found = contact.find(name)
	if found:
		contact.delete(name)
	else:
		print('not found')


def main():
	while True:
		response = menu()
		# Create contact
		if response == '1':
			create_contact()
		# display contacts
		elif response == '2':
			display_contacts()
		# find contacts
		elif response == '3':
			find_contact()
		# update a contact
		elif response == '4':
			update_contact()
		# delete a contact
		elif response == '5':
			delete_contact()
		# quit
		elif response == '6':
			break


if __name__ == '__main__':
	main()