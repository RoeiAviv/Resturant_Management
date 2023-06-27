import csv
from objects.Table import Table

"The TableData class provides functionality to save and load table data using CSV files." 
"It uses the csv module and interacts with the Table class to handle the table information." 
"The department ensures proper file handling by using the with statement."

class TableData:
    def __init__(self, file_table):
        self.file_table = file_table

    def save_info(self, tables):
        with open(self.file_table, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['table_number', 'is_available'])
            for table in tables:
                writer.writerow([table.table_number, table.is_available])

    def load_info(self):
        tables = []
        with open(self.file_table, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 2:  # Check if row has enough elements
                    table = Table(row[0], bool(row[1]))
                    tables.append(table)
        return tables


