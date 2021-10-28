def get_distance(current, future):
    db ={'1':(0,0),'2':(0,1),'3':(0,2),
         '4':(1,0),'5':(1,1),'6':(1,2),
         '7':(2,0),'8':(2,1),'9':(2,2),
         '*':(3,0),'0':(3,1),'#':(3,2)}
    c_x, c_y = db[current]
    f_x, f_y = db[future]
    return (abs(c_x - f_x) + abs(c_y - f_y))

def solution(numbers,hand):
    root = ''
    left, right = '*', '#'
    for i in numbers:
        if i in [1,4,7]:
            root += 'L'
            left = str(i)
        elif i in [3,6,9]:
            root += 'R'
            right = str(i)
        elif i in [2,5,8,0]:
            d_left = get_distance(left,str(i))
            d_right = get_distance(right,str(i))
            
            if d_left > d_right:
                root += 'R'
                right = str(i)
            elif d_left < d_right:
                root += 'L'
                left = str(i)
            elif d_left == d_right:
                if hand =='left':
                    root += 'L'
                    left = str(i)
                else:
                    root += 'R'
                    right = str(i)

    return root
