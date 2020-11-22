from meta import Singleton

import os

class DocumentManager(Singleton):
    def __init__(self):
        this_dir_path = os.path.dirname(os.path.realpath(__file__))
        self.work_dir_path = os.path.realpath(os.path.join(this_dir_path, '..'))
        self.csv_dir_path = os.path.join(self.work_dir_path, 'csvs')

    def load_provinces(self, file_name):
        from asset_csv import CSVTable
        csv_file_path = os.path.join(self.csv_dir_path, file_name)
        csv_table = CSVTable.load_file(open(csv_file_path))

        from scheme import Province
        from data import String
        sch_types = dict(zip(Province.get_field_names(), Province.get_field_types()))
        csv_types = [sch_types.get(n, String()) for n in csv_table.field_names]

        for record in csv_table.records:
            values = [t.convert(v) for t, v in zip(csv_types, record)]
            kwargs = dict(zip(csv_table.field_names, values))
            Province.put(Province(**kwargs))

if __name__ == '__main__':
    DocumentManager.get().load_provinces('1_provinces.csv')

    from scheme import Province
    #print(Province.get(9).head)
    print(Province.get(9).body)
