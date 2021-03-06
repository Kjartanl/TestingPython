from Programs.ProgramWithMenu import functions as fn

def run_for_loops():
    from Logic import For_loops

def run_basic_logic():
    from Logic import basic_logic

def run_generators():
    from Logic import Generators

def run_dictionaries_code():
    from DataStructures import Dictionaries

def run_list_comprehensions():
    from DataStructures import List_comprehension

def run_lists():
    from DataStructures import Lists
    

def display_sub_menu(disp_list, run_list):
    print("SUB-MENU OPTIONS:")
    print("-------------------")
    for opt in disp_list:
        print(opt)
    inputValue = input("Item to run?")

    try:
        selected_option = int(inputValue)
        selected_option -= 1

        print("-----------------------------")
        print(f"Running: {disp_list[selected_option]}")
        print("-----------------------------")

            
        if selected_option <= len(run_list):
            run_list[selected_option]()
        input("Click any key to return.") 
    except ValueError:
        print("Invalid option selected.")


def run_functions():
    from Programs.ProgramWithMenu import __run_module as functions
    display_sub_menu(functions.get_display_list(), functions.get_run_list())
    

def run_core_functionality():
    from CoreFunctionality import __run_module as corefun
    display_sub_menu(corefun.get_display_list(), corefun.get_run_list())
    
def run_data_structures():
    from DataStructures import __run_module as dstructs
    display_sub_menu(dstructs.get_display_list(), dstructs.get_run_list())

def run_logic():
    from Logic import __run_module as logic
    display_sub_menu(logic.get_display_list(), logic.get_run_list())



def main(): # Menu goes here
    list_options = [run_functions, 
                    run_core_functionality, 
                    run_data_structures, 
                    run_logic]


    while(True):
        print("")
        print("------------------------")
        print("SELECT OPTION:")
        print("------------------------")
        print("1. Functions")
        print("2: Core Functionality")
        print("3: Data Structures")
        print("4: Logic, loops, etc")

        print("'Q': QUIT")
        print("------")

        inputValue = input("Menu item?") 

        if inputValue == "q" or inputValue  =="Q":
            break

        try:
            selected_option = int(inputValue)
            print("-----------------------------")
            print(f"Running: {selected_option}")
            print("-----------------------------")

            selected_option -= 1
            
            if selected_option > len(list_options):
                continue

            list_options[selected_option]()
        except ValueError:
            print("Invalid option selected.")
            continue

    return

main()