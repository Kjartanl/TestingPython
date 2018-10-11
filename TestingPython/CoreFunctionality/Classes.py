
# Defining a basic class which inherits from 
# the "root" class type, object:

class MyClass(object):
    # variables within a class are called "attributes":
    my_attribute = "some content"

print("attrib: %s" %MyClass.my_attribute)
print("...and the content (dictionary) of the class: \n%s" %MyClass.__dict__)

# Attributes can be added "on the fly", but please don't do 
# this without a very good reason:
MyClass.FakeAttrib = "That which should not be!"
print("On-th-fly-attribute: %s" %MyClass.FakeAttrib)


class my_other_class(object):
    
    # Init is like the constructor; 
    # NB, Note "self"; a ref from the class, to itself. 
    def __init__(self, message, value):
        self.msg = message
        self.val = value
        print("The message was: %s" %self.msg)
        print("Value was: %s" %self.val)

print("My other class: %s"  %my_other_class)
print("My other class prop: %s"  %my_other_class)

my_inst = my_other_class("I come in peace!", 17)