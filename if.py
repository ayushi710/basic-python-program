"""
# first if program
print("Enter any 10 number")
i = 1
s = 0
while(i <= 10):
    n = int(input())
    if n% 2 == 0 :
        s = s + n
    i += 1
print("Sum of even number = ",s)




"""
# second if program
for i in range(1,11):
    if i != 5:
        print(i)
print("\n")

# third program
for i in range(1,11):
    if i % 2 == 0:
        j = 1
        while j <= 10 :
            print(str(i) + " * " + str(j) + " = " + str(j * i))
            j = j+1
    else:
        print(i," is odd number\n")
    print("\n")

""" 
# fourth program
se = 0
so = 0
for i in range(20):
 n = int(input("Enter a number : "))
    if n % 2 == 0:
        se = se + n
    else:
        so = so + n
print("Sum of even numbers =", se)
print("Sum of odd numbers = ", so)

"""

# fifth program for prime number

n = int(input("Enter number : "))
for j in range(2,n):
    if n% j == 0:
        print("Not prime")
        break
else:
    print("Prime")
