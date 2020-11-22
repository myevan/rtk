from data import Table

import csv

class CSVTable(Table):
    @classmethod
    def load_file(cls, csv_file):
        csv_reader = csv.reader(csv_file)
        head = next(csv_reader)
        body = [row for row in csv_reader]
        return CSVTable(head, body)

