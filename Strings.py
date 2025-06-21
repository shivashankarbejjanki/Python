# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'shiva' is the same as "shiva"

#You can use double or single quotes:

print("Hello")
print('Hello')

# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string;

# Example;
print("It's alright")
print("He is called 'shiva'")
print('He is called "shiva"')




#Assign String to a Variable
#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

#Example;
a = "shiva"
print(a)



'''Multiline Strings
You can assign a multiline string to a variable by using three quotes:

Example
You can use three double quotes:""" or '''

a = '''Hello, my name is Shiva, and I recently completed my Bachelor of Technology in Computer Science from vidya Jyothi institute of technology in the year of 2024. While I come from a technical background, I am now looking for opportunities in non-IT roles where I can contribute with my strengths and grow professionally.
'''
print(a)




'''Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.

Example
Loop through the letters in the word "banana":'''

for x in "Baahubali":
  print(x)



  '''String Length
To get the length of a string, use the len() function.

Example
The len() function returns the length of a string:'''

a = "shiva, shankar"
print(len(a))

x = "The Alchemist by paulo ceolo"
print(type(x))
print(len(x))



'''Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.

Example
Check if "Bejjanki" is present in the following text:'''

txt = "This is shiva shankara chary Bejjanki"
print("Bejjanki" in txt)

txt = "This is shiva shankara chary Bejjanki"
print("Man" in txt)



'''Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

Example
Check if "Bejjanki" is NOT present in the following text:'''

txt = "This is shiva shankara chary!"
print("Bejjanki" not in txt)


message = "shiva shankar"
print(message[0:5])   # start index and end index but here first index is Inclusive i.e Includes and last index is not included.

message = "shiva shankar"
print(message[3:])  # Here only given starting index then it prints from Index3 to all i. va shankar.
                    # This is called Slicing.

message = "shiva shankar"
print(message[:10]) 


message = "SHIVA SHANKAR"
print(message.lower())       # This method is called Lowercase Method 
message = "shiva shankar"
print(message.upper())      # This method is called Uppercase Method

message = "shiva shankar"
print(message.count('a'))   # By using count Method you can know how many times a letter or word repeating.

message = "shiva shankar"
print(message.count('shankar'))

# Replace method; 
message = "shiva shankar"
new_essage=message.replace('shankar','Bejjanki')
print(new_essage)             # replacing the word with other

# Concatinating
first_name = 'welcome'
second_name = 'shiva'
combine  = first_name + ' ' +second_name
print(combine)