def get_upper(s):
    uppper_word = []
    for word in s.split():
        if word.lower:
            uppper_word.append(word.upper())
        else:
            print("BYe")
    return uppper_word

sentence = input("Enter a list of words in lowercase: ")
result = get_upper(sentence)
print(result)