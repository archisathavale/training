# Function of gcd 
# a and b are the two numbers
def gcd(a, b):
	# For swapping higher and lower numbers
	if b>a:
		a,b=b,a
	print ("gcd",a,b)
	# Remainder passed to 'c'
	c=a%b
	
	# while loop for dividing until the remainder is 0
	while c!=0:
		#print (a,b,c)
		# assigning to the prev variable for looping 
		a=b
		b=c
		c=a%b
	#print ('The GCD is...', b)
	return (b)

if __name__ == '__main__':
	print (gcd(15, 40))
	print (gcd(40, 3))
	print (gcd(80, 20))
