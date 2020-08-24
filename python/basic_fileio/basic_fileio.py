def print_file_contents(file_name, odd=None , line_nos=True ):
    f = open(file_name,'r')
    no = 0
    e = 0
    o = 0
    for i in f.readlines():
        no = no +1
        if odd == False:
            if line_nos == True:
                if no % 2 == 0:
                    e = no
                    print (e,i)   
            if line_nos == False:
                if no % 2 == 0:
                    e = no
                    print (i)          
        if odd == True:
            if line_nos == True:       
                if no % 2 == 1:                    
                    o = no    
                    print (o,i)
            if line_nos == False:
                if no % 2 == 1:                    
                    o = no
                    print (i)         
        if odd == None:
            if line_nos == False:
                print(i)
            if line_nos == True:
                print (no,i)

def find_lines(file_name, word, ignore_case=True, match_whole_word=True):
    f=open(file_name,'r')
    a = f.readlines()

    #If upper case or lower case input doesnt matter
    if ignore_case == True:
        #accepting the partial word and returning the whole word
        if match_whole_word == True:
            #parsing through the lines of file with variable line
            for line in a:
                #for making case insensitive
                if word.lower() in line.lower():
                    print (line)
        #not accepting the partial word and returning only the input word            
        if match_whole_word == False:
            #parsing line by line
            for line in a:
                #splitting for not returning unmatched words
                splitted = line.split()
                #ignoring cases
                if word.lower() in splitted:
                    print (line)
    
    if ignore_case == False:
        if match_whole_word == True:
            for line in a:
                if word in line:
                    print (line)
        if match_whole_word == False:
            for line in a:
                splitted = line.split()
                if word in splitted:
                    print (line)
 

if __name__ == "__main__":
    #this will be called as file name as file_name odd is none and line nos is true
    #print_file_contents('my_file.txt',False,False)
    #this will be called with odd as true
    #print_file_contents('my_file.txt', ,True)
    
    print("printing this with", "('my_file.txt', line_nos=True)")
    print_file_contents('my_file.txt',line_nos=True)
    
    print("printing this with", "('my_file.txt', odd=True , line_nos=False)")
    print_file_contents('my_file.txt', True , False )
   
    print ("printing this with","finding_lines('my_file.txt', 'TiS', ignore_case=True, match_whole_word=False)")
    find_lines('my_file.txt', 'TiS', ignore_case=True, match_whole_word=False)

    print ("printing this with","finding_lines('my_file.txt', 'TiS', ignore_case=False, match_whole_word=True)")
    find_lines('my_file.txt', 'tissue', ignore_case=False, match_whole_word=True)