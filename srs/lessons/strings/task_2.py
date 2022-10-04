sentence = input()
max_len=0
max_word=""
words = sentence.split()

for word in words :
    if len(words) > max_len :
        max_word = word
print(max_word)