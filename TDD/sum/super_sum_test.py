import unittest
from super_sum import super_sum


class SuperSumTest(unittest.TestCase):

	# first test to check sum of elements in input as list
	def test_element_sum(self):
		self.assertEquals(super_sum([10, 5, 6, 9]), 30, msg = "element sum not valid")


	def test_for_validity(self):
		self.assertTrue(super_sum([10,10,10]), 130)

	def test_for_strings(self):
		self.assertEquals(super_sum('Jojo'), 0)

	def test_for_list(self):
		self.assertEquals(super_sum([1,2,3,4]), 10)

	def test_for_null(self):
		self.assertEquals(super_sum(''), 0)




if __name__=='__main__':
	unittest.main()

# super_sum(10, 5, 6, 9) => 30
# super_sum([10, 5], 5) => 20
# super_sum([5, 6], [4, 5], 10) => 30


# assertFalse(self, expr, msg=None) unbound unittest.case.TestCase method
   #  Check that the expression is false.
   # assertTrue(self, expr, msg=None) unbound unittest.case.TestCase method