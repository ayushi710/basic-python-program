# using for loop
for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print("\r")

print("\n")

# using while loop
i = 1
while i <= 6:
    j = 1
    while j <= i:
        print("* ",end="")
        j = j+1
    i = i+1
    print("\r")