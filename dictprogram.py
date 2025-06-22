# Dictionary is used to store the data values in KEY:VALUES in Pairs
# These are unordered, mutable(changaeble) and dont allow Duplicate values

DictInfo = {
    "name" : "shiva",
    "Roll_no" : 1201,
    "Fav_Sub" : "Maths"
}

print(DictInfo)

info = {
    "name" : "shankar"
}

print(info)

# Nested Dictionary

student = {
    "name" : "shiva shankar",
    "subjects" : {
        "math" : 99,
        "chem" : 89,
        "phy" : 95
    }
}

print(student)
print(student["subjects"]["chem"])