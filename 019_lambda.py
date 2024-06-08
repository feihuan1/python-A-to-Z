# lambda function is a function expression that returns a value
# usually used in another function when need a quick func dont want save for later

#higher-order function is a function that either takes one or more functions as arguments or returns a function as its result.

squared = lambda num : num * num

print(squared(5)) 

addTwo = lambda num : num + 2

print(addTwo(2)) 

sum_total = lambda a, b : a + b 
 
print(sum_total(1,2))

########################################################### this is how we use lambda

def func_builder(x): # higher order function , it return a function as result !!!!
    return lambda num : num + x

add_ten = func_builder(10) # this return lamda num: num + 10
add_twenty = func_builder(20)

print(add_ten(7))  # now num is 7 so it return 7!!!!
print(add_twenty(7))

#########################################################->build in higher order functions


################################# map !!!! this dont return list back,  return map object
numbers = [3, 7, 12, 18, 20, 21]

# same as js, but pass data as second params , each element in data will apply as param of call back function, can pass two data set and second will apply as second param in callback function
squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

################################# -> filter !!! this dont return list back, return filter object

odds = filter(lambda num : num % 2 != 0, numbers)
print(list(odds))

################################# -> filter !!! this dont return list back,

from functools import reduce # python dont come with it, import reduce!!!

numbers =[1,2,3,4,5,1] 

add = lambda acc, curr: acc + curr

total = reduce(add, numbers) # same as sum(), but can pass starting number as 3rd params as below
print(total)
print(sum(numbers))# same as line abve

total2 = reduce(add, numbers, 10)
print(total2)
print(sum(numbers, 10) ) # same as line above


### when deal with str
add_len = lambda acc, curr : acc + len(curr)

names =["Eric Peng", "Alex Thomas", "Sara Ito1"]

char_count = reduce(add_len, names, 0) # need put 0 because python assuming acc its str sinnce element in names is str, need specify it's a number
print(char_count)
