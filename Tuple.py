thisis_tuple = (1,2,3,4,5)
print(thisis_tuple)

String_tuple = ("shiva", "prabhas", "rasi", "trisha")
print(String_tuple)

String_tuple = ("shiva", "prabhas", "rasi", "trisha")
print(len(String_tuple))                    # By using LEN() function we can find out the lenght of a tuple.


'''Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.'''

# One item tuple, remember the comma:

thistuple = ("shiva",)
print(type(thistuple))

#NOT a tuple
thistuple = ("shiva")
print(type(thistuple))    # This comes under String class.

# A tuple can contain different data types.
tuple1 = ("shiva", 24, True, 175, "male")
print(tuple1)

mytuple = (1,2,3,4,5,6,7,8,9)
print(type(mytuple))

tuple1 = tuple(("shiva", "vaishali", "manogna", "hemanth"))  # note the double round brackets(mandatory).
print(tuple1)               # By using tuple() Constructor we can create a tuple.

# In tuple() also you can use all the functions that are used in list.