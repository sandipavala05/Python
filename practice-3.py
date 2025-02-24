# Variable 
a = 4
A = "one"
b = 'one'
print(a)
print(A)
print(b)
print(type(b))

x = str(1)
y = float(1)
z = int(1)

print(x)
print(y)
print(z)

# Variable Names

myVariableName = "John"
print(myVariableName)

MyVariableName = "John-1"
print(MyVariableName)

My_VariableName = "John-2"
print(My_VariableName)

my_VariableName = "John-3"
print(my_VariableName)

# Assign Multiple Values
x, y, z = "a", "b", "c"
print(x)
print(y)
print(z)

x = y = z = "abc"
print(x)
print(y)
print(z)

fruit = ["apple", "mango", "banana"]
x, y, z = fruit
print(x)
print(y)
print(z)


# Output Variables
x = 'python'
y = 'is'
z = 'awesome'
print(x, y, z)

x = "python "
y = "is "
z = "awesome"
print(x + y + z)


x = 4
y = 6
print(x + y)
print(x, y)


x = 5
y = "John"
print(x, y)

# Global Variables
x = "awesome"
def myfun():
    print(x)
myfun()
    
y = "added"
def fun():
    print("new file " + y)
fun()

x = "new"
def myfun():
    x = "old"
    print(x)
myfun()
print(x)

def myfun():
    global x
    x = "global keyword"
myfun()
print(x)

x = "awesome"

def myfun():
    global x
    x = "fantastic"

myfun()

print("Python is " + x)


