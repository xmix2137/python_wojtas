#25.	The variables a and b contain the dimensions of the sides of the rectangle. 
# Write a program that creates the following rectangle with dimensions a and b. Example result for a = 4 and b = 15:

a = input("Wprowadź a: ")
b = input("Wprowadź b: ")

print("*"*int(a))
for i in range(int(b)-2):
    print("*"+" "*(int(a)-2)+"*")
print("*"*int(a))