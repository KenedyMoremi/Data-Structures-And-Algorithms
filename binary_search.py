#This function accepts a sorted list and returns the index of the item to search, returns -1 if not found
def binary_search(list, item_to_search, left, right):

    if left >= right or right <= 0:
        return -1


    mid = (right + left) // 2   #middle index
    mid_value = list[mid]       #middle value

    if item_to_search == mid_value:
        return mid
    
    if item_to_search < mid_value:
        right = mid
    
    else:
        left = mid + 1
    
    return binary_search(list, item_to_search, left, right)
    
