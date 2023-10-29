#Brute Force Method - O(2N) = O(N)
def firstMissing(arr, n):
    # Write your function here.
    b = []
    # arr.sort()
    if all(val<0 for val in arr):
        b.append(1)
    else:
        for i in range(1,max(arr)+2):
            if i not in arr:
                b.append(i)
                break 
    return min(b)