#29.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. 
# Entering 0 ends entering numbers. Sample result:

total = 0
count = 0

while True:
    num = float(input("Enter number: "))
    if num == 0:
        break
    total += num
    count += 1

if count > 0:
    mean = total / count
else:
    mean = 0

print(f"RESULT: Quantity={count}, Sum={total}, Mean={mean}")