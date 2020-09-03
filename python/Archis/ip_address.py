def ip_address(file_name):
    f = open(file_name,'r')
    data = {}
    for line in f:
        #tokenzing all lines 
        token = line.split()
        #getting the first token i.e. ip
        ip = token[0]
        #condition whether the ip is present in the key of dictionary or not
        if ip in data:
            #if present make count increment
            count = data [ip] + 1
            data [ip] = count
            #else new element
        else:
            data [ip] = 1

    #sorting by value function
    sorted_data = sorted(data.items(), key=item_sorter, reverse=True)
    #adding sorted itms into dictionary
    for key , value in sorted_data:
        #converting list of tuples into dictionary
        data.setdefault(key)
        #formatting 
        print('{0:>16}{1:->10}'.format(key,value))
def item_sorter(item):
    #print (item)
    return item[1]

if __name__ == "__main__":
    ip_address('weblog.txt')
