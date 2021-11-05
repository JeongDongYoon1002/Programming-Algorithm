from itertools import combinations

n, m = map(int,input().split()) # 볼링공 개수, m 무게 

data = list(map(int,input().split()))

duple = 0
for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        if data[i] == data[j]:
            duple += 1

list(combinations(data, 2))

print(len(list(combinations(data,2)))  - duple )

