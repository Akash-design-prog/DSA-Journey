#Defining a function for binary search
def binary_search (arr, key): #Two arguements one is the array another is what I want to find or like check it with
    low = 0                   #The first pointer  
    high = len(arr) - 1       #The last pointer

    while low <= high:
        mid = (low + high) // 2  #Using // as I want in integer whole number

        #When key is in the array
        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1                    #If no key found in the array 

#Taking some example
my_array = [12, 3, 23, 8, 16, 2, 42]    #Need to sort as binary search could only be done in sorted
my_array.sort()          #Used sorting method instead of "Sorted" function as it'll have space complexity as O(n) and here sort() has the space complexity of O(1)

print("Sorted_array: ", my_array)

print("Index of 16: ", binary_search(my_array, 16))    #Give index 4
print("Index of 9: ", binary_search(my_array, 9))      #Returns -1