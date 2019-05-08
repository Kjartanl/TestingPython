string_list = ["we", "are", "the", "knights", "who", "say", "ni"]
print("Element 3 was '%s'" %string_list[3])

# Check existance of an element in a list:
print("Is 'knights' in the list? %s" %('knights' in string_list))
string_list.remove("say")
print("Was 'say' removed? %s" %("say" not in string_list))

string_list.insert(5, "code")
print(string_list)

# Change existing elements
string_list[4] = "for whom"
string_list[6] = "is written"
print(string_list)

last_item = string_list.pop() # pop last item
item_3 = string_list.pop(2) # pop item at index 2 
print("Last item: %s" %last_item)
print("Item #3: %s" %item_3)
print("After poping: %s" %string_list)

string_list.append("is")
string_list.append("SUNG!")
print("List: %s" %string_list) # ['we', 'are', 'knights', 'for whom', 'code', 'is', 'SUNG!']

## SPLICING AND REPLACING ITEMS
string_list[3:5] = ["by", "whom", "code"] #['we', 'are', 'knights', 'by', 'whom', 'code', 'is', 'SUNG!'] 
string_list[-3:] = ["awsome", "code", "is", "regularly", "composed"]
# ['we', 'are', 'knights', 'by', 'whom', 'awsome', 'code', 'is', 'regularly', 'composed']
print("List: %s" %string_list)

# splicing from the start, until the N-last element:
string_list[:-7] = ["These", "are", "the", "hackers"]
print("List: %s" %string_list)

# Appending (1 element) and extending (1 or more elements)
string_list.append("with")
string_list.extend(["clarity", "and", "ease"])

print(string_list)

# Concatenation and repeated output 
# NOTE: All elements must be  lists (i.e. list[x:y], not list[x], which is a string)
another_list = string_list[3:4] + string_list[10:11] + string_list[6:8] + string_list[-4:]

# ['hackers', 'composed', 'awsome', 'code', 'with', 'clarity', 'and', 'ease']
print(another_list)

# ['hackers', 'hackers', 'hackers']
print(another_list[:1] * 3) 

#Stepping backwards through a list:
backwards_list = ["six", "five", "four", "three", "two", "one", "zero"]

#Step from pos 4 (after final element!) to 0, stepping -1 at at time:
print(f"Backwards: {backwards_list[4:0:-1]}")

# the step-indicator can also be used to skip elements:
print(f"Every other element: {backwards_list[0:6:2]}")

#...or to print the whole list in reverse order, if the first two parameters are not included:
print(f"The whole list backwards: {backwards_list[::-1]}")

# Same as previous, but only including every other element:
print(f"The whole list backwards: {backwards_list[::-2]}")



