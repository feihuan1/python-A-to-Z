import sys

# noob
# print("     #")
# print("    ###")
# print("   #####")
# print("     #")
# print("    ###")
# print("   #####")
# print("  #######")
# print("     #")
# print("    ###")
# print("   #####")
# print("  ########")
# print(" ##########")
# print("    ###")
# print("    ###")
# print("    ###")


# pro
user_input = input("How high do you want your tree be?")


while(not user_input.isnumeric()): 
    user_input = input("How high do you want your tree be?")

height = int(user_input)

def print_row(n, buttom_len):
    char = ''
    for _ in range(n):
        char += '#'
    print(char.center(buttom_len+1, ' '))


def print_tree(height):
    bottom_len = 3 + 2 * height
    for chunk in range(1, height + 1):
        for row in range(1, chunk + 3):
            print_row(1 + 2 * (row - 1), bottom_len)

    # Print the trunk
    for _ in range(height):
        print('###'.center(bottom_len, ' '))


# height = input('how height do you want the tree be?')
print_tree(height)
a = None #null
print(print(6))# 6 None
print(type(a))# NoneType 
# print(type(a) == NoneType)  #error, NoneType is not build in

