#A binary search  to find a nubmer in sorted dec of cards

def binary_search(cards, target):

    #for position in range(len(cards)):#linear search if list is not sorted
    #   if cards[position] == target:
        #    return position
    #return -1


    low = 0
    high = len(cards) - 1  

    while low <= high:
        mid = (low + high) // 2  

        if cards[mid] == target:
            return mid  
        elif cards[mid] < target:
            high = mid - 1 
        else:
            low = mid + 1 

    return -1 

cards = [13, 12, 11, 10, 9, 8, 7]  
target = 2
result = binary_search(cards, target)

print(len(cards)) 
print(result) 
















cards = [13,12,11,10,9,8,7]
target = 7
results = binary_search(cards, target)

print(len(cards))
print(results)