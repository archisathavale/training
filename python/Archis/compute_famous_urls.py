def compute_famous_urls(file_name):
    data = {}
    f=open(file_name, 'r')
    for line in f:
        token = line.split()
        ip = token[0]
        url = token[6]
        contents = url.split("/")
        website = contents[0]
        if website in data:
            count = data[website] + 1
            data[website] = count
        else:
            data[website] = 1

    
    sorted_data = sorted(data.items(), key = lambda x:x[1], reverse = True)
    for key, value in sorted_data:
        print (key,value) 
        
if __name__ == "__main__" :
    compute_famous_urls('weblog.txt')