#A function that returns a new list which is reversd

def reversList(numbers):

    revers= []
    

    for  i in  range(len(numbers)-1,-1,-1):
        revers.append(numbers[i])

    return revers    

numbers = [1,2,3,4]    
answer = reversList(numbers)
print(answer)