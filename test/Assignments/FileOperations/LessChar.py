def display_words():
    word_list = []
    with open('story.txt', 'r') as file:
        for line in file:
            words = line.lower().split()
            if len(words) < 4:
                word_list.extend(words)
            else:
                print("NO")
    return word_list

value = display_words()
print("Words with less than 4 words in a line:", value)
