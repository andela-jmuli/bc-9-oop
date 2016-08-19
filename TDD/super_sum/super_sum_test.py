import unittest
from super_sum import super_sum


class SuperSumTest(unittest.TestCase):

	# first test to check sum of elements
	def test_element_sum(self):
		self.assertEquals(super_sum([10, 5, 6, 9]), 30, msg = "element sum not valid")

	# this identifies validity of output given
	def test_for_validity(self):
		self.assertTrue(super_sum([10,10,10]), 130)

	# this check tests for Null and prompts for input if none is provided
	def test_for_null(self):
		self.assertEquals(super_sum(), 0, msg="Please provide arguments")

	# this test checks for Strings as input and prompts for datachange
	def test_for_strings(self):
		self.assertEquals(super_sum('Jojo'), None, msg="Please input a Numerical value")

	# this test checks for a list as an input
	def test_for_list(self):
		self.assertEquals(super_sum([1,2],3), 6)





if __name__=='__main__':
	unittest.main()

