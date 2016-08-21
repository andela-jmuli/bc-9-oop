


class NotesApplication(object):
	"""
	Class notes application
	"""
	def __init__(self, author, note_list=[]):

		# if author == '' or len(note_list) == 0:
		# 	raise TypeError('Arguments expected, Null provided')
		# elif type(note_list) != list:
		# 	raise TypeError('List expected as argument 2')
			
		self.author = author
		self.note_list = note_list



	def create(self, note_content):
		'''
	This method takes note content as the parameter and adds new note data to the list 'note_list'
		'''
		if note_content == None:
			raise TypeError('List should not be empty')
			
		else:
			note_data = self.note_list.append(note_content)
			# print type(self.note_list)
			return note_data


	def list(self):
		'''
	This method displays notes with each author object present
		'''

		auth = 'By Author'
		for k, v in enumerate(self.note_list):
			
			line_data = str(k) + v + auth + self.author
			
			return line_data



	def get(self, note_id):
		'''
	This function takes a note_id which refers to the index of the note 
	in the notes list and returns the content of that note as a string.
		'''
		note_info = self.notes[note_id]

		return note_info



	def delete(self, note_id):
		'''
	This function deletes the note at the index note_id of the notes list.
		'''
		# this deletes(pops) note data from the (db)note_list in relation to it's note id
		# first checks whether item is existent
		if self.note_list[note_id]:
			deleted = self.note_list.pop(note_id)
			return deleted
		else:
			return 'Note does not exist'



	def edit(self, note_id, note_content):

		'''
	This function replaces the content in the note at note_id with new_content
		'''
		# this edits note content in relation to a note ID in the (db)note_list
		self.note_list[note_id] = note_content
		
		return note_content



	def search(self, search_text):
		'''
	This function take a search string, search_text and returns all
	the notes with that text within it.
		'''
		speak = "Showing results for search '{0}'".format(search_text)
		final = "By author"

		for key, value in enumerate(note_list):
			if value.find(search_text) != -1:

				speech = speak + str(self.note_id) + v + final + self.author

				return speech


# kikapu = []
# nb = NotesApplication('Joseph', kikapu)
# nl = NotesApplication('Rachel', kikapu)

# # print nb.create('what an awesome environment')
# # print nb.list()

# nl.create('mabruki')
# nl.delete(0)

# print nl.list()
