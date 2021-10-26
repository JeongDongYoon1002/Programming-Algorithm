# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

n = int(input())

dp = [0]*(n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1]+1

    if n%3 == 0:
        temp = dp[i//3] + 1
        dp[i] = min(temp, dp[i])

    if n%2 == 0:
        temp = dp[i//2] + 1
        dp[i] = min(temp, dp[i])

print(dp[n])