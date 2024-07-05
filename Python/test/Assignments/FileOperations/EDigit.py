def last_digit_words():
    count = 0
    with open('notes.txt', 'r') as file:
        for line in file:
            words = line.lower().split()
            last_word = words[-1]
            print(last_word)
            if last_word[-1].isdigit():
                count += 1
    return count

value = last_digit_words()
print("Number of lines with a digit as part of the last word:", value)
