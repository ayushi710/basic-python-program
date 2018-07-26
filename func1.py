def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

print ("Enter number:",end=" ")
n = int(input())
x = is_prime(n)
if x == 1:
    print("prime")
else:
    print("not prime")
