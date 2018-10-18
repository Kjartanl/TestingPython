
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


# Note: MyOtherClass inherits from MyClass
class MyOtherClass(MyClass):
    
    # Init is like the constructor; 
    # NB, Note "self"; a ref from the class, to itself. 
    def __init__(self, message, value):
        self.msg = message
        self.val = value

    def show_stuff():
        print("The message was: %s" %self.msg)
        print("Value was: %s" %self.val)


print("-----------------")
print("My other class: %s"  %MyOtherClass)
print("My other class prop: %s"  %MyOtherClass)

my_inst = MyOtherClass("I come in peace!", 17)

print("-----------------")
my_inst.show_stuff
print(my_inst.msg)
print(dir(my_inst))


