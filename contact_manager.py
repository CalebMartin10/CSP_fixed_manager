class DuplicateContactError(Exception):
    '''
    Creates a class that handles exceptions caused by adding a contact to the list that is already there.
    '''
    def __init__(self, message):
        self.message = message
        message = f" Contact is already in Contacts"
        super().__init__(self.message)

def check_contact(contact, dict):
    '''
    Makes sure a contact list does not already have the contact in it.

    Args:
       contact (str): The name of an individual which is a key in a dictonary
       dict (dict): A dictionary full of people's names and numbers

    Returns:
        An Error called DuplicateContactError
    '''
    if contact in dict:
        raise DuplicateContactError(f"{contact} is already in Contacts")

contacts = {}

def add_contact(name, phone):
    '''
    Adds a contact and their numbers to a list full of them

    Args:
        name (str): A person's name
        phone (str): A person's phone number

    Returns:
        an Error or print statements
    '''
    try:
        check_contact(name, contacts)
        contacts[name] = phone
        print(f"\n| Added {name} to contacts. |")
    except DuplicateContactError:
        print(f"\n| {name} is already in Contacts |")

def find_contact(name):
    '''
    Prints a contacts phone-number
    '''
    try:
        print(contacts[name])
    except KeyError:
        print(f"\n| Contact not found. |")

def delete_contact(name):
    '''
    deletes a contact
    '''
    try:
        del contacts[name]
        print(f"\n| Deleted {name}. |")
    except KeyError:
        print(f"\n| Contact not found. |")

def main():
    '''
    Operates the Contact manager
    '''
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print(f"\nYou have to type in a number between 1 and 4...")
            continue

        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == 2:
            name = input("Enter name to find: ")
            find_contact(name)
        elif choice == 3:
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == 4:
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()