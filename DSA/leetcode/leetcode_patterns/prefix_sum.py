'''
Prefix Sum involves preprocessing an array to create a new array 
where each element at index i represents the sum of the array from the start up to i. 
This allows for efficient sum queries on subarrays.

Use this pattern when you need to perform multiple sum queries on a subarray or need to calculate cumulative sums.
'''

def prefix_sum(input_arr):
    prefix_sum = []
    sum =0
    for i in input_arr:
        sum+=i
        prefix_sum.append(sum)
    return prefix_sum

input_arr = [1,2,3,4,5,6]
prefix_sum_output = prefix_sum(input_arr)

print(prefix_sum_output)

def prefix_sum_with_queries(input_arr):
    prefix_sums = {0: 0}  # Prefix sums map
    current_sum = 0
    for i, num in enumerate(input_arr):
        current_sum += num
        prefix_sums[i + 1] = current_sum
    return prefix_sums

input_arr = [1,2,3,4,5,6]
prefix_sum_output = prefix_sum_with_queries(input_arr)

print(prefix_sum_output)