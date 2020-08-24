#funtion of finding the minimum number
def find_min_val(array):
	
	# assigning 1st element of array to minval
	minval=array[0]	
	
	# traversing through the array 
	for element in array:
		# to check whether the next element is smaller than the current
		if element < minval: 
			# if yes assigning that number to minval
			minval = element
	return minval

#funtion of finding the maximum number	
def find_max_val(array):
	# assigning 1st element of array to maxval
	maxval=array[0]
	# to check whether the next element is greater than the current
	for element in array:
		# to check whether the next element is greater than the current
		if element > maxval:
			#if yes assigning that number to maxval
			maxval = element
	return maxval
		
if __name__ == '__main__':
	print (find_min_val([2, 3, 4]))
	print (find_min_val([55,83,14,-4]))
	print (find_max_val([2,3,4]))
	print (find_max_val([55,83,14,-4]))