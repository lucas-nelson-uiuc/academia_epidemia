import os
import re
import warnings
import pandas as pd

from errors import *
from FileManager import FileManager
from CSVFile import CSVFile
from CheckPoints import checkprint, subcheckprint, tableprint

class DataWarehouse:
    def __init__(self, file_type):
        # what information do I need to work with my data?
        self.file_type = file_type
        self.file_manager = FileManager()
        self.directory = self.file_manager.get_directory(self.file_type)

    def match_regular_expression(self):
        # which files exists in my directory?
        try:
            assert self.file_manager.connect_file_dir(self.file_type)
            self.files = self.file_manager.gather_files(self.file_type)
            if len(self.files) == 0:
                raise EmptyDirectoryError
        except EmptyDirectoryError as e:
            print(f'EmptyDirectoryError::{e}')
        
        if self.file_type == 'csv':
            # how can I get data across as many observations as possible?
            expr = '["]*([\d]{1,2}\/[\d]{1,2}\/[\d]{2,4})["]*,([\w\d\s!@#$%^&*-.\'"]*),([\w\d\s!@#$%^&*-.\'"]*),(["\d]*),([\($"]*[\d.,]+[\)\s"]*),([$"]*[\d.,]+["]*)'
            # how do I collect all valid entries?
            matches = None
            # which files are valid?
            checkprint('Files gathered', 'bold green')
            
            for csv_file in self.file_manager.gather_files(self.file_type):
                csv_obj = CSVFile(csv_file)
                subcheckprint(
                    csv_obj.print_csv_information(),
                    'bold magenta'
                )
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
            
            # the good batch
            return matches

    def generate_dataframe(self):
        # the good batch ... this time in pd.DataFrame form
        return pd.DataFrame(
                self.match_regular_expression(),
                columns=['Date', 'Description', 'Comments', 'Check Number', 'Amount', 'Balance']
            )

    def clean_dataframe(self):
        # please stop telling me what I don't want to hear
        warnings.filterwarnings('ignore')

        # okay how can I make this good batch a great batch?
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
        
        # don't think I don't see you...
        df = df.drop_duplicates(
            subset=['Date', 'Comments', 'Amount'],
            keep='last'
            )

        # did it work? can i pretty please see if it worked?
        checkprint('DataFrame compiled')
        tableprint(df)
        
        return df

    def revert_univ_directory(self):
        # easter egg: college dorm room listening to EITS
        os.chdir(self.file_manager.univ_dir)