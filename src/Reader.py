import csv


class Reader:
    content = []

    def __init__(self, file):
        self.content = []
        self.reader(file)

    def reader(self, path):
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_line = csv_file.readline()  # to get rid of the first line i.e val1, val2, result
            for row in csv_reader:
                if '' in row:
                    row.remove('')
                self.content.append(row)
        #csv_file.close()
        #return self.content
