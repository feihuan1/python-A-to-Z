
# Dictionary

band = {
    "vocals": "Plant",
    "guitar": "Page",
}
# constructors
band2 = dict(vocals="Plant", guitar="Page")

print(band, band2)
print(type(band))
print(isinstance(band, dict))
print(len(band))  # check size lol

# access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list key/value as tuples
print(band.items())

# has own property
print("guitar" in band)
print("triangle" in band)

# change value
band['vocals'] = "updated"  # modify
band.update({"guitar": "updated"})  # modify
band['piano'] = "Add New"  # add
band.update({"bass": "New"})  # add
print(band)

# remove
print(band.pop("bass"))  # pass key return value!!! remove last item in dict
print(band)

print(band.popitem())  # return key value as tuple, remove last added item in dict
print(band)

print(band2.popitem())  # return a tuple, last item in dict removed
print(band2)

# delete and clear
del band['vocals']  # delete one item
print(band)
band2.clear()  # make it empty
del band2  # destroy this dict
# print(band2)#⬆️ band 2 became undifined

# copy dict

# band2 = band # create a reference, not copy -> reference type -> 2 variable will always be same value
# print("bad copy")
# print(band2)
# print(band)
# band2["drums"] = "dave" # both will change
# print(band2)
# print(band)

# 1. use copy method
band2 = band.copy()  # right way mae copy
# print("good copy")
# print(band2)
# print(band)
# band2["drums"] = "dave" # band will not change
# print(band2)
# print(band)

# 2. use dict() constructor
band3 = dict(band)
band2 = band.copy()  # right way mae copy
print("good copy")
print(band2)
print(band)
band2["drums"] = "dave"  # band will not change
print(band2)
print(band)

# Nested dict
member1 = {
    "name": "Plant",
    "instrument": "Vocals",
}
member2 = {
    "name": "Page",
    "instrument": "Guitar",
}

band4 = {
    "member1": member1,
    "member2": member2,
}
print(band4)
print(band4['member1']["name"])

# ============================================SETS
# use assignment
nums = {1, 2, 3, 4}
# use constructor
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))
print(isinstance(nums, set))

# No duplicates allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
# true is gone because 1 infront, 0 gone becuase False infront of it
nums = {1, True, False, 0, 2, 4}
print(nums)

# check value in set
print(2 in nums)
# cant refer to element in set with an index position or a key

# add value
nums.add(8)
print(nums)

# add element from one set to another (concat)
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# can use update with list tuple and dict to

# merge two set create new set
one = {1, 2, 3}
two = {5, 6, 7}
newset = one.union(two)  # wont change original set
print(newset)

# keep the duplicate
one = {1, 2, 3, 6}
two = {5, 6, 7, 3}
one.intersection_update(two)  #  change the first set become only duplicates
print(one) # one changed

# keep everything but remove duplicates 
one = {1, 2, 3, 5, 6}
two = {5, 6, 7, 2}
one.symmetric_difference_update(two)  # duplicates will be gone, not keep even one of them
print(one)