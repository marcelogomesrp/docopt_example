import sys, os
from docopt import docopt

from services import NumService, output_services 
from services.input_services import StdioInputService, FileInputService, TuiInputService
from services.output_services import StdioOutputService, FileOutputService, TuiOutputService


def read_args(args ) :
    input_file = args['--input_file']
    output_file = args['--output_file']
    tui = args['--tui']
    return (input_file, output_file, tui)

def get_input_service(input_file, tui):
    if tui:
        input_service = TuiInputService()
    else:
        if input_file:
            input_service = FileInputService(input_file)
        else:
            input_service = StdioInputService()
    return input_service

def get_output_service(output_file, tui):
    if tui:
        output_service = TuiOutputService()
    else:     
        if output_file:
            output_service = FileOutputService(output_file)
        else:
            output_service = StdioOutputService()  
    return output_service
