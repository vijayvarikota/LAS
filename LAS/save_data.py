import csv

RESOURCE_DIR = 'resources/small'

def write_csv(file_name, data):
    items = []
    path = '{}/{}'.format(RESOURCE_DIR, file_name)
    with open(path, 'wb') as file:
        file_writer = csv.writer(file, delimiter=',')
        keys = data[0].keys()
        file_writer.writerow(keys)
        for item in data:
            row = []
            for key in keys:
                row.append(item[key])
            file_writer.writerow(row)
    return items