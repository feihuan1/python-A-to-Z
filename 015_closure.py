# closure is a function having access to the scope of its parent function 
# even after the parent function has returned  -> call tommy so returned, then call again it keep subtract coins from tommy
# this concept is same in python and JS

def parent(person, coins):
    # coins = 3 

    def child(): 
        nonlocal coins # if coins is param of parent, it's same as parent var scope
        coins -= 1

        if coins > 1:
            print('\n ' + person + ' has ' + str(coins) + ' coins left.')
        elif coins == 1:
            print('\n ' + person + ' has ' + str(coins) + ' coin left.')
        else: 
            print('\n ' + person + ' is out of coins')

    return child # not calling 

# use case
# dad gives tommy and jenny 3 coins per person
tommy = parent("Tommy", 3)
jenny = parent("Jenny", 3)
tommy() # tomy play 2 games 
tommy()
tommy()

jenny()# jenny play 1 game

# idea is , when return child, the closure created, the tommy and jenny will have access it's own coins!!!! thats what fuking closure means