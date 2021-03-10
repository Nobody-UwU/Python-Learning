fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Syntax:
#newlist = [expression for item in iterable if condition == True]
#The condition is like a filter that only accepts the items that valuate to True
newlist = [x for x in newlist if x!="apple"]
print(newlist)

#The condition is optional and can be omitted:
newlist = [x for x in fruits]
print(newlist)

#The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [_ for _ in range(10) if _ < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

#"Return the item if is not banana, if it is banana return orange".
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)