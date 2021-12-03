

def string_numbers():
    from Dates import day_01_string_numbers

def main(): # Menu goes here
    list_dates = [string_numbers]

    while(True):
        print("")
        print("------------------------")
        print("SELECT DATE:")
        print("------------------------")
        print("1: String numbers")

        print("'Q': QUIT")
        print("------")

        inputValue = input("Date?") 

        if inputValue == "q" or inputValue  =="Q":
            break

        try:
            selected_date = int(inputValue)
            print("-----------------------------")
            print(f"Running code from {selected_date}")
            print("-----------------------------")

            selected_date -= 1
            
            if selected_date > len(list_dates):
                continue

            list_dates[selected_date]()
        except ValueError:
            print("Invalid date selected.")
            continue

    return

main()

