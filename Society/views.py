from hashlib import new
from operator import index
import sys
import csv

def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)
# add(['girl', 'F', 'B-02', '321', '123@com'])

def view():
    data = []
    with open('data.csv') as file:
        read = csv.reader(file)
        for row in read:
            data.append(row)
    print(data)
    return data
#view()


def remove(i):

    def save(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
    new_list = []
    MID = i


    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element == MID:
                    new_list.remove(row)
    save(new_list)
#remove('B-02')

def update(i):

    def update_newlist(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    MID = i[0]
    # ['B-04', 'Boy', 'F', 'B-04', '421', '143@com']

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == MID:
                    MID = i[0]
                    name = i[1]
                    gender = i[2]
                    flatno = i[3]
                    telephone = i[4]
                    email = i[-1]

                    data = [MID, name, gender, flatno, telephone, email]
                    index = new_list.index(row)
                    new_list[index] = data

    update_newlist(new_list)

# sample = ['B-04', 'coder', 'F', 'B-04', '123', 'coder@gmail.com']
# update(sample)

def search(i):
    data = []
    MID = i

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if(element == MID):
                    data.append(row)
    print(data)
    return data

