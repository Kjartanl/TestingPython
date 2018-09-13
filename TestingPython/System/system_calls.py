
import os

input("Hit ender to clear screen!")
cmdResult = os.system("cls") #Call cls on system command-line

if(cmdResult == 0):
    print('Success! (return value was "0"')
else:
    print('Attempted command failed!')

input("Hit ender to clear screen again, and then enter an invalid command:")
cmdResult = os.system("cls") 
cmdResult = os.system('InvalidCommand')
if(cmdResult == 0):
    print('Success! (return value was %s' % cmdResult)
else:
    print('Attempted command failed! Return value was %s' % cmdResult)