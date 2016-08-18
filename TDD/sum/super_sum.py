

def super_sum(*args):
	count = 0

	for y in args:
		if type(y) == list:
			for x in y:
				count += x
		elif type(y) == str:
			return None
		else:
			count = count + x
	return count


print super_sum('')