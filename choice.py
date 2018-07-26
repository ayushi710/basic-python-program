from functions import *

print("Enter pattern ")
print("Enter prime")
print("Enter perfect")
print("Enter palindrome")
print("Enter armstrong")
print("Enter your choice :", end=" ")
choice = input()
if choice == "pattern":
    pattern()

elif choice == "prime":
    print("Enter a number :", end=" ")
    n = int(input())
    if prime(n):
        print(str(n)+" is a prime number")
    else:
        print(str(n) + " is not a prime number")

elif choice == "perfect":
    print("Enter a number :", end=" ")
    n = int(input())
    if perfect(n):
        print(str(n) + " is a prefect number")
    else:
        print(str(n) + " is not a prefect number")

elif choice == "palindrome":
    print("Enter a number :", end=" ")
    n = int(input())
    if palindrome(n):
        print(str(n) + " is a palindrome number")
    else:
        print(str(n) + " is not a palindrome number")

elif choice == "armstrong":
    print("Enter a number :", end=" ")
    n = int(input())
    if armstrong(n):
        print(str(n)+" is a armstrong number")
    else:
        print(str(n) + " is not a armstrong number")

else:
    print("Wrong Choice !")