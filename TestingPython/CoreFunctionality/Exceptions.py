
# Basic handling:

try:
    invalid = 1/0
    print("This will not be output, since it is after the invalid line.")
except(ZeroDivisionError):
    print("Error caught!")
finally:
    print("This part will be printed no matter what!")


class CustomException(Exception):

    # NOTE: "Self" will not be an externally provided parameter, 
    # but rather a ref. to the object itself:
    def __init__(self, error):
        # Note: In versions of Python < 3, we'd have to pass "Exception" 
        # to __super__:
        #super(Exception, self).__init__(error)
        super(CustomException) # No "self"-parameters needed from Python 3 and onward. 

        self.errormessage = error
    
    def __str__(self):
        return "Error: %s" %self.errormessage

raise CustomException("EROOOOOOOOR!")