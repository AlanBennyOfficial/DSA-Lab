lst = [1,2,3,56,89,456,786,1546]
lst.sort()  # Ensure the list is sorted

def BinSearch(target, lst):
    high = len(lst)-1
    low = 0
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        
        if lst[mid] == target:
            return mid
        
        elif lst[mid] < target:
            low = mid + 1
            
        else:
            high = mid - 1
    
    return -1

target = 456

result = BinSearch(target, lst)

if result != -1:
    print("Element is present at index", result)
    print(lst[result])
else:
    print("Element is not present in array")
