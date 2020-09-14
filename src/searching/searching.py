def linear_search(arr, target):
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:
        midpoint = (left+right)//2

        if arr[midpoint] == target:
            return midpoint
        
        elif arr[midpoint] > target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    


    return -1  # not found
