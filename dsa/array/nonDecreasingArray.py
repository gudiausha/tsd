def isPossible(arr, n):
    # Write your code here.
    out_of_order_ele = []
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            out_of_order_ele.append(arr[i])
    
    if len(out_of_order_ele)>1:
        return False
    else:
        return True