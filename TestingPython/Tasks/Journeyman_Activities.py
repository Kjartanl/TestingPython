
import socket

##############
### TASK 1 ###
##############

# Take in a list of strings, and a separate int. The int indicates which item in the list
# should be interpreted as the name of a file to write. All the rest of the elements
# in the list should be written to that file. 

def create_file(str_list, filename_indicator):
    filename = str(str_list[filename_indicator])
    file_handle = open(filename, "w+")
    del str_list[filename_indicator]
    for word in str_list:  
        file_handle.write(word + "\n")


     
##############
### TASK 2 ###
##############

# Write a function that takes an int as a parameter, 
# and returns the sum of that integer and all positive 
# integers smaller than it. 
# NB: USE A GENERATOR!

def get_next_sum(target):
    nr = 0
    sum = 0
    while nr < target:
       sum = (sum + nr)
       print("(Yielding sum up to: %s. Sum so far: %s)"  % (target, sum))
       yield sum
       nr += 1
    sum += nr
    print("(Final yield for numbers <= %s. Final sum: %s)"  % (target, sum))
    yield sum 

pint = get_next_sum(5)
print(pint)
    

### Alternative implementation:
def get_sum_up_to(target):
    print("Sum up to %s: %s" %(target, sum(get_numbers_up_to(target))))

def get_numbers_up_to(target):
    nr = 0
    while nr < target:
        yield nr
        nr += 1


##############
### TASK 3 ###
##############

# Create a client that connects to a running instance of the 
# simple StringServer (found under "Networking").

def query_server(): 
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn_data = ('127.0.0.1', 50002)    
    clientSock.connect(conn_data)

    received_string = clientSock.recv(1024)
    
    print("Output: %s" %received_string)

    msg = input("Message?") 
    while msg != '':
        clientSock.send(msg.encode('utf8'))
        msg = input("Next message?")

    clientSock.close()


     
##############
### TASK 4 ###
##############
def person_populator():
    class Person:
        def __init__(self = 0, height = 0, weight = 0, hair = '', eyes = ''):
            self.height = height
            self.weight = weight
            self.hair = hair
            self.eyes = eyes

        def print_self(self):
            print("Height: %d\nWeight: \t%d\nHair: \t%s \nEyes: \t%s" % (self.height, self.weight, self.hair, self.eyes))

    pers1 = Person(172, 65, 'brown', 'blue')

    pers1.print_self()

    return


###############
### TESTING ###
###############
task_to_run = int(input("Task to run (1-4)?"))
if(task_to_run == 1):
    # A couple of test-runs:
    create_file(["filename_0.txt", "second", "middle", "third"], 0)
    create_file(["one", "two", "three", "Filename_1.txt", "four"], 3)
    create_file(["first", "second", "third", "Filename_2.txt"], 3)

elif(task_to_run == 2):

    alt_nr = int(input("Implementation 1 or 2?"))
    if(alt_nr == 1):
        zero_sum_list = get_next_sum(0)
        #print(zero_sum_list)
        for element in zero_sum_list:
            print("Result: %s" % element)    
        
        single_item_list = get_next_sum(1) 
        for element in zero_sum_list:
            print("Result: %s" % element)
        
        three_list = get_next_sum(3)
        for element in three_list:
            print("Result: %s" % element)
    elif(alt_nr == 2):
       get_sum_up_to(0) 
       get_sum_up_to(1) 
       get_sum_up_to(3) 
       get_sum_up_to(5) 
    
elif(task_to_run == 3):
    query_server()

elif(task_to_run == 4):
    person_populator()
else:
    print("Invalid task selected.")

