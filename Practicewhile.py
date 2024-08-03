
i = 1
while i<=100:
    print(i)
    i+=1
print("loop ended")


#Practice 2

i = 100
while i >= 1: # this is called Stoping condition
    print(i)
    i -= 1
    print("end")

# Practice 3

n = int(input("enter the number: "))
i =1
while i <= 10:
    print(n*i)
    i += 1

# Practice 4

#Traverse
number = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i<len(number):
    print(number[i])
    i += 1

# Practice 5

num = [1,4,9,16,25,36,49,64,81,100,25,25]
x = 25
i = 0
while i<len(num):
    if(num[i] == x):
        print("found at index", i)
    else:
        print("finding")
    i += 1


