#kalkulator


class kalkulator():
    
    def __init__(self):
       
        self.pamiec = 0
        
    def dodawanie(self, liczba1, liczba2):
        
        self.pamiec = float(liczba1) + float(liczba2)
    
    def odejmowanie(self, liczba1, liczba2):
        
        self.pamiec = float(liczba1) - float(liczba2)
    
    def mnozenie(self, liczba1, liczba2):
        
        self.pamiec = float(liczba1) * float(liczba2)
            
    def dzielenie(self, liczba1, liczba2):

        self.pamiec = float(liczba1) / float(liczba2)
    
    def kasowanie_pamieci(self):
        self.pamiec = 0
        
    def dodawanie_do_pamieci(self, liczba):
        self.pamiec +=liczba
        
    def odejmowanie_od_pamieci(self, liczba):
        self.pamiec -=liczba
        
    def wyswietl_pamiec(self):
        print(self.pamiec)
            

            
kalkulator1 = kalkulator()

a = float(input("Wprowadź pierwszą liczbę: "))
b = input("Wprowadź znak działania: ")
c = float(input("Wprowadź drugą liczbę: "))

if b == "+":
    kalkulator1.dodawanie(a, c)
    print(kalkulator1.pamiec)
    
if b == "-":
    kalkulator1.odejmowanie(a, c)
    print(kalkulator1.pamiec)
    
if b == "*":
    kalkulator1.mnozenie(a, c)
    print(kalkulator1.pamiec)
    
if b == "/":
    kalkulator1.dzielenie(a, c)
    print(kalkulator1.pamiec)
    
kalkulator1.wyswietl_pamiec()
kalkulator1.kasowanie_pamieci()
kalkulator1.wyswietl_pamiec()

