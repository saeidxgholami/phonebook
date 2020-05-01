# textbase ui
# view


import os


import contact  # logic
import txtfile  # model



def display_menu():
	menu_items = [
		'Create a contact',
		'Display a contacts',
		'Find a contact',
		'Update a contact',
		'Delete a contact',
		'Exit',
	]

	for index, item in enumerate(menu_items, 1):
		print(f'[{index}] {item}')


def get_info():
	name = input('Name: ')
	phone = input('Phone: ')
	return name, phone


def create_ui():
	name, phone = get_info()
	contact.create(name, phone)
	print('created successfuly.')


def display_ui():
	cnts = contact.read()
	print(cnts)


def find_ui():
	name = input('Name to find')
	res = contact.find(name)
	print(res)



def update_ui():
	name = input('Name to update: ')
	new_name, new_phone = get_info()
	res = contact.update(name, new_name, new_phone)
	print(res)


def delete_ui():
	name = input('Name to update: ')
	res = contact.delete(name)
	print(res)


def exit_ui():
	print('Exiting ...')
	contacts = contact.read()
	txtfile.write('contacts.txt', contacts)
	exit()



actions = {
	'1': create_ui,
	'2': display_ui,
	'3': find_ui,
	'4': update_ui,
	'5': delete_ui,
	'6': exit_ui,
}

def run():
	contact.contacts = txtfile.read('contacts.txt')

	while True:
		os.system('cls') if os.name == 'nt' else os.system('clear')

		display_menu()
		response = input('Choose from menu\n> ')

		if actions.get(response) is not None:
			actions[response]()
		else:
			print('Please choose from menu ...')

		input('Press any key back to menu ...')


def main():
	run()


if __name__ == '__main__':
	main()
