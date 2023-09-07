#21.	The 'university' variable contains the name of university where you study. 
# Write a program that displays the contents of the 
# variable with an extra space between characters (add a space between each character).

a = input("Wprowadź nazwę: ")
b = ""

for i in range(len(a)):
    b+=a[i]
    b+=" "

print(b)