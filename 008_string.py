# created with ''  or ""


# quotes for strings
test = 'test'
test2 = "Test2"

# quotes inside of string

test3 = ' he said "this is great" '
test4 = ' he said \'this is great\' '  # escape charactor
print(test3)
print(test4)

# escape charactor

test5 = 'Line1: some text. \nline2: some more text. \ttab is here \rline break'
print(test5)

# multiple lines
test6 = ''' hello 

oh no 


ssssss
'''

print(test6)


# math an string
test7 = 'hello ' + 'world'
print(test7)
test8 = 'copy' * 5
print(test8)

# how to get value from string
name = 'eric'
age = 36
greeting = 'Hello {1}, you are {0} years old'.format(age, name)# indexing
greeting2 = 'Hello {one}, you are {two} years old'.format(two=age, one=name) # assignment
greeting3 = f'Hello {name}, you are {age} years old'# f-string
print(greeting3)

# exercise 
x = 'eric'
y = 'coding' 
text = f'Hello, \nmy name is {name} and my hobby is {y}'
print(text)

