# program 1
print("Enter any number :",end=" ")
a = int(input())
print("Enter any number :",end=" ")
b = int(input())
print("1.ADD 2.SUB 3.MULTIPLY 4.DIVIDE")
print("Enter your choice : ",end="")
ch = int(input())
if ch == 1:
    print("Result : ",a + b)
elif ch == 2:
    print("Result : ",a - b)
elif ch == 3:
    print("Result : ",a * b)
elif ch == 4:
    print("Result : ",a / b)
else :
    print("Please enter your choice properly.")

# program 2
print("Enter any number :",end=" ")
a = int(input())
print("Enter any number :",end=" ")
b = int(input())
print("Enter any number :",end=" ")
c = int(input())
if (a > b) & (a > c):
    print(a," is the greatest number")
elif (b > a) & (b > c):
    print(b, " is the greatest number")
else:
    print(c, " is the greatest number")

