from os import *
from sys import *
from collections import *
from math import *



def minElementsToRemove(arr):

    # Write your Code here.
    arr_len = len(arr)
    unique_arr = set(arr)
    uni_arr_len = len(unique_arr)
    min_elements_to_remove = arr_len - uni_arr_len
    
	return min_elements_to_remove
