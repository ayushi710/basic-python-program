# perfect number
print("Enter a number to check whether number is perfect or not :",end=" ")
n = int(input())
sum = 0
for i in range(1 , n):
    if (n % i) == 0:
        sum = sum + i
if n == sum :
    print(n," is a perfect a number")
else :
    print(n,"is not a perfect number")

