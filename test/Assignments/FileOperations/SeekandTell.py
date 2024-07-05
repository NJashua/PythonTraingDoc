def get_chars():
    with open('story.txt', 'r') as file:
        file.seek(3)
        position = file.tell()
        char = file.read(position)
        return position, char

position, char = get_chars()
print(f"Position: {position} char is {char}")