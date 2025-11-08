from collections.abc import Hashable

list = [1,2,5,8,2,4,8,565,9,87,2345]
newlist = set(list)

for elem in list:
    if isinstance(elem, Hashable):
        newlist.add(elem)

print(newlist)