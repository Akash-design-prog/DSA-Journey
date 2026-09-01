def recursive_binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        return recursive_binary_search(arr, key, mid+1, high)
    else:
        return recursive_binary_search(arr, key, low, mid-1)

my_array = [12, 3, 23, 8, 16, 2, 42]    
my_array.sort()          

print("Sorted_array: ", my_array)

print("Index of 16: ", recursive_binary_search(my_array, 16, 0, len(my_array) - 1))    
print("Index of 9: ", recursive_binary_search(my_array, 9, 0, len(my_array) - 1)) 