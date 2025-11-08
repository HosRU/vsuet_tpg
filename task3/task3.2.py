tuplee = (1,4,6,2,3,9,"element",7,8,5,1,2)

index = 0
for elem in tuplee:
    if elem == "element":
        index = tuplee.index(elem)

if index > 0:
    print(tuplee[index:])
else: print(())