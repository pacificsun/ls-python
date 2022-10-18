
x = "awesome"

def myfunc():
    x = "fantastic"
    print("In Python is "+ x
        )
myfunc()

print("Python is "+ x)

# When using global keyword we can make a local variable to global.

y = "Suraj"
def myfunc():
    global y
    y = "Thapa"

myfunc()

print("Y is " + y)