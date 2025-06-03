#linear  and binary serch

def linear_search(numbers, target):

    for p in range(len(numbers)):
        if numbers[p] == target:
            return p
        print(f"index: {p}, value: {numbers[p]}")
    return -1
    



numbers=[4,4,7,8,9]
target = 7    
result = linear_search(numbers, target)


print(result)

#finding the max num

def max_num(numbers1):

    max_value = numbers1[1]
    for i in range(len(numbers1)):
        if i > max_value:
            max_value = i
        print(f"index: {i}, value: {numbers1[i]}")    
    return max_value


numbers1 = [1,2,3,4,5]
answer = max_num(numbers1)


print(answer)

