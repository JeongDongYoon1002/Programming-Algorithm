def solve(array):
    now = array[0]
    result = 1
    for i in range(1, len(array)):
        if now < array[i]:
            result += 1
            now = array[i]
    return result
test_case = int(input())
array = []
for t in range(test_case):
    array.append(int(input()))

print(solve(array))
array.reverse()
print(solve(array))