
# Basic handling:

try:
    invalid = 1/0
    print("This will not be output, since it is after the invalid line.")
except(ZeroDivisionError):
    print("Error caught!")
finally:
    print("This part will be printed no matter what!")
