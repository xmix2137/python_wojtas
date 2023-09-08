#31.	Write a program that displays 20 integer random numbers in the range of 5 to 10.

import random

for _ in range(20):
    random_num = random.randint(5, 10)
    print(random_num, end=' ')