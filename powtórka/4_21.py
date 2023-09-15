#21.	Define an anonymous function that returns true when the first number is greater than the second one.
# Otherwise returns false. Use the conditional operator. 

greater_than = lambda x, y: True if x > y else False

result1 = greater_than(5, 3)
result2 = greater_than(3, 5)

print(result1)
print(result2)
