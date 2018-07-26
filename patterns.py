# pattern 1
print("\n PATTERN 1 \n")
for i in range(5):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print("\r")

# pattern 2
print("\n PATTERN 2 \n")
for i in range(5,0,-1):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print("\r")

# pattern 3
print("\n PATTERN 3 \n")
for i in range(7):
    for j in range(i):
        print("*",end=" ")
    for k in range(12 - 2*i):
        print(" ",end=" ")
    for l in range(i):
        print("*",end=" ")
    print("\r")

# pattern 4
print("\n PATTERN 4 \n")
for i in range(6 , 0 , -1):
    for j in range(i):
        print("*",end=" ")
    for k in range(12 - 2*i):
        print(" ",end=" ")
    for l in range(i):
        print("*",end=" ")
    print("\r")

# pattern 5
print("\n PATTERN 5 \n")
for i in range(5):
    for k in range(5-i):
        print("",end="  ")
    for j in range(2*i+1):
        print("*",end=" ")
    print("\r")

for i in range(4,0,-1):
    print("",end="  ")
    for k in range(5-i):
        print("",end="  ")
    for j in range(2*i-1):
        print("*",end=" ")
    print("\r")

# pattern 6
print("\n PATTERN 6 \n")
for i in range(5,0,-1):
    for k in range(5-i):
        print("",end="  ")
    for j in range(2*i-1):
        print("*",end=" ")
    print("\r")
for i in range(2,6):
    for k in range(5-i):
        print("",end="  ")
    for j in range(2*i-1):
        print("*",end=" ")
    print("\r")

# pattern 7
print("\n PATTERN 7 \n")
for i in range(6):
    for j in range(i):
        print(j+1,end=" ")
    print("\r")

# pattern 8
print("\n PATTERN 8 \n")
for i in range(6):
    for j in range(i):
        print(i,end=" ")
    print("\r")