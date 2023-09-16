#Dla podanej listy wyrazów [brzuch, ramie, dupa, noga, cyce, plecy] znajdź: 
#najdłuższy wyraz, najkrótszy wyraz, ilość wystąpień litery c we wszystkich wyrazach, wszystkie wyrazy dłuższe niż 4 znaki

tab = ["brzuch", "ramie", "dupa", "noga", "cyce", "plecy"]

def najdluzszy(tab):
    naj = tab[0]
    for i in range(len(tab)):
        if len(tab[i])>len(naj):
            naj = tab[i]
    return naj

print(najdluzszy(tab))

def najkrotszy(tab):
    naj = tab[0]
    for i in range(len(tab)):
        if len(tab[i])<len(naj):
            naj = tab[i]
    return naj

print(najkrotszy(tab))

def c_app(tab):
    licznik = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == "c":
                licznik+=1
    return licznik

print(c_app(tab))

def dluzsze(tab):
    lista = []
    for i in range (len(tab)):
        if len(tab[i])>4:
            lista.append(tab[i])
            
    return lista

print(dluzsze(tab))