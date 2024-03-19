#collection was an four types - 1) list :
# Allows Duplicate
# Any type of Data can be stored
# We can motify the list.it was using a four operations
# insert(),append(),extend(),pop().
a=[1,2,3,4,5,6]
a.insert(0,11)
print(a)

b=[1,2,3,4,5,6]
b.append(7)
print(b)

c=[1,2,3,4,5,6]
c.pop(3)
print(c)

d=[2,4,6]
e=[1,3,5]
d.extend(e)
print(d)
