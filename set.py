# a={1,2,3};b={2,3,4};c={3,4,5};d={5,6,7}
# print(a.intersection(b))
# print(a.intersection(c))
# print(a.intersection(d))



# """""union"""
# print(a.union(b))""
# print(a.union(d))
# print(b.union(c))



# ""'""'update """""""
# a.update(c)
# print(a)
# a.update(d)
# # print(a)


# """" difference """ 
# a={1,2,3,False,4,}
# b={4,5,6,False,None,True}
# c=b.symmetric_difference_update(a)
# print(c)
# print(a-b)
# print(b-a)

# """""" discard"""""


# """pop"""


# a={1,2,3,4}
# a.pop()
# print(a)
# a.pop()
# print(a)


# """" disjoin """


# a={1,2,3,4}
# b={3,4,7,8}
# print('are  a and b disjoint',a.isdisjoint(b))
# print('are  a and b disjoint',a.isdisjoint(b))
# print('are  a and b disjoint',a.isdisjoint(b))

# # """""issubset"""

# a={1,2,3,4}
# b={1,2,3,4}
# c={4,5,6,7}
# print(a.issubset(b))
# print(a.issubset(c))


'''''symmetric_difference_update'''

# a={44,55,6,55,77}
# b={4,55,6,7}
# (b.symmetric_difference_update(a))
# print(a)




# a={44,55,66,77}
# b={55,77,99,00}
# (a.symmetric_difference_update(b))
# print(a)

"""'""remove"""

# a={44,55,66,77}
# a.remove(55)
# print(a)


""""'"issuperset"""

# a={20,30,40,50}
b={20,30,40,50}
# print(a.issuperset(b))
b={20,30,40,50}
c={60,70,80,22}
print(b.issuperset(c))

a={1:'moulali',
   2:'history'}
print(a)