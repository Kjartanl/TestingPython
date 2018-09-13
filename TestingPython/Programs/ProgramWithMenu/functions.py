import operator

def accept_and_store(): # Accept and store a string value
    print("Accept and store String value!")
    global saved_string
    saved_string = input("Input string?")
    return

def calculator(): # Add, sub, multiply, divide
    print("Running Calculator!")
    nr1 = int(input("First Nr? "))
    nr2 = int(input("Second nr? "))
    operation = input("Operation? ")

    # Ref. to functions for maths-operations:
    signs = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.sub }

    if operation == "":
        print("Invalid or no operation char given; defaulting to '+'")
        operation = "+"

    # Call the referenced function:
    result = signs[operation](nr1,  nr2)

    print("nr %d %s %d = %d" %(nr1, operation, nr2, result))

    return


def print_string(): #print previously stored value (if any)
    if not 'saved_string' in globals():    
        print("No string was not set!")
    else:
        print("String was: %s" %saved_string)

    return


def compare_numbers(): # compare two numbers to find the highest
    print("Will now compare Numbers")
    num1 = int(input("First num?"))
    num2 = int(input("Second num?"))
    
    res = num1 if (num1 > num2) else num2 if num2 > num1 else "None of them - they are equal!"

    print("The largest number was: %s" %res)
    
    return


def remove_letter(): #remove specified letter from the list
    print("Remove letter")

    given_str = str(input("Enter a string"))
    char_to_remove = str(input("Enter a letter to remove"))

    char_to_remove = char_to_remove[0]

    print("Char to remove is %s" %char_to_remove)

    for char in given_str:
        if char is char_to_remove:
            pos = given_str.index(char)
            given_str = given_str[:pos] + given_str[pos + 1 :]
            print(given_str)
    return 












