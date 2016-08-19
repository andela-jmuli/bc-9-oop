
from datetime import date




class Student(object):

	# class variable
	last_id = 0
	
	def __init__(self, f_name, l_name):
		super(Student, self).__init__()
		self.id = self.generate_id()
		self.f_name = f_name
		self.l_name = l_name


# Make at least 5 students attend class

	def attend_class(self, date, **kwargs):

		# this contains default data outputed if dict not specified
		dee = {teacher: 'Alex', location : 'Hogwarts'}

		if kwargs is not None:
			if date == date.today():
				new_dict = {}
				# this confirms student instance attend_class class in specified date (currently today)
				return True
			return False
		return dee
		


	def generate_id(self):
		# increment class variable with new method call for each instance
		Student.last_id += 1

		# assign id to instance
		i_d = Student.last_id
		# return i_d


