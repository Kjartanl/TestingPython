
def run_classes():
    from CoreFunctionality import Classes
    
def run_command_line_args():
    from CoreFunctionality import Command_line_args
    
def run_Exceptions():
    from CoreFunctionality import Exceptions
    
def run_FileIo():
    from CoreFunctionality import FileIo
    
def run_Lambdas():
    from CoreFunctionality import Lambdas
    
def run_Print_format():
    from CoreFunctionality import print_format

def get_run_list():
    return [run_classes, 
            run_command_line_args, 
            run_Exceptions, 
            run_FileIo, 
            run_Lambdas, 
            run_Print_format]

def get_display_list():
    return ["  1. Classes", 
            "  2. Command line args", 
            "  3. Exceptions", 
            "  4. File IO", 
            "  5. Lambdas", 
            "  6. Print formatting"]