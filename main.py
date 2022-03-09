# This is a Simple Interest Calculator
# Question - Find the simple interest when the principal amount is rs 2000, rate of interest is 5% per-annum and the
# time period is of 5 years.

p = float(input("Enter the Principal amount = "))
r = float(input("Enter the rate of interest = "))
t = float(input("Enter the time period = "))
si = (p * r * t)/100
print("Your simple interest is = ", si)
