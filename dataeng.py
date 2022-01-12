import os
import re
import warnings
from openpyxl import load_workbook
import pandas as pd
from datetime import datetime

from errors import EmptyDirectoryError, InvalidDirectoryError
from errors import IncorrectColumnsError, FileNotExistError
from errors import DirectoryConnectionError


class CSVFile:
    def __init__(self, file):
        self.file = file
    
    def gather_date_information(self):
        date_string = self.file[self.file.find('_') + 1 : self.file.rfind('.csv')]
        return datetime.strptime(date_string, '%Y%m%d').strftime('%B %d, %Y')
    
    def print_csv_information(self):
        return f'\t> {self.gather_date_information()}\t{self.file}\t{os.path.getsize(self.file)} bytes'

class XLSXFile:
    def __init__(self):
        self.file_manager = FileManagement()

    def write_to_excel(self, dataframe, xlsx_file):
        try:
            if self.file_manager.connect_file_dir('xlsx'):
                
                dataframe.to_excel(
                    xlsx_file,
                    sheet_name='Expenses'
                )

                print(':: XLSX Successfully Saved ::')
                print(f'\t> Date: {datetime.today().date()}')
                print(f'\t> Time: {datetime.today().time()}')
            else:
                raise DirectoryConnectionError
        except DirectoryConnectionError as e:
            print(f'DirectoryConnectionError: {e}')
    
    def confirm_chdir_xlsx(self, user_input, xlsx_file):
        if user_input.lower() == 'yes':
            try:
                if os.path.isdir(self.file_manager.univ_dir + self.file_manager.xlsx_dir):
                    os.chdir(self.file_manager.univ_dir + self.file_manager.xlsx_dir)
                    if os.path.isfile(xlsx_file):
                        print(':: Redirecting to test_workbook.xlsx ... ::')
                        os.system('open -a \'Microsoft Excel\' test_workbook.xlsx')
                        print(':: Redirecting to report_workbook.xlsx ... ::')
                        os.system('open -a \'Microsoft Excel\' report_workbook.xlsx')
                    elif len(os.listdir()) == 0:
                        raise EmptyDirectoryError
                    else:
                        raise FileNotExistError
                else:
                    raise InvalidDirectoryError
            except EmptyDirectoryError as e:
                print(f'EmptyDirectoryError: {e}')
            except InvalidDirectoryError as e:
                print(f'InvalidDirectoryError: {e}')
            except FileNotExistError as e:
                print(f'FileNotExistError: {e}')
        print(':: Process Complete ::')


class FileManagement:
    def __init__(self):
        self.univ_dir = os.path.dirname(os.getcwd())
        self.python_dir = '/py_src'
        self.csv_dir = '/csv_exports'
        self.xlsx_dir = '/xlsx_reports'

    def get_directory(self, file_type):
        return self.univ_dir + self.csv_dir if file_type == 'csv' else self.univ_dir + self.xlsx_dir
    
    def connect_file_dir(self, file_type):
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
        if self.connect_file_dir(file_type):
            return [
                file
                for file in os.listdir()
                if file.endswith(file_type)
            ]
        
class DataWarehouse:
    def __init__(self, file_type):
        self.file_type = file_type
        self.file_manager = FileManagement()
        self.directory = self.file_manager.get_directory(self.file_type)

    def match_regular_expression(self):
        try:
            assert self.file_manager.connect_file_dir(self.file_type)
            self.files = self.file_manager.gather_files(self.file_type)
            if len(self.files) == 0:
                raise EmptyDirectoryError
        except EmptyDirectoryError as e:
            print(f'EmptyDirectoryError::{e}')
        
        if self.file_type == 'csv':
            # what is common across all valid entries?
            expr = '["]*([\d]{1,2}\/[\d]{1,2}\/[\d]{2,4})["]*,([\w\d\s!@#$%^&*-.\'"]*),([\w\d\s!@#$%^&*-.\'"]*),(["\d]*),([\($"]*[\d.,]+[\)\s"]*),([$"]*[\d.,]+["]*)'
            # how do I collect all valid entries?
            matches = None
            # which entries are valid?
            print(':: Files gathered ::')
            for csv_file in self.file_manager.gather_files(self.file_type):
                csv_obj = CSVFile(csv_file)
                print(csv_obj.print_csv_information())
                with open(csv_file, 'r') as csv:
                    try:
                        if ''.join(csv.readline().split('"')) != 'Date,Description,Comments,Check Number,Amount,Balance\n':
                            raise IncorrectColumnsError
                    except IncorrectColumnsError as e:
                        print(f'IncorrectColumnsError" {e}')
                    if matches == None:
                        matches = [
                            list(re.search(expr, line).groups())
                            for line in csv.readlines()
                            if re.search(expr, line)
                        ]
                    else:
                        for line in csv.readlines():
                            if re.search(expr, line):
                                matches.append(list(re.search(expr, line).groups()))
            return matches

    def generate_dataframe(self):
        return pd.DataFrame(
                self.match_regular_expression(),
                columns=['Date', 'Description', 'Comments', 'Check Number', 'Amount', 'Balance']
            )

    def clean_dataframe(self):
        warnings.filterwarnings('ignore')
        df = self.generate_dataframe()
        df.drop(columns=['Check Number', 'Description'], inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Comments'] = df['Comments'].str.replace('"', '')
        df['Amount'] = df['Amount'].str.replace('(', '-'
                                ).str.replace('$', ''
                                ).str.replace(')', ''
                                ).str.replace('"', ''
                                ).str.replace(',', ''
                                ).str.strip().astype('float64')
        df['Balance'] = df['Balance'].str.replace('$', ''
                                ).str.replace('"', ''
                                ).str.replace(',', ''
                                ).str.strip().astype('float64')
        df = df.drop_duplicates(
            subset=['Date', 'Comments', 'Amount'],
            keep='last'
            )

        print(':: DataFrame compiled ::')
        print(f'\t|    Rows| {df.shape[0]}', end='\t')
        print(f'\t| Columns| {df.shape[1]}')
        print(f"\t|Earliest| {df['Date'][0].date()}", end='\t')
        print(f"|  Latest| {df['Date'][df.shape[0] - 1].date()}")

        return df

    def revert_univ_directory(self):
        os.chdir(self.file_manager.univ_dir)
