#17.	Create a program that calculates how many times the given letter appears in any text. 
# Then create a program and check how many 
# times the letter ‘e’ appears in the text below. Define a function for making calculations.

def count_letter_occurrences(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count

text_to_analyze = "This is a sample text containing the letter 'e' multiple times."
letter_to_count = 'e'

result = count_letter_occurrences(text_to_analyze, letter_to_count)
print(f"The letter '{letter_to_count}' appears {result} times in the text.")
