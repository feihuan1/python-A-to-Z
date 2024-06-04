# methods are functions that are attached to objects
#  the reason why there are both functions and methods is that some functionality should only exist for certain objects, exp: it make no sense to have a function to create an uppercase number


# google python string methods

test = 'a Word'
print(test.upper())  # dont change the oringal data !!!
print(test)
print(test.lower())  # dont change the oringal data !!!
print(test)
print(test.capitalize())  # dont change the oringal data !!!
print(test)
test.upper()  # invalid not store anywhere
test = test.upper()  # change origianl value
print(test)

username = "John sMIthxX"
print(username.title())  # capitalize each word
print(username.strip("X"))  # remove head and tail matiches argument

print(dir(username))  # show all methods can apply to the variable

print(username.isalpha())# space is not alpha

exercise_string = 'I like puppies'
print(exercise_string.replace('puppies', 'kittens'))
