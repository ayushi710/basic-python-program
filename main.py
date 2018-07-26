from functions import perfect
print("Enter a number :",end=" ")
num = int(input())
p = perfect(num)
if p :
    print("Perfect")
else:
    print("Not Perfect")

