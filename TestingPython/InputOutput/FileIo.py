
## Files / IO:
# - Maps more or less directly to C commands for IO-tasks. 
# - The main function we'll use here is Python`s Open()
#   - This maps to "fopen()" in Linux, and WinAPI`s CreateFile under Windows.
#   - Open() abstracts and simplifies a lot of operations here.

# Open file for write only-mode
my_file_object = open("MyTestFile.txt", "w")

# Write to the feil - NOTE: After this, the pointer will be at the EOF, 
# so any attempt at reading it would fail, since it would be after the content:
my_file_object.writelines("Always look on the bright side of death!")

my_file_object.close()

# Open the same file again as a different object - pointer will be at start now, 
# so we can read it
my_edited = open("MyTestFile.txt", "r")

result = my_edited.read()

print("Content was: %s" %result)

# Open in APPEND-mode+ (append + read)
updated_file = open("MyTestFile.txt", "a+")
updated_file.write("\nAdded content...")

# ..see? No content! After EOF again!
updated_output = updated_file.read()
print("End: %s" %updated_output)

final_file = open("MyTestFile.txt", "r")
final_output = final_file.read()
print("Final otput: %s" %final_output)

# Close - Note that Python will do this automatically at the end, 
# but it is still good practice to call it:
final_file.close()
