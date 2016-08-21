import unittest
from notes import NotesApplication




class NoteAppTest(unittest.TestCase):


	def test_for_input(self):
		'''
		Checks for valid input data types
		'''
		kitabu = []
		notebook = NotesApplication('Joseph', kitabu)
		self.assertNotEquals(notebook.create(9), 'word', msg="Please input a String Value")


	def test_for_author_name(self):
		'''
		Checks whether first argument 'author' is provided
		'''
		author = ''
		lister = ['writing unittests']
		notebook = NotesApplication(author, lister)
		self.assertEqual(notebook.author, '', msg="Provide missing argument")


	def test_for_class_instance(self):
		'''
		Checks whether object is instance of class
		'''
		author = 'Joseph'
		content_list = []
		notebook = NotesApplication(author, content_list)
		self.assertIsInstance(notebook, NotesApplication, msg="Check Class instance")


	def test_for_constructor_list(self):
		'''
		Checks whether second argument is of type list
		'''
		author = 'Joseph'
		lister = ['That awkward moment']
		notebook = NotesApplication(author, lister)
		self.assertEqual(type(lister), list, msg="Arguments should provide a list")


	def test_for_constructor_str(self):
		'''
		Checks whether first argument is of type string
		'''
		author = 'Joseph'
		lister = ['A magical place']
		notebook = NotesApplication(author, lister)
		self.assertEqual(type(notebook.author), str, msg="First input should be a String")


	def test_for_empty_note(self):
		'''
		Checks whether note created is blank
		'''
		author = 'Joseph'
		lister = []
		notebook = NotesApplication(author, lister)
		self.assertEqual(notebook.create(" "), None, msg="Note created is empty")


	def test_for_note_deletion(self):
		'''
		raises index error
		'''
		author = 'Joseph'
		lister = ['a random list']
		notebook = NotesApplication(author, lister)
		notebook.create('A random note')

		self.assertEqual(notebook.delete(0), 'Successful Deletion!', msg="Deletion Failed!")




if __name__ == '__main__':
	unittest.main()