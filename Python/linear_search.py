def linear_search(arr, key):
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
    return -1

my_array = [12, 3, 23, 8, 16, 2, 42]

print("Index of 16: ", linear_search(my_array, 16))

