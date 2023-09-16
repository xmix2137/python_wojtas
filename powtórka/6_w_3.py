#Dla podanej macierzy 1d [3, 8, 12, 45, 10, 17, 18, 99, 64, 35], oblicz: 
# mediane używając funkcji sort
#ilość liczb więszych niżliczba podana z klawiatury
#zamień podaną macierz na macierz 2d

tablica = [3, 8, 12, 45, 10, 17, 18, 99, 64, 35, 100]

def mediana(tab):
    mediana = 0
    tab.sort()
    print(tab)
    if len(tab)%2 == 0:
        mediana = (tab[len(tab)//2-1]+tab[len(tab)//2])/2
    else: 
        mediana = tab[len(tab)//2]
    return mediana

print(mediana(tablica))

def ilosc(tab):
    a = int(input("Wprowadź liczbę: "))
    licznik = 0
    for i in range(len(tab)):
        if tab[i]>a:
            licznik+=1
    return licznik

#print(ilosc(tablica))

def dwade(tab):
    tab2d = []
    if len(tab)%2 == 0:
        for i in range(0, len(tab), 2):
            pomoc = []
            for j in range(2):
                pomoc.append(tab[i+j])
            tab2d.append(pomoc)
    else:
        tab.append(0)
        for i in range(0, len(tab), 2):
            pomoc = []
            for j in range(2):
                pomoc.append(tab[i+j])
            tab2d.append(pomoc)      
    return tab2d

print(dwade(tablica))