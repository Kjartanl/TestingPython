
##############
### TASK 1 ###
##############
def is_even_or_odd(nr):
    
    number = int(nr)

    if  number % 2 == 0:
        return "Even"
    else:
        return "Odd"


##############
### TASK 2 ###
##############

def sum_two_numbers(first, second):
    return int(first) + int(second)


##############
### TASK 3 ###
##############

def count_even_nrs(list):
    evenCount = 0
    for nr in list:
        if(is_even_or_odd(nr) == "Even"):
            evenCount += 1
    return evenCount




##############
### TASK 4 ###
##############

def reverse_string(str):
    #reversed = ""
    #for letter in str:
    #    reversed = letter + reversed
    #return reversed

    #NOTE: The "Pythonic" way to do it; iterate from end-to end, stepping backwards one character at a time:
    return str[::-1] 
        
###############
### TESTING ###
###############
task_to_run = int(input("Task to run (1-4)?"))
if(task_to_run == 1):
    for nr in range(9):
        print("%d is %s" %(nr,  is_even_or_odd(nr)))

elif(task_to_run == 2):
    firstNr = 23
    secondNr = 48
    print("sum of %d and %d is: %d" % (firstNr, secondNr, sum_two_numbers(firstNr, secondNr)))
    
elif(task_to_run == 3):
    # Run task 3:
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print("Nr of even nrs: %d" % count_even_nrs(my_list))
    
elif(task_to_run == 4):
    # Run task 4
    print(reverse_string("Reverse This!"))
else:
    print("Invalid task selected.")


