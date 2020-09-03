addressbook={}
# Empty Dictionary

# Function of adding an address
# email is the key and name is the value
def add_address(email , name):
	addressbook [email] = name
	#print (addressbook)
	return (email, name)

# Function of deleting an address
# only key is enough to delete the value in a dictionary
def dele_address(email):
	del addressbook[email]
	#print (addressbook)
	return (email)

# Function of printing the addressbook
def print_address():
	print (addressbook)
	return (addressbook)

# Passing parameters
if __name__ == '__main__' :
	add_address('archisathavale', 'Archis')
	add_address('avinashathavale', 'Avinash')
	add_address('arnavathavale','Arnav')
	dele_address('arnavathavale')
	dele_address('avinashathavale')
	add_address('pankajaathavale', 'Pankaja')
	print_address()
