thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

reverse = []
for x in thislist:
    reverse.insert(0,x)
print(reverse)
#alternately
thislist.sort(reverse=True)
print(thislist)

def myfunc(n):
  return abs(n - 50)
x=51
print(myfunc(x))
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True, key=myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)