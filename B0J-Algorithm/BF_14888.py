n = int(input())
nums = list(map(int,input().split()))
add, sub, pro, div = map(int, input().split())



min_, max_ = 1e9, -1e9


def dfs(i, cur, add, sub, pro, div):
    global min_, max_

    if i == n:
        min_ = min(cur, min_)
        max_ = max(cur, max_)
        return

    else:
        if add:
            dfs(i+1,cur+nums[i], add-1, sub, pro, div)
        if sub:
            dfs(i+1,cur-nums[i], add, sub-1, pro, div)
        if pro:
            dfs(i+1,cur*nums[i], add, sub, pro-1, div)
        if div:
            dfs(i+1, int(cur/nums[i]), add, sub, pro, div-1)

dfs(1, nums[0], add,sub,pro,div)

print(max_)
print(min_)