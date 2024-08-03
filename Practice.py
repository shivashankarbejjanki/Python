#First practice

Dict = {

"cat" : "a small animal",
"table" : ("a piece of furniture", "list of facts & figures")
}
print(Dict)

# second practice

subjects = {
    "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
}
print(subjects)
print(len(subjects))

# third prctice

marks = {}

x = int(input("Enter phy: "))
marks.update({"phy" : x})

x = int(input("Enter chem: "))
marks.update({"chem" : x})

x = int(input("Enter math: "))
marks.update({"math" : x})

print(marks)

# Fourth practice

values = {9, "9.0"}
print(values) #or you can write like this also

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)

