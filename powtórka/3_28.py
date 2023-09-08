#28.	Write a program that displays the first fifty words of the Fibonacci sequence. The sequence is defined as follows: 
# the first term is equal to 0, 
# the second is equal to 1, each subsequent term is the sum of the previous two. Sample result below. 

fibonacci_sequence = [0, 1]

for i in range(2, 50):
    next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_term)

for term in fibonacci_sequence:
    print(term, end=' ')