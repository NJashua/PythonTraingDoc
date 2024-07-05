vowels_list = 'aeiou'
vowels = []
consonants = []
def get_vow_cons(words):
    for i in words:
        if i in vowels_list:
            vowels.append(i)
        else:
            consonants.append(i)
    return vowels, consonants
sentence = input("Enter sentence: ")
value = get_vow_cons(sentence)
for i in value:
    print(i)