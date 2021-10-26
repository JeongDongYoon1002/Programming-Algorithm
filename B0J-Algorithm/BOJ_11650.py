test_case = int(input())
array = []
for t in range(test_case):
    x, y = map(int,input().split())
    array.append([x,y])

array.sort()
for a in array:
    print(a[0], a[1])
