#20.	Write a program that creates a multiplication table in the range 1 to 10 for any number entered by the user. Sample result:

a = input("Wprowadź liczbę: ")
ai = int(a)
b = 1

for i in range(10):
    wynik = ai*b
    b+=1
    print(wynik)