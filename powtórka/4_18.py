#18.	Define a function that calculates the sum of number digits. Then use the function to calculate the sum of digits in the number 7182.

def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

number = 7182
result = sum_of_digits(number)
print(f"The sum of digits in the number {number} is {result}.")
