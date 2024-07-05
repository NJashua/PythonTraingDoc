def get_text():
    file = open('poem.txt', 'w')
    get_result = file.writelines("james")
    print(get_result)

get_text()