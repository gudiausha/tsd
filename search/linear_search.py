'''
Linear Search.: Iterate thro' array to find the element. Not necessary that arr must be sorted.
'''

def linear_search(input_arr,target):
    '''
    Time Complexity:
        Best : O(1) - Target is first element in array
        Worst : O(n) _ Target is last ele or not found
    Space Complexity:
        O(1)
    '''
    for ind in range(0,len(input_arr)):
        if input_arr[ind] == target:
            return [ind]
    return -1


if __name__ == "__main__":
    # A = [13, 46, 24, 52, 20, 9]
    A = []
    target = 40
    output = linear_search(A,target)
    print(output)

