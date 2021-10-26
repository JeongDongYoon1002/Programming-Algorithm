n, m = map(int, input().split())
listen = []
see = []
result = []
# 입력
for i in range(n):
    a = input()
    listen.append(a)

for i in range(m):
    a = input()
    see.append(a)

listen.sort()

def binary_search(array, target, start, end):
    global result 
    if start > end :
        return 0

    mid = (start+end)//2
    if array[mid] == target:
        result.append(array[mid])

    if array[mid] > target :
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid+1, end)


for i in see:
    binary_search(listen, i, 0, n-1)
result.sort()
print(len(result))
for i in result:
    print(i)


