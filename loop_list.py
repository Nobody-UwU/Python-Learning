thislist = ["Orange", "Apple", "Guava"]

for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(i)

z = 0
while z < len(thislist):
    print(thislist[z])
    z = z + 1

[print(x) for x in thislist]