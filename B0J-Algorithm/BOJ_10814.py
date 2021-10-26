test_case = int(input())
info = []
for t in range(test_case):
    age, name = input().split()
    info.append((int(age),name))

info = sorted(info, key = lambda x:x[0])
for i in info:
    print(i[0], i[1])




   
    
        
    

    

    
