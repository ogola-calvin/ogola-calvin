#A binary search  to find a nubmer in sorted dec of cards

#def binary_search(cards, target):

    #for position in range(len(cards)):#linear search if list is not sorted
    #   if cards[position] == target:
        #    return position
    #return -1


#     low = 0
#     high = len(cards) - 1  

#     while low <= high:
#         mid = (low + high) // 2  

#         if cards[mid] == target:
#             return mid  
#         elif cards[mid] < target:
#             high = mid - 1 
#         else:
#             low = mid + 1 

#     return -1 

# cards = [13, 12, 11, 10, 9, 8, 7]  
# target = 2
# result = binary_search(cards, target)

# print(len(cards)) 
# print(result)

#finding the maximum number

def muxNum(numbers2):
    max_num = numbers2[0]

    for j in numbers2:
        if j > max_num:
            max_num = j
        
    return max_num

numbers2 = [9,10,4,56,4]
answer = muxNum(numbers2)

print(answer)
