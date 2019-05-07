from Programs.ProgramWithMenu import functions as fn

def run_for_loops():
    from Logic import For_loops


def main(): # Menu goes here
    list_options = [fn.accept_and_store, 
                    fn.print_string, 
                    fn.compare_numbers,
                    fn.calculator, 
                    fn.remove_letter, 
                    run_for_loops]


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
        print("  6. Run For Loops code")
        print("------")
        print("7. (or 'Q') QUIT")
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

            if(selected_option is 6):
                break
            
            list_options[selected_option]()
        except ValueError:
            print("Invalid option selected.")
            continue

    return

main()