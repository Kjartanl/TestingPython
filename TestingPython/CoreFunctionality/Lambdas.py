
#Basic lambdas: Anonymous functions:
square = lambda x: x**2
cube = lambda x: square(x)*x
octahedron = lambda x: cube(x) * x 

print("Squared 2: %s" %square(2))
print("Squared 3: %s" %square(3))

print("Cubed 2: %s" %cube(2))
print("Cubed 3: %s" %cube(3))

print("Octagonized 2: %s" %octahedron(2))
print("Octagonized 3: %s" %octahedron(3))

# Returning lambdas (a "lambda engine?" ^^) from functions:
def lambdaengine(nr):
    return lambda x: x**nr
        
squarer = lambdaengine(2)
cuber = lambdaengine(3)
octo = lambdaengine(4)

print("Squarer 4: %s" %squarer(4))
print("Cuber 5: %s" %cuber(5))
print("octo 10: %s" %octo(10))



