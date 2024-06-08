# ============================================list
users = ['Dave', 'Eric', 'Alex']

data = ['Eric', 42, True]

empty_list = []

# check if value in list jsArray.include()
print('Dave' in users)

# indexing
print(users[0])

print(users[-1])  # last value
print(users[-2])  # last second value

# modify
users[0] = 'Alexxxx'

# Array.findIndex()
print(users.index("Eric"))

# slicing always incuding start but not ending index
print(users[0:2])  # slicing 0 - 2 not including 2, same as string

print(users[1:])
print(users[-3:-1])  # not including -1
print(users[-3:])  # include -3

print(len(data))  # get length

# ################################################add to end
users.append('Elsa')
print(users)

# ############################################################concat
users += ['Jason']
print(users)
users.extend(['Robert', 'Jimmy'])
print(users)

# concat every letter, because string is a list of char || split()? -> [] += "hello"
data.extend('Hello')
print(data)

# ####################################################################################insert
users.insert(0, 'Bob')  # index -> value
print(users)

# concat this list at index 2, and add from original index 2 as tail of list
users[2:2] = ["New Person", "Another Person"]
print(users)

# replace value
# concat this list at index 1, and add from original index 4 as tail of list
users[1: 4] = ['Robert', 'HP']
print(users)

# remove data
users.remove('Bob')
print(users)

# ############################################################pop out
last_element = users.pop()
print(last_element + ' -> ', users)

# ################################################ delete index
del users[0]
print(users)
# dealocate list from memory
# del data
# print(data)#not defined

data.clear()  # empty an array
print(data)

# sort  || modify origianl list
users[1:2] = ["eric"]
users.sort()  # sort alphabeticlly, upper case come first
print(users)

users.sort(key=str.lower)  # sort alphabeticlly, include the lower case
print(users)
nums = [4, 42, 78, 1, 5]

nums.sort()  # sort accending order no call back needed lol
print(nums)
nums2 = [4, 33, 24, 22, 12, 1]
nums2.sort(reverse=True)  # sort decending order
print(nums2)

# ################################################sort || return copy
nums4 = [2, 4, 21, 22, 11, 1, 6]
# return a new list, remove reverse to be accending order

nums4_copy = sorted(nums4, reverse=True)  # fasted way
nums5 = [2, 1, 4, 44, 22]
nums5_copy = nums5.copy()
another_nums5_copy = list(nums5)
slice_copy = nums5[:]  # slice from 0 to end, can be [0:]
print(nums5, slice_copy)


# reverse
nums3 = [4, 42, 1, 55, 5, 2]
nums3.reverse()
print(nums3)

print(type(nums))  # list
print(type(nums) == list)  # True


# =================================================== Tuple  **** can't change but can copy
# when assign value, call PACKTHETUPLE
my_tuple = tuple(('Eric', 42, True))
my_tuple2 = (1, 4, 2, 8)

print(my_tuple[1])  # accessing the value

print(my_tuple)
print(type(my_tuple))  # tuple

# count return how many element match the passed in value
print("count: ", my_tuple, my_tuple.count(1))  # True is 1 omfg
print(my_tuple.index(True))  # return index of the passed in value in a tuple

# ##############################################copy
new_list = list(my_tuple)
new_list.append("new value")
new_tuple = tuple(new_list)

print(my_tuple, new_tuple)

# UNPACK TUPLE --> similar as array distruction

# put * before, z will be the remaining value in tuple with list, or has to pass same amount of variable as tuple element
(x, y, *z) = my_tuple2
print(x)
print(y)
print(z)

(a, *b, c) = my_tuple2  # b will contain list of 2 value
print(a, b, c)

# #error, tuple cant change
# my_tuple[1] = 1
# print(my_tuple)
