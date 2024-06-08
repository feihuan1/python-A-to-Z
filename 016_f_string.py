# search for pythonformatting types, many tricks there like :.2f

# exp:
person = "Eric"
coins = 3

print('\n' + person + ' has ' + str(coins) + ' coins left.')


message = '\n%s has %i coins left.' % (person, coins)  # old way like c
print(message)

message2 = '\n{0} has {1} coins left.'.format(
    person, coins)  # pass var via index
print(message2)

message3 = '\n{person} has {coins} coins left.'.format(
    person=person, coins=coins)  # assign vars by name
print(message3)

message4 = '\n{} has {} coins left.'.format(
    person, coins)  # defaul asign by order
print(message4)


# use dict ==== use this if you have tons of var to insert!!!
player = {"person": "Eric", "coins": 3}
# assign by accessing dict, ** will look for all keys and asign to string matched place
message3 = '\n{person} has {coins} coins left.'.format(**player)
print(message3)


# f-string  -> this is the way

# could lead to error if user input cause a comment
print(f'\n{person} has {coins} coins laft')
# do thins inside f-string
print(f'\n{person.lower()} has {2 * coins} coins laft')

print(f'\n{player['person']} has {
      player['coins']} coins laft')  # accessing dict

##############
num = 10
# :.2f means fixed at second decimal
# this is how to fix a number to a string, if want return number, use round()
print(f"\n 2.25 times {num} is {2.25 * num:.2f}")


for num in range(1, 11):  # loops ~
    print(f"2.25 times {num} is {2.25 * num:.2f}")# this is how to fix a number to a string, if want return number, use round()

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")# this is how to fix a number to a %tage
