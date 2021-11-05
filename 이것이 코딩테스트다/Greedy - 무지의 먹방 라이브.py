import  heapq
def solution(food_times, k):
    if sum(food_times) <= k :
        return -1
    
    q = [] 
    
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1))
        
    sum_value = 0 # 먹기 위해 사용한 시간
    pre = 0 # 직전에 다먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수 
    
    while sum_value + ((q[0][0]-pre) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - pre)*length 
        length -= 1
        pre = now 
        
    result = sorted(q, key = lambda x:x[1])
    return result[(k - sum_value) % length][1]
