# Funcion of inverting 
# variable array as parameter
def invert_array(array):
	# python starts from 0 len starts from 1
	len_array = len(array) - 1

	# For traversing through the array
	for i in range(len(array)):
		# swapping the positions of first and last and so on
		array[i], array[-(i + 1)] = array[-(i + 1)], array[i]

		# to break the 'or' loop when reaching the middle element
		if i >= ((len_array)-1)/2 :
			print (array)
			return array
#function of sorting
#variable array as a parameter 
def sort_array(array):

	#using bubble sort
	#for traversing through the array
	for i in range(len(array)):
		#for traversing through the array ranging from next number to i
		for j in range(i+1, len(array)):
			#compairing i and j to find smaller number
			if array[j] < array[i]:
				#swapping the positions of greater and smaller number
				array[i], array[j] = array[j], array[i]
	print (array)
	return array

# checking the ouput
if __name__ == '__main__':
	invert_array([83, 55, -4, 14, 18, 77])
	invert_array([83, 55, -4, 14, 18])
	invert_array([2, 3, 4])
	sort_array([65,89,-9,12,0])
	sort_array([90,130,-55,1,40])
	sort_array([44,9,84,9,11])
