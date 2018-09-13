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
        print("3. Print string")
        print("4. Compare numbers")
        print("5. Remove letter")
        print("6. Quit")

        inputValue = input("Menu item?") 

        if inputValue == "q" or inputValue  =="Q":
            break

        selected_option = int(inputValue)
        print(selected_option)

        if(selected_option is 6):
            break
            
        selected_option -= 1
        list_options[selected_option]()
    return

main()