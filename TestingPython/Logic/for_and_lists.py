
list_of_stuff = ["These", "are", "almost", "random", "words"]

print("The list: \n%s" % list_of_stuff)

print("Printed directly in a for loop:")
for word in list_of_stuff:
    print(word)

print("\nPrinted in a for loop with the end changed from new-line to a blank:")

for word in list_of_stuff:
    print(word, end='')

print("\n The equivalent, but using tabs instead of newlines or blank:")

for word in list_of_stuff:
    print(word, end='\t')


