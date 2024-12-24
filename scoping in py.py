#LEGB
# local enclosing global built in
#this is how py check a verible in LEGB scopes

x = 'global veriable'


#this how global veriable define


def func():
    return 'local veriable'


print(func(), x)


#we can access global scope in local scope, but we are not able to access local in global scope like js if we want we need
#to define global veriabe in local envirment

def func2():
    global x
    xyz = 'global 1 veriable'
    # print(x)


print(x)


#enclusing scope
def outer():
    x = 'outer x'

    def inner():
        print(x)

    inner()
    print(x)
    outer()

#closin a function in an existing function


#builtin scope
#in this scope if we use a function that already built in we use like min() max() from math they called builtin function
