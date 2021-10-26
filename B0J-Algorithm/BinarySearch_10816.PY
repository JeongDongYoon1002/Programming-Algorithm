from collections import Counter

N = int(input())
lst = sorted(list(map(int, input().split()))) # 정렬 
M = int(input())
card = list(map(int, input().split()))


dic = {}

for n in lst:
    if n in dic: # 딕셔너리에 있으면
        dic[n] += 1
    else: # 딕셔너리에 없으면
        dic[n] = 1

print(dic)


print(' '.join(str(dic[c]) if c in dic else '0' for c in card))