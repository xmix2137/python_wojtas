#6.	Define a function that displays numbers in the layout as below 
# (like on a phone keypad). Apply an loop statement. Then call the function.

def phone():
    for i in range(1, 10):
        if i%3==0:
            print(i)
        else:
            print(i, end=" ")
            
phone()
