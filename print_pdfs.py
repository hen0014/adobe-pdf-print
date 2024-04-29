#includes
import os
import pdfprint
import argparse
import logging
import sys

logging.basicConfig(filename=f'{sys.argv[0]}.log', encoding='utf-8',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

#get user args
def get_args():
    parser = argparse.ArgumentParser(description='Print PDFs in a directory')
    #required argument directory, default pwd
    parser.add_argument('directory', help='Directory to print PDFs from, specify "pwd" or directory', default='pwd')
    #required argument printer
    parser.add_argument('printer', help='Printer to print PDFs to', default='lexy=print')
    #option flag to read options from file
    parser.add_argument('-ro', '--readOptions', help='Read options from file')
    #debug flag
    parser.add_argument('-d', '--debug', help='Debug mode', action='store_true')
    #suppress all messages to log file flag
    parser.add_argument('-s', '--silent', help='Silent mode', action='store_true')
    parser.add_argument('-o', '--options', help='Options to print PDFs', nargs='+')
    parser.add_argument('-all', '--all', help='Print all PDFs in directory', action='store_true')
    return parser.parse_args()


#read options from file where every new line is stored as a new element in a list
def read_options(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

#function to handle messages in relation to the debug and silent mode
def msg(message, debug=False, silent=False, error=False):
    if debug:
        logging.debug(message)
    if error:
        logging.error(message)
    if not silent:
        print(message)

def file_execution(pdf, args):
    #read in list from a text file
    try:
        with open(args.readOptions, 'r') as f:
            options = f.read().splitlines()
        return options
    except:
        msg(f'Error reading file {args.readOptions}', args.debug, args.silent, error=True)
        return 1

def main1():
    args = get_args()
    #check user entered any arguments
    if len(sys.argv) == 1: print('No arguments entered') ; return

    #setup debug mode
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    logging.debug(f'Arguments: {args}')
    #create a pdf_print object
    pdf = pdfprint.pdf_print(args.directory)
    #setup printer
    pdf.set_printer_info(args.printer)
    #check if the directory is valid
    if pdf.get_path() == 1: msg(f'Directory{args.directory} does not exist', args.debug, args.silent); return
    #check if the PDF app is valid
    #if pdf.check_app(): msg(f'PDF app -- {pdf.get_pdf_print_app()} -- is not valid, check your path', args.debug, args.silent); return

    #are we reading options from a file or from the command line
    if args.readOptions:
        pdf.set_selection(file_execution(pdf, args))
    else:
        pdf.set_selection(args.options)

    #if not printing all is there an error in the selection list
    #if there is a missmatch error print the missmatch, keeping to silent rules if set, but putting in log
    if not args.all:
        if pdf.print_missmatch(): msg(f'Error in file selection', args.debug, args.silent, error=True); return

    #switch case for the differnt print options
    if args.all:
        pdf.print_all_files()
    else:
        pdf.print_files(args.printer)
    #print the PDFs

#main == main
if __name__ == '__main__':
    main1()
