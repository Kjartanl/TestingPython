
# Generators - the Python equivalent of the C# Yield keyword?
# Quote: "Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time)."

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



