#short-hand if statement
if 2 != 1: print("2 is greater than 1")

#short-hand if... else statement
print("True") if 2>1 else print("False")

#This technique is known as Ternary Operators, or Conditional Expressions

#One line if else statement, with 3 conditions
print("A") if 2 > 1 else print("=") if 2==1 else print("B")

#"or" and "and" operators
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions is True")

#nested if statements
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#pass statement
if 3>2:
    pass