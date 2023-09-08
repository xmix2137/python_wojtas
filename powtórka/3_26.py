#26.	The payment card is secured with a four-digit PIN code (0805).
# Write a program that checks if the PIN code entered in the payment terminal is correct. 
# The user has up to three possibilities for entering a PIN code. 
# In case of three unsuccessful attempts, the card is blocked. Sample result:

correct_pin = "0805"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_pin = input("Enter the PIN code: ")

    if entered_pin == correct_pin:
        print("PIN code accepted. You have access to your payment card.")
        break
    else:
        print("Incorrect...")
        attempts += 1

if attempts == max_attempts:
    print("Sorry, your payment card has been blocked.")
        