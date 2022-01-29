import os
from errors import *

class FileManager:
    def __init__(self):
        self.univ_dir = os.path.dirname(os.getcwd())
        self.csv_dir = '/csv_exports'
        self.xlsx_dir = '/xlsx_reports'

    def get_directory(self, file_type):
        # what is the path to my desired directory?
        return self.univ_dir + self.csv_dir if file_type == 'csv' else self.univ_dir + self.xlsx_dir
    
    def connect_file_dir(self, file_type):
        # does my csv/xlsx directory exist?
        try:
            if os.path.isdir(self.get_directory(file_type)):
                os.chdir(self.get_directory(file_type))
                return True
            else:
                raise InvalidDirectoryError
        except InvalidDirectoryError as e:
            print(f'InvalidDirectoryError: {e}')
            return False
    
    def gather_files(self, file_type):
        # what files, if any, exist in csv/xlsx directory?
        if self.connect_file_dir(file_type):
            return [
                file
                for file in os.listdir()
                if file.endswith(file_type)
            ]