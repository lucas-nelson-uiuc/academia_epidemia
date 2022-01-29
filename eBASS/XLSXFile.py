import os
from datetime import datetime

from errors import *
from FileManager import FileManager
from CheckPoints import checkprint, subcheckprint

class XLSXFile:
    def __init__(self):
        # how can I manage my files in script?
        self.file_manager = FileManager()

    def write_to_excel(self, dataframe, xlsx_file):
        # how can I write my beautiful dataframe to my xlsx file?
        try:
            if self.file_manager.connect_file_dir('xlsx'):
                
                dataframe.to_excel(
                    xlsx_file,
                    sheet_name='Expenses'
                )

                # did it work? can you show me in pretty colors?
                checkprint('XLSX Successfully Saved')
                subcheckprint(f'Date: {datetime.today().date()}')
                subcheckprint(f'Time: {datetime.today().time()}')
            else:
                raise DirectoryConnectionError
        except DirectoryConnectionError as e:
            print(f'DirectoryConnectionError: {e}')

    def confirm_chdir_xlsx(self, xlsx_file):
        # would you like to see your changes?
        checkprint('Open test_workbook.xlsx (yes or no)')
        user_input = input('\t> ')
        if user_input.lower() == 'yes':
            # is my progress reflected in my excel worksheets?
            try:
                if os.path.isdir(self.file_manager.univ_dir + self.file_manager.xlsx_dir):
                    os.chdir(self.file_manager.univ_dir + self.file_manager.xlsx_dir)
                    if os.path.isfile(xlsx_file):
                        checkprint('Redirecting to test_workboox.xlsx ...')
                        os.system('open -a \'Microsoft Excel\' test_workbook.xlsx')
                        checkprint('Redirecting to report_workbook.xlsx ...')
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

        # hype
        checkprint('Process Complete')