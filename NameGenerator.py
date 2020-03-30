import csv
import random

def name_generator(type):
    if type == 0:
        filename = 'FirstNames.csv'
        endrange = 3474
    elif type == 1:
        filename = 'LastNames.csv'
        endrange = 3790
    with open(filename, mode='r') as namefile:
        name_list = []
        readnames = csv.reader(namefile, delimiter=',')
        for row in readnames:
            name_list.append(row)
        id = random.randrange(1, endrange)
    return name_list[id][0]