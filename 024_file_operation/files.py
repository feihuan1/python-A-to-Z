# just like crud
# r = Read 
# a = Append 
# w = Write 
# x = Create

#                                   ******************Read - error if doesn't exist *****************


f = open("names.txt", "r") # read names.txt (r means read, rt-> text file, rb -> binary file), default is read open('file_name') will read the file too 

# print(f.read())# if terminal not in current directory, it wont found the file!!!
# print(f.read(4))# read 4 letter, space or new line counts
# print(f.readline())# read first line
# print(f.readline())# this will read second line if read first line above already(will be space between two lines)

# loop through lines in file 
print(f) #prints html like tag

for line in f:
    print(line)

f.close()# same out put but this is super important, changes won't show up until close file, open -> change file -> close -> open -> access change

# open file not exist
# first approach
try:
    file = open("dsfdsf.txt")
    print(file.read())
except:
    print('file not exist')
else:# close it!!!
    file.close()

# 2nd approach
try:
    with open("dsfdsf.txt", "r") as file: # with statement auto close file after it's block of code excuted, even exception occur
        print(file.read())
except FileNotFoundError:
    print('file not exist')

# 3rd approach
try:# f is already defined on the top, but blocked when re-assign, if not defined, error will thrown
    f = open("dsfdsf.txt", "r") 
    print(f.read())
except FileNotFoundError:
    print('file not exist')
finally:
    f.close()

# 4th approach
file = None
try:# file defined as None, if not error will appear
    file = open("dsfdsf.txt", "r")
    print(file.read())
except FileNotFoundError:
    print('file not exist')
finally:
    if file:
        file.close()


#                                   ****************** Append to file - creates the file if it doesn't exist *****************
# append to the end of file

a = open("names.txt", "a") # "a" means append
# a.write("\nNeil") # this will append Neil every time it runs
a.close()

a = open("names.txt") # "a" means append
print(a.read())
a.close()


#                                   ****************** Write - creates the file if it doesn't exist *****************
# this overwrites everything in file, be super careful!!!!
w = open("context.txt", "w") # w means write
w.write("I deleted all context")
f.close()

w = open("context.txt") # "a" means append
print(w.read())
w.close()

#                                   ****************** Create - Two ways to create!!! *****************
# each way creating file has it's own use case
# open a file for writing -> creates the file if it doesn't exist

c = open("not_exist.txt", "w") # this line will create a new file in current directory
f.close()

# creates the specified file, but retuns a error if the file exists
# so need check before creates the file 
# # -> need import os!!!!
import os 

if not os.path.exists("eric.txt"):
    cn = open("eric.txt", "x") # x means creae, not C!!!!
    cn.write("hello there!")
    cn.close()


#                                   ****************** Delete a file - rasie error if file not exist *****************

# avoid an error if it doen't exist 
if os.path.exists("not_exist.txt"):
    os.remove("not_exist.txt")
else:
    print("don't need delete")

if os.path.exists("eric.txt"):
    os.remove("eric.txt")
else:
    print("don't need delete")



# with key word

# read more_name and copy it to names -> with will auto close file when block of code excuted
with open("more_names.txt") as b:
    content = b.read() 

with open("names.txt", "w") as b:
    b.write(content)