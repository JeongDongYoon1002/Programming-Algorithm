import copy
def solve(array, n):
    if len(array) == n:
        operator_list.append(copy.deepcopy(array))
        # 재귀로 append 할때는 deppcopy 써야한다.
        return 
    array.append(' ')
    solve(array, n)
    array.pop()

    array.append('+')
    solve(array, n)
    array.pop()

    array.append('-')
    solve(array, n)
    array.pop()



test_case = int(input())
for t in range(test_case):
    n = int(input())
    operator_list = []
    solve([], n-1)

    integers = [i for i in range(1, n+1)]

    for op in operator_list:
        string = ""
        for i in range(n-1):
            string = string + str(integers[i]) + op[i]
        string += str(integers[-1])

        if eval(string.replace(" ","")) == 0:
            print(string)
        
        

'''
import copy
def solve(array, n):
    if len(array) == n:
        operator_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    solve(array, n)
    array.pop()

    array.append('+')
    solve(array, n)
    array.pop()

    array.append('-')
    solve(array, n)
    array.pop()


test_case = int(input())
for _ in range(test_case):
    n = int(input())
    operator_list = []
    solve([], n-1)

    integer = [i for i in range(1, n+1)]

    print(operator_list)
'''
    

