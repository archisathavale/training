def parse_weblog_file(filename):
    """Returns a list of tuples of the form - (ip, url, transferred_bytes) after 
    processing the file.
    """
    f=open(filename, 'r')
    log_entries = []
    for line in f:
        token = line.split()
        ip = token[0]
        url = token[6]
        contents = url.split("/")
        website = contents[0]
        bytes = token[9]
        log_entry = (ip,website,bytes)
        log_entries.append(log_entry)

    return log_entries


def compute_unique_ips(log_entries):
    """Returns a list of unique ips after processing the log_entries.
    """
    #1.Initialize empty set
    unique_ips = set()
    #2. Parse through all enries
    for entry in log_entries:
        
        #3. Add 0th element in log_entries into set unique_ips
        unique_ips.add(entry[0])
    
    #4. Return list of unique_ips 
    return list(unique_ips)


def compute_famous_urls(log_entries, howmany=5):
    """Returns 'howmany' URLs with maximum occurence 
    """ 
    # 0. Initialize empty dictionary
    urls_dict = {}
    # 1. Go through all the entries
    for entry in log_entries:
        
        # 2. Get the URL 
        url = entry[1]

        # 3. Add the url into our urls_dict along with it's count
        if url in urls_dict:
            count = urls_dict[url] + 1
            urls_dict[url] = count
        else:
            urls_dict[url] = 1

    #4. Sorting by maximum occurence of URL's
    sorted_urls = sorted(urls_dict.items(), key= lambda x: x[1], reverse=True)
    
    #5. Returning howmany urls with maximum occurence
    return sorted_urls[:howmany]


def compute_greedy_client(log_entries, top=5):
    """Returns 'top' greedy clients with total bytes received by them.  
    """
    #1. Initialize empty dictionary
    bytes_dict = {}
    #2. Parsing through log_entries and getting ip's and bytes 
    for entry in log_entries:
        ip = entry[0]
        bytes = entry[2]
        #3. Converting bytes string into integer 
        try:
            bytes = int(bytes)
        except:
            bytes = 0  
        #4. Adding bytes of similar ips and passing it to dictionary     
        if ip in bytes_dict:
            bytes += bytes_dict[ip]
            bytes_dict[ip] = bytes
        else:
            bytes_dict[ip] = bytes
                
    #5. Sorting the data by bytes received
    sorted_data = sorted(bytes_dict.items(), key = lambda x:x[1], reverse=True)

    #6. Returning top IP's with most bytes received 
    return sorted_data[:top]

if __name__ == "__main__":

    filename = "weblog.txt"
    log_entries = parse_weblog_file(filename)

    print (compute_unique_ips(log_entries))
    print (compute_famous_urls(log_entries, 15))
    print (compute_greedy_client(log_entries, 15))