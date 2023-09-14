#30.	A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number. 
# Write a program that finds N leading prime numbers. Read the value of N from the keyboard. 
# Using loop statements check that the number N is divisible only by 1 and by N.


n = int(input("Wprowadz liczbę większą od 1: "))
pierwszetab = []
pierwsze = 0
licznik = 0
g = 0

while pierwsze<n:
    licznik+=1
    if licznik>1:
        g = 0
        for i in range(1, licznik+1):
            if licznik%i==0:
                g+=1
    if g==2:
        pierwszetab.append(licznik)
        pierwsze+=1
        
print(pierwszetab)
                