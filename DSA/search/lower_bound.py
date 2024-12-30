"""
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.
"""

def ImplementLowerBound(arr):
    '''
    What is Lower Bound?
    The lower bound algorithm finds the first or the smallest index in a sorted array 
    where the value at that index is greater than or equal to a given key i.e. x.

    The lower bound is the smallest index, ind, where arr[ind] >= x. 
    But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.
    '''

    lower_bound = arr[0]
    upper_bound = len(arr)-1
    mid = (lower_bound + (upper_bound-lower_bound))//2

    while lower_bound>upper_bound: