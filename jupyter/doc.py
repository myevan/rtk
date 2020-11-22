from meta import Singleton
from scheme import Province
from scheme import Hero

import os

class DocumentManager(Singleton):
    def __init__(self):
        this_dir_path = os.path.dirname(os.path.realpath(__file__))
        self.work_dir_path = os.path.realpath(os.path.join(this_dir_path, '..'))
        self.csv_dir_path = os.path.join(self.work_dir_path, 'csvs')

    def load_table(self, cls, file_name):
        from asset_csv import CSVTable
        csv_file_path = os.path.join(self.csv_dir_path, file_name)
        csv_table = CSVTable.load_file(open(csv_file_path))

        from data import String
        sch_types = cls.get_field_name_types()
        csv_types = [sch_types.get(n, String()) for n in csv_table.heads]

        mem_table = csv_table.convert(csv_types)
        for row in mem_table.rows:
            kwargs = dict(zip(csv_table.heads, row))
            cls.put(cls(**kwargs))

if __name__ == '__main__':
    doc_mgr = DocumentManager.get()
    doc_mgr.load_table(Hero, '1_generals.csv')
    doc_mgr.load_table(Province, '1_provinces.csv')

    from scheme import Province
    #print(Province.get(9).head)
    print(Province.get(9).body)
