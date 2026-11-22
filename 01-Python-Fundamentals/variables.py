#num variables
x="3"
y="5"
print(x)
print(y)

#priting the same value
x="6"
x="Sally"
print(x)

#casting
x=str(3)
y=str(5)
z=float(5)

print(x)
print(y)
print(z)

x="5"
y="John"
print(type(x))
print(type(y))

#Assigning multiple values
fruits = ["apple", "banana","orange"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global variable
x="awesome"
def myfunc():
    print("Python is "+ x)
myfunc()

x = 'Welcome'
print(x[3])

txt = "You are a python developer"
if "python" in txt:
    print("Yes, you are a python developer")