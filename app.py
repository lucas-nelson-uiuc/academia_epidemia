import pandas as pd
from dataeng import DataWarehouse, FileManagement, XLSXFile

def main():
    d = DataWarehouse('csv')
    x = XLSXFile()
    x.write_to_excel(d.clean_dataframe(), 'test_workbook.xlsx')
    x.confirm_chdir_xlsx(input('  ?? Open test_workbook.xlsx ?? (yes or no)\n\t> '), 'test_workbook.xlsx')


if __name__ == '__main__':
    main()