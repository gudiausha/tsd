def BubbleSort(A: list) -> list:
    """
    Sorts a list A using the bubble sort algorithm with an optimization
    to stop early if the array becomes sorted.
    """
    if len(A) < 2:
        return A  # Handle edge case for empty or single-element list
    
    for i in range (len(A)-1,-1,-1):
        swapped=False
        for j in range(0,i):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                swapped = True
        if not swapped:
            return A
    return A

if __name__ == "__main__":
    A = [13, 46, 24, 52, 20, 9]
    # A = [5, 10, 15, 20, 25] --> Input for Optimized Bubble Sort
    # A = [5, 10, 15, 30, 20, 25] --> Partially sorted input
    output = BubbleSort(A)
    print(output)
