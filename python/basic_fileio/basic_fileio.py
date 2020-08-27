def return_file_contents(file_name, odd=None , line_nos=True ):
    f = open(file_name,'r')
    no = 0
    e = 0
    o = 0
    lines_list = []
    for i in f.readlines():
        no = no +1
        if odd == False:
            if line_nos == True:
                if no % 2 == 0:
                    line_str = str(no) + " " + i.strip()
                    lines_list.append(line_str)
            if line_nos == False:
                if no % 2 == 0:
                    line_str = "" + i.strip()
                    lines_list.append(line_str)   
        if odd == True:
            if line_nos == True:       
                if no % 2 == 1:
                    line_str = str(no) + " " + i.strip()
                    lines_list.append(line_str)
            if line_nos == False:
                if no % 2 == 1:
                    line_str = "" + i.strip()
                    lines_list.append(line_str)
        if odd == None:
            if line_nos == False:
                line_str = "" + i.strip()
                lines_list.append(line_str)
            if line_nos == True:
                line_str = str(no) + " " + i.strip()
                lines_list.append(line_str)
    return lines_list


def find_lines(file_name, word, ignore_case=True, match_whole_word=True):
    f=open(file_name,'r')
    a = f.readlines()
    lines_list = []

    #If upper case or lower case input doesnt matter
    if ignore_case == True:
        #accepting the partial word and returning the whole word
        if match_whole_word == False:
            #parsing through the lines of file with variable line
            for line in a:
                #for making case insensitive
                if word.lower() in line.lower():
                   lines_list.append(line)
                   separated_lines = "".join(map(str,lines_list))
        #not accepting the partial word and returning only the input word            
        if match_whole_word == True:
            #parsing line by line
            for line in a:
                #splitting for not returning unmatched words
                splitted = line.split()
                #ignoring cases
                if word.lower() in splitted:
                    lines_list.append(line)
                    separated_lines = "".join(map(str,lines_list))
        if match_whole_word == False:
            if ignore_case == False:
                for line in a:
                    if word in line:
                        lines_list.append(line)
                        separated_lines = "".join(map(str,lines_list))
        if match_whole_word == True:
            for line in a:
                splitted = line.split()
                if word in splitted:
                    lines_list.append(line)
                    separated_lines = "".join(map(str,lines_list))
    return separated_lines

#if __name__ == "__main__":

 #   print (find_lines('my_file.txt', 'NoS', ignore_case=True, match_whole_word=False))
"""
    print (return_file_contents('my_file.txt', odd=False ,line_nos=True))    
    #this will be called as file name as file_name odd is none and line nos is true
    #print_file_contents('my_file.txt',False,False)
    #this will be called with odd as true
    #print_file_contents('my_file.txt', ,True)
    #print("printing this with", "('my_file.txt', line_nos=True)")
    print("printing this with", "('my_file.txt', odd=True , line_nos=False)")
    print (return_file_contents('my_file.txt', True , False))
    #print ("printing this with","finding_lines('my_file.txt', 'TiS', ignore_case=True, match_whole_word=False)")
    #print (find_lines('my_file.txt', 'TiS', ignore_case=True, match_whole_word=False))
"""
    #print ("printing this with","finding_lines('my_file.txt', 'TiS', ignore_case=False, match_whole_word=True)")
    #print (find_lines('my_file.txt', 'NoS', ignore_case=True, match_whole_word=False))