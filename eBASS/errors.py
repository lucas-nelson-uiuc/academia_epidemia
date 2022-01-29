class EmptyDirectoryError(Exception):
    '''Directory is empty and has length zero'''

class DirectoryConnectionError(Exception):
    '''Cannot complete connection to attempted directory'''

class InvalidDirectoryError(Exception):
    '''Directory does not exist'''

class IncorrectColumnsError(Exception):
    '''Columns do not align with previous exports'''

class FileNotExistError(Exception):
    '''Directory does not contain file of interest'''