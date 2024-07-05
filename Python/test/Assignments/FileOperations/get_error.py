def get_count():
    count = 0
    with open(r'poem.txt', 'r') as file:
        for line in file:
            print(line)
            if line[0] == "T":
                print("Escape")
            else:
                count += 1
    return count

value = get_count()
print(value)