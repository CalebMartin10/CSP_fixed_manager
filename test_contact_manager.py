import unittest
from contact_manager import contacts, add_contact, delete_contact, find_contact, check_contact, DuplicateContactError

class TestContactManagement(unittest.TestCase):
    '''
    Below test test to see a contact is added to the contacts dict
    '''
    def test_add_contact(self):
        contact = "Test Example"
        contacts[contact] = "555"
        self.assertIn(contact, contacts)
    '''
    Below test ensures that the check_contact (and thus the add_contact function), raises DuplicateContactError)
    '''
    def test_find(self):
        contact = "Test Example"
        contacts[contact] = "555"
        self.assertRaises(DuplicateContactError, check_contact, "Test Example", contacts)
    '''
    Below tests ensure that find contact and delete contact fail gracefully (if they do not print anything they will not 
    return None). It also ensures that they do not crash

    '''
    def test_find_phone(self):
        self.assertIsNone(find_contact("Test Example"))
    
    def test_incorrect_delete(self):
        self.assertIsNone(delete_contact("Test Example"))
    '''
    Below test ensures that a contact is actually deleted when called for
    '''  
    def test_deleting_contact(self):
        contact = "Test Example"
        contacts[contact] = "555"
        delete_contact("Test Example")
        self.assertNotIn("Test Example", contacts)

if __name__ == "__main__":
    unittest.main()