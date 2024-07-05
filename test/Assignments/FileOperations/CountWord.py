def get_count():
    count = 0
    with open(r"C:\Users\1038588\OneDrive - Blue Yonder\Desktop\test\notes.txt", 'r') as file:
        for line in file.readlines():
            if 'the' in line:
                words = line.lower().split()
                count += words.count('the')
            else:
                ("Velli aaduko amma")
    return count 
value = get_count()
print("The no.of count for the is: ",value)