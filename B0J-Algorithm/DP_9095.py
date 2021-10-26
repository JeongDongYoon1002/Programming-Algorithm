def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return solve(n-1) + solve(n-2) + solve(n-3)

n = int(input())
for i in range(n):
    print(solve(int(input())))