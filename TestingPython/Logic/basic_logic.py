
stmt = True
contradiction = False

if(stmt):
    print("Indeed!")

if(contradiction):
    print("Still true, but shouldn't be! Wtf?")
else:
    print("I'm afraid I'm obliged to protest!")

print("------- WHILE LOOP ---------")
number = 0
while(number < 5):
    print("Nr is %s" %number)
    number = number+1

print("Finally, number is %s" % number)