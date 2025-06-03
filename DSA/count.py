#A program that counts how many times a number has appear

def appear(num,target):

    times = 0

    for i in num:
        if i == target:
            times = times + 1

    return times

num = [1,2,2,2,4,4,5] 
target = 5

answer = appear(num,target)       

print(answer)