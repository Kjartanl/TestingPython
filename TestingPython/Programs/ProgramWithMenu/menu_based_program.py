import functions as fn

def main(): # Menu goes here
    list_options = [fn.accept_and_store, 
                    fn.calculator, 
                    fn.compare_numbers,
                    fn.print_string, 
                    fn.remove_letter]


    while(True):
        print("------------------------")
        print("SELECT OPTION:")
        print("1. Accept and store string")
        print("2. Calculate")
        print("3. Compare numbers")
        print("4. Print string")
        print("5. Remove letter")
        print("6. (or 'Q') Quit")

        inputValue = input("Menu item?") 

        if inputValue == "q" or inputValue  =="Q":
            break

        try:
            selected_option = int(inputValue)
            print(selected_option)

            selected_option -= 1
            
            if selected_option > len(list_options):
                continue

            if(selected_option is 5):
                break
            
            list_options[selected_option]()
        except ValueError:
            print("Invalid option selected.")
            continue

    return

main()