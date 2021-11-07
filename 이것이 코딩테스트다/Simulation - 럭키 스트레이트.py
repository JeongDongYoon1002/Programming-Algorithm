data = input()
length = len(data)
left = 0
right = 0

for i in range(len(data)):
    if i < length // 2 :
        left += int(data[i])
    else :
        right += int(data[i])

if(left == right):
    print('LUCKY')
else:
    print('READY')
