

from Programs.ProgramWithMenu import functions as fn

def get_run_list():
    return [fn.accept_and_store, 
            fn.print_string, 
            fn.compare_numbers, 
            fn.calculator,
            fn.remove_letter]

def get_display_list():
    return ["1. Accept and store string",
            "2. Print string",
            "3. Compare numbers",
            "4. Calculate",
            "5. Remove letter"] 