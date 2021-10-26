
def solve(n, y, x):
    global result 

    if n == 2 :
        if X == x and Y == y:
            print(result)
            return
        result += 1

        if X == x+1 and Y == y:
            print(result)
            return 
        result +=1

        if Y == y+1 and X == x:
            print(result)
            return
        result += 1

        if X== x+1 and Y == y+1 :
            print(result)
            return
        result += 1
        return

    else:
        solve(n/2, y, x)
        solve(n/2, y, x + n/2)
        solve(n/2, y + n/2, x)
        solve(n/2, y+n/2, x+n/2)

if __name__ == "__main__":
    N, Y, X = map(int,input().split())
    result = 0
    solve(2**N, 0,0)
