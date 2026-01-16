import copy

li = [1,2,3,[5,8]]
a = copy.deepcopy(li)
li[1] = 6
a.append(100)
print(li)
print(a)
print(li)
print("programming in python")
print("smdfsdl")
