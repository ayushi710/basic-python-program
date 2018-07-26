print("Enter basic salary ")
basic = float(input())
ta = 0.02 * basic
da = 0.02 * basic
hra = 0.03 * basic
itax = 0.02 * basic
total = basic + ta + da + hra + itax
print("Total Salary = ", total)