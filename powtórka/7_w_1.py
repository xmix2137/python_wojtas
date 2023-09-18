#Wygeneruj 5 wierszy po 5 liczb 0-100 zapisz je do pliku o nazwie "pliki_sa_bez_sensu_na_chuj_to_robic" i wyprintuj
import random
plik = open("C:\Test\pliki_sa_bez_sensu_na_chuj_to_robic.txt",'w')
for i in range(5):
    for j in range(5):
        print((str(random.randint(1,100))), end=" ")
    print()
plik.close()

plik2 = open("C:\Test\pliki_sa_bez_sensu_na_chuj_to_robic.txt",'r')
plik2.close()

print(plik2)
