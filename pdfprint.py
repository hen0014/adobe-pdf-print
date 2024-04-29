
#from os import path and exec command line
from os import path, system, listdir
import logging
import sys

logging.basicConfig(filename=f'pdf_print_class.log', encoding='utf-8',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
#log level debug
logging.getLogger().setLevel(logging.DEBUG)

#class that retrieves paths for a directory or present working directory depending on the input at initialisation
class pdf_print:
    def __init__(self, dir):
        self.__dir = dir  # This is now a "private" variable
        self.__selection = []
        self.__printer_info = ""
        self.__pdf_print_app = "Acrobat.exe"

    def get_path(self):
        try:
            if self.__dir == 'pwd':
                logging.debug(f'Present working directory: {path.abspath(path.curdir)}')
                return path.abspath(path.curdir)
            else:
                logging.debug('User defined directory')
                return path.abspath(self.__dir)       
        except:
            return 1

    def get_files(self):
        try:
            #debug message
            logging.debug(f'Reading directory {self.get_path()}')
            logging.debug(f'Files in directory: {listdir(self.get_path())}')
            fileList = listdir(self.get_path())
            #list only files with .pdf extension
            pdf_files = [file for file in fileList if file.endswith('.pdf')]
            #debug message
            logging.debug(f'PDF files in directory: {pdf_files}')
            return pdf_files
        except:
            #log error
            logging.error(f'Error reading directory {self.__dir}')
            return 1
    
    #are all files in selection list in the directory
    def check_files(self):
        #if file is not in directory append to list else return true
        missmatch = []
        for file in self.__selection:
            if file not in self.get_files():
                missmatch.append(file)
        return missmatch
      
    #print missmatch between selection list and directory files
    def print_missmatch(self):
        if len(self.check_files()) < 1: return
        print('The following files are not in the directory:')
        for i, file in enumerate(self.check_files(), start=1):
            print(f'{i}. {file}')

    #function that returns the printer information
    def get_printer_info(self):
        return self.__printer_info
    
    #function that returns the selection list
    def get_selection(self):
        return self.__selection
    
    #function that appends selection list
    def append_selection(self, selection):
        self.__selection.append(selection)
    
    #function that removes last element from selection list
    def remove_selection(self):
        self.__selection.pop()
    
    #function that clears selection list
    def clear_selection(self):
        self.__selection.clear()

    def set_selection(self, selection):
        self.__selection = selection

    #set the printer information
    def set_printer_info(self, printer_info):
        self.__printer_info = printer_info
    
    #check adobe reader is executable without defining the path
    def check_app(self):
        try:
            system(self.__pdf_print_app)
        except:
            raise RuntimeError('{} is not executable'.format(self.__pdf_print_app))
    
    #print the selected files that are in the selection list and in the directory
    def print_files(self):
        for file in self.__selection:
            #print the command line to the console
            self.print(file)
    
    def print(self, file):
        #prints files handed to function
        command = '{} /t {}'.format(self.__pdf_print_app, file)
        logging.debug(f'Command: {command}')
        system(command)

    #print all files in the directory
    def print_all_files(self):
        for file in self.get_files():
            self.print(file)


    #get pdf_print_app info
    def get_pdf_print_app(self):
        return self.__pdf_print_app
    
    