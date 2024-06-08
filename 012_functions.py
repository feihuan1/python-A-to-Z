
def hello_world():
    print("Hello World")


hello_world()


def sum(num1=0, num2=0):

    if (type(num1) != int or type(num2) is not int):
        return

    return num1 + num2

print(sum(3))

def multiple_items(*args):
    print(args) # tuple
    print(type(args))

multiple_items(1,2,"a", True, [6,7], {"c": "b"})

def mult_named_items(**kwargs):#key word arguement
    print(kwargs) # dict
    print(type(kwargs))

mult_named_items(a=1,b=2,c="a", d=True, e=[6,7], f={"c": "b"})