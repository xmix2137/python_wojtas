#27.	A computer numeric keyboard has the arrangement of the keys as below. The included program code displays the computer keyboard. 
# Analyse the program in terms of the displayed results. 
# Do you understand each program statement? Then make a change in your program code. 
# Replace the ‘for’ with a ‘while’ statement.

i = 6
while i >= 0:
    for j in range(1, 4):
        print(f' {i+j}', end='')
    print()
    i -= 3
