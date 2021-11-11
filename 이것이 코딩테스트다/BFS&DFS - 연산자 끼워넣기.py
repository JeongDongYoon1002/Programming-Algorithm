n = int(input())
data = list(map(int,input().split()))
add, sub, pro, div = map(int,input().split())


max_value, min_value = -1e9, 1e9

def dfs(index, total):
    global max_value, min_value, add, sub, pro, div 
    
    if index == n:
        min_value = min(min_value, total)
        max_value = max(max_value, total)

    else:
        if add > 0:
            add -= 1
            dfs(index+1, total + data[index])
            add += 1
            
        if sub > 0:
            sub -= 1
            dfs(index+1, total - data[index])
            sub += 1
            
        if pro > 0 :
            pro -=1
            dfs(index+1, total*data[index])
            pro += 1
            
        if div > 0:
            div -= 1
            dfs(index+1, int(total / data[index]))
            div += 1
            
dfs(1, data[0])

print(min_value, max_value)
                
