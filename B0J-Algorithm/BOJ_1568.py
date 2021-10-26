bird = int(input())
time = 0
temp = 1
while bird > 0:

    if bird < temp :
        temp = 1
    bird = bird - temp
    time += 1
    temp += 1
       

print(time)