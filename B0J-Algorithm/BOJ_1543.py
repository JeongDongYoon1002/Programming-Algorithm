document = input()
word = input()
index = 0
cnt = 0

while len(document) - index >= len(word):
    if document[index:index + len(word)] == word:
        cnt += 1
        index += len(word)
    else:
        index += 1

print(cnt)
