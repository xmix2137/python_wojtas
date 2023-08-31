# 18.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). #
# Write a program showing any amount (natural number) read from 
# the keyboard with as few coins as possible.

a = input("Wprowadź liczbę: ")
p = 0
d = 0
j = 0

liczba = int(a)

g = liczba//5
liczba%=5
p+=g
h = liczba//2
d+=h
liczba%=2
j+=liczba
print(p, d, j)
        