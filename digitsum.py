print("Enter any number :",end="")
n = int(input())
s = 0
s1 = 0
k = n
count = 0
while k != 0 :
    d = int(k % 10)
    s1 = s1 + d
    s = s*10 + d
    k = int(k / 10)
    count = count +1
print("Sum of digit =",s1)
print("Reverse of digit = ",s)
print("Number if digit =",count)