import unittest
from my_sum import my_sum

class MySumTest(unittest.TestCase):


	def test_sum_of_digits(self):
		self.assertEqual(my_sum(10, 15), 25)


	def test_for_null(self):
		self.assertIsNotNone(my_sum(10, 15), 0)

	def test_non_numbers(self):
		self.assertNotEqual(my_sum('jo', 'jo'), 0, msg="please provide integers")





if __name__=='__main__':
	unittest.main()

