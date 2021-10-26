import numpy as np
import pandas as pd

num = int(input())
data = [int(x) for x in input().split()]
total = 0
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i] > data [j] :
            temp = data[j]
            data[j] = data[i]
            data[i] = temp
for i in range(len(data)-1):
    j = i+1
    data[j] = data[i]+data[j]
    
print(sum(data))
        