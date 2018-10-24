
# Generators - the Python equivalent of the C# Yield keyword?
# Quote: "Simply speaking, a generator is a function that returns an object (iterator) 
# which we can iterate over (one value at a time)."
# (In short: Yield temporarily cedes flow to caller; will continue 
# from after that same yield statement next time the generator is called). 

# Simplest possible generator:
def generate_numbers():
    yield "one"
    yield "two"
    yield "three"

# Calling a generator directly:
result = generate_numbers() 
print("value: %s" %next(result))
print("value: %s" %next(result))
print("value: %s" %next(result))

# Calling a generator as a for-loop or list comprehension:
result_list = [str("Item " + nr) for nr in generate_numbers()]
print("res: %s" %result_list)

# This funcion will yield return-values on the last line:
def rev_str(my_str):
    length = len(my_str)
    #Note the Range() function to get indexes in reverse order:
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output: o l l e h
for char in rev_str("hello"):
     print(char)


# Eternal loop generating and outputting ever greater odd
# numbers, starting with the input number:
def get_next_odd(start_nr):
    while True:
        if (start_nr % 2 != 0):
            yield start_nr
        start_nr += 1 # After first Yield, each subsequent call will start it's flow from here. 

for nr in get_next_odd(5):
    print("Next odd nr: %s" %nr)
    if(nr > 10):
        break
        

### GENERATOR EXPRESSIONS
# Same as lambda function creates an anonymous function, generator expression creates an anonymous generator function.

# Initialize a list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
first_list = [x**2 for x in my_list]

print("The list fetched directly: %s" %first_list)

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
last_list = (x**2 for x in my_list)
print("The generator on the other hand, is an object: %s" %last_list)
print("Items: %s %s %s %s" %(next(last_list),next(last_list),next(last_list),next(last_list)))



