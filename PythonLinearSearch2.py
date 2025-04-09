L = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target_value = 28

low = 0
high = len(L) - 1

while low <= high:
    mid = (low + high) // 2
    if L[mid] == target_value:
        print("Found at index:", mid)
        break
    elif L[mid] < target_value:
        low = mid + 1
    else:
        high = mid - 1
if low > high:
    mid = -1
    print(mid, "\n","Item not in list")
    

    
