from typing import List
from tabulate import tabulate

class Table:
    def __init__(self, row_labels: List, col_labels: List):
        self.table = [col_labels]
        
        for row_label in row_labels:
            row = [row_label]
            
            row += ['-' for _ in range(len(col_labels) - 1)]
            
            self.table.append(row)
            
    def __repr__(self):
        return tabulate(self.table, tablefmt="grid")
    
    def file_export(self):
        with open("table.txt", 'w') as file:
            file.write(self.__repr__())
    
        
            