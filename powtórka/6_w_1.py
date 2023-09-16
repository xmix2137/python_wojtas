# Z tabicy o wymiarach 3x3 policz ilość elementów większych od 3
a = [[1,2,3], [4,5,6], [7,8,9]]
licznik = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]>3:
            licznik+=1
            
print(licznik)