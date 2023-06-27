import unittest
import os
from objects.Table import Table
from data.TableData import TableData

class TestTableData(unittest.TestCase):

    def setUp(self):
        self.file_path = 'table.csv'  # Absolute file path
        tables = [Table('1', 4, True), Table('2', 6, False), Table('3', 2, True)]
        table_data = TableData('table.csv')
        table_data.save_info(tables)
        self.table_data.save_info(tables)


    def tearDown(self):
        # Clean up the test file
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_info_load_info(self):
        # Save tables to file
        self.table_data.save_info(self.tables)

        # Load tables from file
        loaded_tables = self.table_data.load_info()

        # Check if loaded tables match the original tables
        self.assertEqual(len(loaded_tables), len(self.tables))
        for i in range(len(self.tables)):
            self.assertEqual(loaded_tables[i].table_number, self.tables[i].table_number)
            self.assertEqual(loaded_tables[i].capacity, self.tables[i].capacity)
            self.assertEqual(loaded_tables[i].is_available, self.tables[i].is_available)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)