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
        print(selected_option)

        selected_option -= 1
            
        if selected_option <= len(run_list):
            run_list[selected_option]()
    except ValueError:
        print("Invalid option selected.")


def run_core_functionality():
    from CoreFunctionality import __run_module as corefun
    display_sub_menu(corefun.get_display_list(), corefun.get_run_list())

def main(): # Menu goes here
    list_options = [fn.accept_and_store, 
                    fn.print_string, 
                    fn.compare_numbers,
                    fn.calculator, 
                    fn.remove_letter, 
                    run_for_loops, 
                    run_basic_logic, 
                    run_generators, 
                    run_lists, 
                    run_list_comprehensions, 
                    run_dictionaries_code, 
                    run_core_functionality]


    while(True):
        print("")
        print("------------------------")
        print("SELECT OPTION:")
        print("------------------------")
        print("Code with IO")
        print("  1. Accept and store string")
        print("  2. Print string")
        print("  3. Compare numbers")
        print("  4. Calculate")
        print("  5. Remove letter")        
        print("Simpler functions:")
        print("  6. For Loops code")
        print("  7. Basic Logic")
        print("  8. Generators code")
        print("  9. Lists")
        print("  10. List comprehensions")
        print("  11. Dictionaries")
        print("------")
        print("  12: Sub-menu")
        print("'Q': QUIT")
        print("------")

        inputValue = input("Menu item?") 

        if inputValue == "q" or inputValue  =="Q":
            break

        try:
            selected_option = int(inputValue)
            print(selected_option)

            selected_option -= 1
            
            if selected_option > len(list_options):
                continue

            list_options[selected_option]()
        except ValueError:
            print("Invalid option selected.")
            continue

    return

main()