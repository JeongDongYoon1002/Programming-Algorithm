Y, X = map(int,input().split())
array = []
for i in range(Y):
    a = list(input())
    array.append(a)
    
row = [0]*Y
column = [0]*X

for i in range(Y):
    for j in range(X):
        if array[i][j] == 'X':
            row[i] = 1
            column[j] = 1

row_count = 0
column_count = 0
for i in range(len(row)):
    if row[i] == 0:
        row_count += 1

for i in range(len(column)):
    if column[i] == 0:
        column_count += 1
print(max(column_count,row_count))