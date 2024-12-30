def SelectionSort(A: list) -> list:
    """
    Sorts a list A using the selection sort algorithm.
    """
    if len(A) < 2:
        return A  # Handle edge case for empty or single-element list

    for i in range(len(A) - 1):  # Optimize to len(A) - 1
        temp_min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[temp_min]:
                temp_min = j
        if temp_min != i:  # Avoid unnecessary swaps
            A[i], A[temp_min] = A[temp_min], A[i]
    return A

if __name__ == "__main__":
    A = [13, 46, 24, 52, 20, 9]
    output = SelectionSort(A)
    print(output)
