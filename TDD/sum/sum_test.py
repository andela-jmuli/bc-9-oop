import unittest
from my_sum import my_sum

class MySumTest(unittest.TestCase):


	def test_sum_of_digits(self):
		self.assertEqual(my_sum(10, 15), 25)


	def test_for_null(self):
		self.assertIsNotNone(my_sum(10, 15), 0)

	# def test_for_non_numbers(self):
	# 	'''
	# 	Assertion throwing of exception when it's a non-number
	# 	'''
	# 	self.assertFalse(my_sum(10, 15), 25)

	# def test_for_strings(self):
	# 	self.assertEquals(my_sum('Jo', 'jo'), 'Not valid')





if __name__=='__main__':
	unittest.main()


# msg 2  msg = 'Please check arguments for none integers'
# msg 3  msg = "results shouldn't be null"