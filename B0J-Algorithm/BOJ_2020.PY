array = list(map(int,input().split()))
a = True
d = True

for i in range(1,8):
    if a[i] > a[i-1]:
        d = False
        
    elif a[i] > a[i+1]:
        a = False
if a :
    print('ascending')
elif d:
    print('decending')
else :
    print('mixed')
    
