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

    signs = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.sub }

    #result = nr1 + nr2
    #if operation == "-":
    #    result = nr1 - nr2
    #elif operation == "*":
    #    result = nr1 * nr2
    #elif operation == "/":
    #    result = nr1 / nr2
    #else:
    #    print("Invalid or no operation char given; defaulting to '+'")
    #    operation = "+"

    if operation == "":
        print("Invalid or no operation char given; defaulting to '+'")
        operation = "+"

    result = signs[operation](nr1,  nr2)

    print("nr %d %s %d = %d" %(nr1, operation, nr2, result))

    return

def print_string(): #print previously stored value
    if not 'saved_string' in globals():    
        print("No string was not set!")
    else:
        print("String was: %s" %saved_string)

    return

def compare_numbers(): # compare two numbers to find the highest
    print("Compare Numbers")
    return

def remove_letter(): #remove specified letter from the list
    print("Remove letter")
    return 