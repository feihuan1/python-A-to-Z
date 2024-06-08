# modules can be considered as small libraries that has some specific features -> some are build in in python like 'math'
import math
import sys as system  # using alias
from random import choice
from enum import Enum
import custom_module

print(math.pi)
print(round(math.pi, 2))

print(choice('123'))

print(dir(system))  # print what in the module, can use '.' too!!!!!

for item in dir(math):
    print(item)

custom_module.random_fun_fact()  # call function from module
print(custom_module.bird) # call value

print(__name__) # return __main__ ==== this is the current module we are running
print(custom_module.__name__) # return module name

system.exit()

# google "Phthon Module Index" => give list of all modules
