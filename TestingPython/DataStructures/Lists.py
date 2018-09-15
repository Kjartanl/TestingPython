

string_list = ["we", "are", "the", "knights", "who", "say", "ni"]

# Print whole list
print(string_list)

#Print element
print("Element 3 was '%s'" %string_list[3])

#remove element, and replace it with another:
string_list.remove("say")
string_list.insert(5, "code")

print(string_list)

# Change existing elements
string_list[4] = "for whom"
string_list[6] = "is written"
print(string_list)

last_item = string_list.pop() # pop last item
item_3 = string_list.pop(2) # pop item at index 2 

print("Last item was %s" %last_item)
print("Item #3 was %s" %item_3)

print("After poping those, the list looks like this: %s" %string_list)

# append
string_list.append("is")
string_list.append("SUNG!")
print("Final list: %s" %string_list)
