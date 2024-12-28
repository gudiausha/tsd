def InsertionSort(A: list) -> list:
    """
    Sorts a list A using the insertion sort algorithm.
    """
    if len(A) < 2:
        return A  # Handle edge case for empty or single-element list
    
    for i in range (1,len(A)):
        j = i
        while (j>0 and A[j-1]>A[j]):
            A[j],A[j-1] = A[j-1],A[j]
            j-=1
    return A

if __name__ == "__main__":
    A = [13, 46, 24, 52, 20, 9]
    output = InsertionSort(A)
    print(output)
