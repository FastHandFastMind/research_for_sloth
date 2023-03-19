url_list = []

def read():
    with open('data/link.txt', 'r') as file:
        for line in file:
            url_list.append(line.strip())
    return url_list
