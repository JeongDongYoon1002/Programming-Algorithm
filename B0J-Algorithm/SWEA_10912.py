t = int(input())
for i in range(1, t+1):
    word = input()
    stack = []
    for w in word:
        if w in stack:
            stack.remove(w)
        else :
            stack.append(w)
    stack.sort()
    print ("#{} ".format(i),end ='')
    if len(stack) == 0:
        print('Good')
    else:
        for s in stack:
            print(s, end='')
        print()
        