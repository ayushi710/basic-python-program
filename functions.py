def pattern():
    for i in range(6):
        for j in range(i):
            print("*",end=" ")
        print("\r")

def prime(num):
    for i in range(2,num):
        if num % 2 == 0 :
            return False
    return True

def perfect(num):
    s = 0
    for i in range(1 , num):
        if num % i == 0:
            s = s + i
    if s == num:
        return True
    else:
        return  False

def palindrome(num):
    rev = 0
    k = num
    while k > 0:
        d = k % 10
        rev = rev * 10 + d
        k = k//10
    if rev == num:
        return True
    else:
        return False

def armstrong(num):
    arm = 0
    k = num
    while k != 0:
        d = k % 10
        arm = arm + (d**3)
        k = int(k/10)
    if arm == num:
        return True
    else:
        return False