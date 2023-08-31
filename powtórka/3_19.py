#19.	Write a program that calculates a dog's age in dog’s years.
# For the first two years,
# a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years.

a = int(input("Wpisz wiek: "))
wiek = 0

if a <= 2:
    wiek+=a*10.5

else:
    wiek = (a-2)*4+21
    
print(wiek)