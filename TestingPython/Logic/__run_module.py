

def run_basic_logic():
    from Logic import basic_logic

    
def run_for_loops():
    from Logic import For_loops

    
def run_generators():
    from Logic import Generators

def get_run_list():
    return [run_basic_logic, 
            run_for_loops, 
            run_generators]

def get_display_list():
    return ["  1. Basic logic", 
            "  2. for-loops", 
            "  3. Generators"] 