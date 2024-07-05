# 7)write a program to display and count unique vowels present in the given word.
#   using list
#   Input: blueyondersoftwaresolutions
#     output: u e a i o =>5


input_val = input("Enter a word: ").lower()
vowels = "aeiou"
unique_vowels = []

for char in input_val:
    if char in vowels and char not in unique_vowels:
        unique_vowels.append(char)

print("Unique vowels:", ' '.join(unique_vowels))
print("Number of unique vowels:", len(unique_vowels))
