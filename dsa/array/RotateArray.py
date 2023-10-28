def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    sliced_list = arr[:k]
    del arr[:k]
    arr.extend(sliced_list)
    return arr