def compute_greedy_client(filename):
    f=open(filename,'r')
    data = {}
    ip_list = []
    byte_list = []
    new_list = []
    for line in f:
        token = line.split()
        ip = token[0]
        inte = token[9]
        ip_list.append(ip)
        byte_list.append(inte)
        for x in range(len(byte_list)):
            try:
                byte_list[x] = int(byte_list[x])
            except:
                byte_list[x] = 0    

    for p in range(len(ip_list)):
        for q in range(p+1,len(ip_list)):
            if ip_list[p] != ip_list[q]:
                data[ip_list[p]] = byte_list[p]
            else:
                data[ip_list[p]] = byte_list[p] + byte_list[q]    

    if '69.64.69.150' in data:
        print ('*')
    sorted_data = sorted(data.items(), key = sort_by_byte, reverse=True)

    print ('Greedy client first')
    for key, value in sorted_data:
        print('{0:>16}{1:->10}'.format(key,value))


def sort_by_byte(byte):
    return byte[1]

if __name__ == "__main__":
    compute_greedy_client('weblog.txt')
