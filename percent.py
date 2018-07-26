sum = 0
print("enter marks of 4 subjects")
for i in range(4):
    m = int(input())
    sum = sum + m
percent = sum / 4
print("Percentage = ", percent)