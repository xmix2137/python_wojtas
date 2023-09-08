rows = 7
columns = 7
start_number = 1

for i in range(1, rows + 1):
    for j in range(columns):
        if j == 0:
            print(start_number, end=' ')
        else:
            print(start_number + j * rows, end=' ')
    print()
    start_number += 1
