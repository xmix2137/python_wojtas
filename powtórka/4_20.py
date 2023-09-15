#20.	Define a function power(x, n) that evaluates xn. Apply recursion. Then calculate 53.
#Tip: xn =  x * xn-1

def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / (x * power(x, -n - 1))
    else:
        return x * power(x, n - 1)

result = power(5, 3)
print(f"5^3 is equal to {result}")

