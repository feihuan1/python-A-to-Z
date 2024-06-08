

def add_to_ten_loop(num):
    pass


def add_to_ten_rec(num): 
    if(num >= 9):
        return num + 1 

    total = num + 1 
    return add_to_ten_rec(total)


print(add_to_ten_rec(3))
print(add_to_ten_loop(4))

