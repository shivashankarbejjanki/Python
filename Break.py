# Break Keyword is used to TERMINATE the LOOP statement

i = 1
while i <= 10:
    print(i)
    if(i == 5):
        break
    i += 1

print("loop ended")

num = [1,4,9,16,25,36,49,64,81,100,25,25]
x = 25
i = 0
while i<len(num):
    if(num[i] == x):
        print("found at index", i)
        break
    else:
        print("finding")
    i += 1