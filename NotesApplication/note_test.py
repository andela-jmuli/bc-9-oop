import unittest
from notes import NotesApplication


def catchError():
	raise Exception('Please input a proper list')


class NoteAppTest(unittest.TestCase):

	def test_for_input(self):
		kitabu = []
		notebook = NotesApplication('Joseph', kitabu)
		self.assertNotEquals(notebook.create(9), 'word', msg="Please input a String Value")







if __name__ == '__main__':
	unittest.main()