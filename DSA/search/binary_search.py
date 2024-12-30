'''
Binary Search : Divide and Conquer Strategy
'''

def binary_search_iterative(input_arr,target):
    '''
    Time Complexity:
        Best : O(1) - Mid element is the target
        Worst : O(log n)

    Space Complexity:
        O(1)
    '''

    # If array is empty no need to check, return -1
    if len(input_arr) == 0:
        return -1
    
    # Initialize the state of the indexes that correspond to the first and last available indexes in the array.
    low = 0
    high = len(input_arr)-1
    
    # Iterate through the elements while the indexes are within the possible range
    while low <= high:

        # Get the middle position of the array
        # Python does not lead to overflow issues in case of large integers. In other languages this issue is present.
        # Hence mid must be calculated as below instead of mid = (low+high)//2
        mid = low + (high - low) // 2

        # Test if the middle element is the target value (best case scenario)
        if target == input_arr[mid]:
            return mid
        
        # Is the target to the left of the current element
        elif target < input_arr[mid]:
            # Because the element is of the left we want the sub-array on the left.
            # The firstElement is the same (0) but the last element is on the position before the middle element.
            # The middle element is excluded because we already checked if it was our target value and it can be discarded.
            high = mid-1
        
        # Is the target to the right of the current element
        else:
            # Because the element is on the right we want the sub-array on the right.
            # The lastElement is the same, but the firstElement is now the one whose position is after the middle element.
            # The middle element is excluded because we already checked if it was our target value and it can be discarded.
            low = mid+1

    # If the last element position is zero or less it means that the element was not
    # found or that the array as no values, so we can return -1 to indicate a negative match for the
    # target value
    return -1

def binary_search_recursive(input_arr,low,high,target):
    '''
    Time Complexity:
        Best : O(1) - Mid element is the target
        Worst : O(log n)

    Space Complexity:
        - O(log n) - Each recursive call adds a frame to the call stack
    '''
    # If array is empty no need to check, return -1
    if len(input_arr) == 0:
        return -1

    # If one of the indexes is in a situation like 0 < -1 or n < (n - 1) that means
    # the array does not contain the target value
    if low > high:
        return -1

    # Get the middle position of the array
    mid = low + (high - low) // 2

    # Test if the middle element is the target value (best case scenario)
    if target == input_arr[mid]:
        return mid

    elif target < input_arr[mid]:
        # The target is smaller than the current element, then the target value must be on the left
        return binary_search_recursive(input_arr,low,mid-1,target)

    else:
        # The target value is bigger than the current element, then the target value must be on the right
        return binary_search_recursive(input_arr,mid+1,high,target)        

if __name__ == "__main__":
    # A = [9,13, 20, 24, 46, 52]
    A = []
    target = 95
    # output = binary_search_iterative(A,target)
    low = 0
    high = len(A)-1
    output = binary_search_recursive(A,low,high,target)
    print(output)