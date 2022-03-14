import csv

def write_to_txt(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for value in data:
            file.writelines(f'{value}\n')


def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return dict(csv.reader(file))