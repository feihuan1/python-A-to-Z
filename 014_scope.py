# use globle to access globle var, 
# use nonlocal to access parent var!!!
# nonlocal can be passed to grand child 
# globle is like context api ====== nonlocal is like props ddrilling !!!!

name = 'eric'  # globle scope -> access everywhere in file
count = 1  # globle


def greeting(name):
    color = 'blue'  # local scope
    print(name)  # name refer param not globle, cant use globle as defaul value
    print(color)  # can only access inside function


greeting("john")
# print(color) # can't access local scope variable


def another():
    greeting('Dave')  # call globle function
    print(count)  # can access but not modify

    def greet2():  # only accessable in parent scope
        print("hello 2")
        # count = 2 # this is another variable, not the one in globle
        global count
        count += 1  # this is how it works
        print(count)

    greet2()


another()

if True:
    x = 1

if False:
    y = 1

print(x)  # it is defined
# print(y)# not defined lol

print(count)


z = 1
o = 1
p = 3

def parent():
    p = 1
    def change_z():
        z = 2  # this dont change z, z is new var in local
        global o
        o += 1  # this is how to access globle var
        nonlocal p # this will looking for p in parent scope, not globle !!! use globle if want acccess globle var
        p+=1
        print('inside', z, o, p)

        def deep():
            nonlocal p #get from change_z
            print(' this is how to get p into grand child')
        deep()
        
    change_z()


parent()
print('outside', z, o, p)
