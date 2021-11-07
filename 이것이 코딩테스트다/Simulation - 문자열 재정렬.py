data = input()
word = []
total = 0
for i in range(len(data)):
    if 'A' <= data[i] and data[i] <= 'Z':
        word.append(data[i])
    else:
        total += int(data[i])

word.sort()
word.append(total)


for d in word :
    print(d, end='')
