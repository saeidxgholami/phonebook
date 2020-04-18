
contacts = []


while True:
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

	if response == '1':
		name = input("Name: ")
		phone = input("Phone: ")
		contacts.append(name)
		contacts.append(phone)
	elif response == '2':
		for contact in contacts:
			print(contact)
	elif response == '3':
		name = input("Enter a name to search: ")
		for contact in contacts:
			if contact == name:
				print(contact, contacts[contacts.index(contact)+1])
	elif response == '4':
		name = input('Contact name: ')
		if contacts.count(name) > 0:
			index_contact = contacts.index(name)
			contacts[index_contact] = input('New Name: ')
			contacts[index_contact+1] = input('New Phone: ')
			print('updated!')
		else:
			print('not found')
	elif response == '5':
		name = input('contact name to delete: ')
		if contacts.count(name) > 0:
			contacts.remove(name)
			phone_index = contacts.index[name] + 1
			del contacts[phone_index]
		else:
			print('not found')
	elif response == '6':
		break