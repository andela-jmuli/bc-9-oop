

def super_sum(*args):
	# counter initialized for input length
	count = 0

	# first loop checks input type
	for y in args:

		# if data type is a list, the list is iterated with each element being added to count
		if type(y) == list:

			for x in y:
				count += x

		# second check indentifies strings and returns None since 
		elif type(y) == str:
			return None


		else:
			# this check assumes input has integers and sums the total to count
			count = count + y

	# final value is returned 
	return count


super_sum([2,3])