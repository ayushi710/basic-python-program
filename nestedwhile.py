print("Enter Number :",end=" ")
num = int(input())
i = 1
while i <= num:
    j = 1
    while j <= 10:
        print(str(i) + " * " + str(j) + " = " + str(j * i))
        j = j+1
    print("\r")
    i = i+1
