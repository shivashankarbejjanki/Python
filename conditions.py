"An 'if statement' is written by using the if keyword."

a = 10
b = 20

if b > a:
    print("b is greater than a")


"Elif keyword is used for if the previoues condition is not true"

x = 58
y = 58

if x > y:
    print("x is greater")
elif x == y:
    print("both are equal")


"The else keyword catches anything which isn't caught by the preceding conditions."

p = 46
q = 49

if p > q:
    print("p is greater")
elif p == q:
    print("Both are equal")
else:
    print("q is greater than p")


"You can also have an else without the elif:"

a = 89
b = 99

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")


"The 'and keyword' is a logical operator, and is used to combine conditional statements:"

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


"The or keyword is a logical operator, and is used to combine conditional statements"

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


"The not keyword is a logical operator, and is used to reverse the result of the conditional statement:"

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")




a = 66
b = 55
c = 10

if a > b and a > c:
   print("both are true")


a = 44
b = 55
c = 10

if a > b or a > c:
   print("only one true")



"You can have if statements inside if statements, this is called nested if statements."

x = 99

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



"if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error."

a = 33
b = 200

if b > a:
  pass