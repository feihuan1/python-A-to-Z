import math
# =======================string data type===================================================================

# literal assignment=================

first = 'Eric'
last = 'Peng'

print(type(first))  # <class 'str'>
print(type(first) == str)  # true
print(isinstance(first, str))  # true

# constructor function================================
pizza = str("Popperoni")
print(type(pizza))  # <class 'str'>
print(type(pizza) == str)  # true
print(isinstance(pizza, str))  # true

# Concatenation

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to string===========================
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like musi from " + decade + 's.'
print(statement)

# Multiple lines ===============================

multiline = '''
hey how are you?
        I was just checking in 
                                All good?
'''


print(multiline)

# Escaping special charactors``````````````````````````````````
#          escape'           tab   2 new line         escape\
sentence = 'I\'m back at work!\tHey\n\nWhere\'s this at\\located?'
print(sentence)


# string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())  # capitalize every first letter
print(multiline.replace('good', 'ok'))
print(multiline)  # dont change original data

print(len(multiline))
multiline += '                  '
multiline = '              ' + multiline
print(len(multiline))


print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title = 'menu'.upper()
print(title.center(20, "="))  # center of 20 space replace space with =

print("Coffee".ljust(16, '.') + "$1".rjust(4))
print("Muffin".ljust(16, '.') + "$2".rjust(4))
print("Cheesecake".ljust(16, '.') + "$4".rjust(4))
print('')

# string index value
print(first[0])  # first letter
print(first[-1])  # last letter(includ last)
# second to second to last letter(range return index between two index, including starting but not ending index)
print(first[1: -1])
print(first[1:])  # return second to last letter
# return second to last til last letter(include the -2 index)
print(first[-2:])

# methods return boolean
print(first.startswith('E'))
print(first.endswith('c'))

# =======================boolean data type===================================================================
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# =======================Numeric data type===================================================================
# =######################interger type####################
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# =######################float type####################
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# =######################complex type####################
comp_value = 5 + 3j
comp_value2 = complex(2, 3)
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# build in methods for numbers
print(abs(gpa))  # absolute value

print(round(gpa))  # round the number
print(round(gpa, 1))  # round and keep 1 decimal

# math module
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting string to a number
zipcode = '100001'
zip_value = int(zipcode)
print(type(zip_value))

# Error if attempt to cast incorrect data
# x = (int('haha'))

