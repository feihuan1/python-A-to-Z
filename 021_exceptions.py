
# create a custom error inheretant from Exception class 

class NotGoodLookingError(Exception):
    pass


x = 2
try:
    raise NotGoodLookingError(" you are not good looking")  #👇 raise an error will block code after it, notice else block is grayed out too!!!
    raise Exception("'I'm a custom exception")# custom exception with custom massage
    # when ever had a error, it will stop the code and run except, order below matters
    # print(x / 0)
    # print(y)# not defned
    # if not type(x) is str:
    #     raise TypeError('only str are allowed') # raise error by your self
except NameError:# catch only name error won't catch other error
    print('NameError means something might not be defined')
except ZeroDivisionError: 
    print('pls dont be stupid')
except Exception as error: #cover other error raised by your self
    print(error)
else:# rasie an error in try will blocl this
    print('no error')# this will run if no error occur! why not just put this into try block????
finally:# run no matter what
    print('this will run with or without error')