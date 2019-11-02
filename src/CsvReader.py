import csv

class CsvReader:
    data = []
    def __init__(self,filepath):
        print(filepath)
        self.data = []
        with open(filepath, 'r') as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)

        pass