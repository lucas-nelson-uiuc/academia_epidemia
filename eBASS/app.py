from DataWarehouse import DataWarehouse
from XLSXFile import XLSXFile

def main():
    d = DataWarehouse('csv')
    x = XLSXFile()
    x.write_to_excel(d.clean_dataframe(), 'test_workbook.xlsx')
    x.confirm_chdir_xlsx('test_workbook.xlsx')


if __name__ == '__main__':
    main()