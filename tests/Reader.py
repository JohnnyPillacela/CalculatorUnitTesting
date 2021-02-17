import csv

content = []


def reader(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_line = csv_file.readline()  # to get rid of the first line i.e val1, val2, result
        for row in csv_reader:
            if '' in row:
                row.remove('')
            content.append(row)
    return content
