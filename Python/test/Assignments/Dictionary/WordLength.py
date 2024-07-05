# 1)Write a program that reads string from user. Your program should create a dictionary having key as word length and value is count of words of that length. For example, if user enters 'A fat cat is on the mat'.

# Word	Word length
# A	1
# fat	3
# cat	3
# is	2
# on	2
# the	3
# mat	3
# The content of dictionary should be {1:1, 3:4, 2:2}

word_sentence = input("Enter a sentence: ").split()

result_dict = {}
for word in word_sentence:
    if len(word) in result_dict:
        result_dict[len(word)] += 1
    else:
        result_dict[len(word)]=1 

for i,j in result_dict.items():
    print("The set of word length is: ", i ,":",j)
