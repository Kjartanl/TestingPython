
import sys

# Note: First argument (index 0) is always the name of 
# the running application.
for arg in sys.argv:
    print("Argument was: %s" %arg)

my_first_arg = sys.argv[1]
my_second_arg = sys.argv[2]
# ...etc...