#16.	Each month of a calendar year can be expressed by its
# name or by a number that indicates the position of the month in year. Define a function month(n) 
# that returns a month name based on the month number (values from 1 to 12). 
# Then create a program and display the name of the month 7.

def month(n):
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    if 1 <= n <= 12:
        return month_names[n - 1]
    else:
        return "Invalid month number"

month_number = 7
month_name = month(month_number)
print(f"The name of month {month_number} is {month_name}.")
