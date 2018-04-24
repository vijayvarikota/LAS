import csv
from models import *

RESOURCE_DIR = 'resources/small'

def load_csv(file_name):
    items = []
    path = '{}/{}'.format(RESOURCE_DIR, file_name)
    with open(path, 'rb') as file:
        file_reader = csv.reader(file, delimiter=',')
        header = file_reader.next()
        for row in file_reader:
            data = {}
            for index, column in enumerate(header):
                data[column] = row[index]
            items.append(data)
    return items

def load_banks():
    banks = []
    data = load_csv('banks.csv')
    for item in data:
        banks.append(Bank(item))
    return banks

def load_covenants():
    covenants = []
    data = load_csv('covenants.csv')
    for item in data:
        covenants.append(Covenant(item))
    return covenants

def load_facilities():
    facilities = []
    data = load_csv('facilities.csv')
    for item in data:
        facilities.append(Facility(item))
    return facilities

def load_loans():
    loans = []
    data = load_csv('loans.csv')
    for item in data:
        loans.append(Loan(item))
    return loans