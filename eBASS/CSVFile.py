import os
from datetime import datetime

class CSVFile:
    '''
    Class for displaying csv file related information,
    namely, the date the data was retrieved.
    '''

    def __init__(self, file):
        self.file = file
    
    def gather_date_information(self):
        # when was this file pulled/stored on my local machine?
        date_string = self.file[self.file.find('_') + 1 : self.file.rfind('.csv')]
        return datetime.strptime(date_string, '%Y%m%d').strftime('%B %d, %Y')
    
    def print_csv_information(self):
        # doesn't really print but I'm too lazy to change it
        return f'{self.gather_date_information()}\t{self.file}\t{os.path.getsize(self.file)} bytes'