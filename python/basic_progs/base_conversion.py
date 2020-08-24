def convert_int_base(integer, base = 'binary'):
    """Returns a string of integer, converted into given base
    """ 

    #Converting the base into lower case for simplicity 
    base = base.lower()
    #Taking integer as int()
    quotient = int(integer)
    #1. If loop for converting integer into 'Binary' 
    if base == 'binary':
        #2. Make empty list for storing each number
        binary_list = []
        #3. while loop for checking if quetioent is not 0 
        #   and appending remainders into the list till quetioent is 0 
        while quotient != 0:
            remainder = quotient % 2
            binary_list.append(remainder)
            quotient = int(quotient / 2)
        #4. Reversing the list for representation of binary number    
        binary_list.reverse()
        #5. Returning a string of contents in the list
        bin_string = ''.join(map(str, binary_list))
        return bin_string

    if base == 'hexadecimal':
        hexadecimal_list = []
        hex_dict = { 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        while quotient != 0:
            remainder = quotient % 16
            if remainder in hex_dict.keys():
                remainder = hex_dict.get(remainder)              
            hexadecimal_list.append(remainder)
            quotient = int(quotient / 16)
        hexadecimal_list.reverse()
        hex_string = ''.join(map(str, hexadecimal_list))
        return hex_string


    if base == 'octal':
        octal_list = []
        while quotient != 0:
            remainder = quotient % 8
            octal_list.append(remainder)
            quotient = int(quotient / 8)
        octal_list.reverse()
        oct_string = ''.join(map(str, octal_list))
        return oct_string

#1. Function for converting an integer to any base upto 16 
def convert_int_base_simple(integer , base = 2):
    #2. Initialize empty dictionary 
    digits = []
    #3. Making a string of all hex digits
    hex_digits = '0123456789ABCDE'
    #4. while loop for conversion till quotient is zero
    while integer > 0:
        remainder = integer % base
        digits.append(hex_digits[remainder])
        integer = integer // base
    #5. Reversing the contents of list and cutting the spaces between them
    # Storing it in a variable 
    answer = "".join(digits[::-1])
    return answer

if __name__ == "__main__":
    print (convert_int_base(7))
    print ('\n')
    print (convert_int_base(20, 'Binary'))
    print('\n')
    print (convert_int_base(174, 'hexadecimal'))
    print ('\n')
    print (convert_int_base(210, 'OcTaL')) 
    print ('\n')  
    print (convert_int_base_simple(174 , 16))