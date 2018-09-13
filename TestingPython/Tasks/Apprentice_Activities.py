
def is_even_or_odd(nr):
    
    number = int(nr)

    if  number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def sum_two_numbers(first, second):
    return int(first) + int(second)

for nr in range(9):
    print("%d is %s" %(nr,  is_even_or_odd(nr)))

firstNr = 23
secondNr = 48
print("sum of %d and %d is: %d" % (firstNr, secondNr, sum_two_numbers(firstNr, secondNr)))

def count_even_nrs(list):

    evenCount = 0
    for nr in list:
        if(is_even_or_odd(nr) == "Even"):
            evenCount += 1
    return evenCount

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Nr of even nrs: %d" % count_even_nrs(my_list))

def reverse_string(str):
    #reversed = ""
    #for letter in str:
    #    reversed = letter + reversed
    #return reversed

    #NOTE: The "Pythonic" way to do it; iterate from end-to end, stepping backwards one character at a time:
    return str[::-1] 
        
print(reverse_string("Reverse This!"))