# myDict.keys() returns all keys

student = {
    "name" : "shiva",
    "Roll_no" : 1201,
    "Grade" : "First class"
}

print(len(list(student.keys())))
print(len(student))
print(type(student))

# Returns all Values

print(student.values())
print(len(student.values()))

# Returns all (key,val) pairs as tuples

print(student.items())

# Returns the key according to values

print(["name1"]) #error
print(student.get("name")) #no error --> none

# Inserts the specified items to the Dictionary --> myDict.update(newDict)

# new_Dict = {"nam2":"shiva"}
student.update({"name3" : "mahi"}) #or
new_Dict = {"name2":"shiva"}
student.update(new_Dict)
print(student)

# In Dictionary OverWrite will occur due to Duplicates dont allow when you give the same key