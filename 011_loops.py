# while loop

value = 1

while value <= 10:
    if (value == 3):  # !!!!!!!!!!!!!!!!! () works lol
        value += 1  # this is importtant, if value dont + , it will always = 3 and continue
        continue  # skip current loop,
    # if value == 5:
    #     break  # stop the loop
    print(value)  # if move this up, it will print 5
    value += 1  # this order matters too, if move to top, it will print 2-11 without ifs
else:  # will run when complete loop (not break)
    print('done')

names = ['Dave', 'Sara', 'john']

for name in names:  # loop list
    print(name)
else:
    print('it is over')

for char in 'Mississipi':  # loop str
    print(char)
else:
    print('it is over')

for x in names:  # Dave
    if x == 'Sara':
        break
    print(x)
else:
    print('it is over')

for x in names:  # Dave John
    if x == 'Sara':
        continue
    print(x)
else:
    print('it is over')

for x in range(4):  # 0 1 2 3
    print(x)
else:
    print('it is over')

for x in range(2, 4):  # 2, 3
    print(x)
else:
    print('it is over')

for x in range(0, 10, 2):  # 0 2 4 6 8
    print(x)
else:
    print('it\'s over') # run after loop

r = range(0, 10, 2)
print(type(r))  # there is a type called range!!!
print(isinstance(r, range))  # True

names = ['Dave', 'Sara', 'john']
actions = ['codes', 'eats', 'sleeps']

for name in names:  # loop in loop
    for action in actions:
        print(name + ' ' + action)


for action in actions:  # loop in loop
    for name in names:
        print(name + ' ' + action)
