# 5. Write a program that input a string and ask user to delete a given word from a string.

sentence = input("Enter a string sentence: ")
word = input("Enter a word to delete: ")
if word in sentence:
    words = sentence.split()
    value =  words.remove(word)
    new_sentence = ' '.join(words)
    print(f"The word {word} is deleted in this sentence {sentence}")
    print(new_sentence)
else:
    print(f"The word{word} is not found in sentence {sentence}")