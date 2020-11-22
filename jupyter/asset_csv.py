from data import Table

import csv

class CSVTable(Table):
    @classmethod
    def load_file(cls, csv_file):
        csv_reader = csv.reader(csv_file)
        heads = next(csv_reader)
        rows = [row for row in csv_reader]
        return CSVTable(heads, rows)

    def convert(self, types):
        new_rows = [[t.convert(v) for t, v in zip(types, row)] for row in self.rows]
        return Table(self.heads, new_rows, types)

