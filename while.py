# while loop
i = 1
while i <= 10:
    print(i,end=" ")
    i += 1
print("\n")

# print sum of 10 number
i = 1
sum = 0
while i <= 10:
    print("enter no :",end="")
    n = int(input())
    sum = sum + n
    i += 1
print("Sum of given 10 number = ",sum)
print("\n")

# while program 3

print("Enter number :",end="")
n = int(input())
s = n
while n != 0 :
    print("Enter number :", end="")
    n = int(input())
    s = s + n
print("Sum = ",s)
print("\n")