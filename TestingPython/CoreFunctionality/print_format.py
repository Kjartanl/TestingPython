
#def DoInputOutput():
print("This should be fine.")

str1 = "Number is %d"
str2 = 5
print(str1 % str2)

str3 = 45
print("Next value is %s" % str3)
    
inputStr = int(input("Number?")) # parse input from command line to int

print("Number was %d" % inputStr)

print("Numbers separated by tabs:")
print("Nrs: \t| %d\t| %d\t| %d\t|" %(str2, str3, inputStr))

print("We will now state something cool:")
string_with_format = "This should contain a {} cool thing here: {}"
input_cool_thing = input("(Quick, what do you want it to say?)")
input_coolness_level = input("(..and how cool do you want it to be?)")

print(string_with_format.format(input_coolness_level, input_cool_thing))
