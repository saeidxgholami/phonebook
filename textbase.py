import contact



def menu():
	menu_items = [
		"1. Create a contact",
		"2. Display Contacts",
		"3. Find a Contact",
		"4. Update a  Contact",
		"5. Delete a  Contact",
		"6. Quit",
	]
	for item in menu_items:
		print(item)

	response = input("Please choose from menu:\n>>  ")
	return response
# Text(Termina, console) base version of PhoneBook application
# Features: Create, Find, Update, Delete contact and Display contacts
# author: @saeidxgholami


def main():
	while True:
		response = menu()
		if response == '1':
			name = input("Name: ")
			phone = input("Phone: ")
			contact.create(name, phone)
			print('Contact created successfuly.')
		elif response == '2':
			for name, phone in contact.read():
				print(name, phone) 
		elif response == '3':
			name = input("Enter a name to find: ")
			found = contact.find(name)
			if found:
				print(contact.contacts[name])
			else:
				print('not found')
		elif response == '4':
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
		elif response == '5':
			name = input("Enter a name to update: ")
			found = contact.find(name)
			if found:
				contact.delete(name)
			else:
				print('not found')
		elif response == '6':
			break


if __name__ == '__main__':
	main()