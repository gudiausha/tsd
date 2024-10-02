### 1. **Selection Sort**:
- **Time Complexity**: 
  - Best: \(O(n^2)\)
  - Average: \(O(n^2)\)
  - Worst: \(O(n^2)\)
- **Space Complexity**: \(O(1)\) (in-place sorting).
- **Key Features**:
  - Simple but inefficient for large datasets.
  - Inefficient for nearly sorted data since it always scans the entire unsorted portion of the list.
  - **Not stable** (relative order of equal elements may change).

### 2. **Bubble Sort**:
- **Time Complexity**: 
  - Best: \(O(n)\) (with an optimized version that checks if the list is already sorted).
  - Average: \(O(n^2)\)
  - Worst: \(O(n^2)\)
- **Space Complexity**: \(O(1)\) (in-place).
- **Key Features**:
  - Simple, but inefficient for large datasets, similar to selection sort.
  - Better than selection sort in the best case when the array is already sorted.
  - **Stable** (maintains the relative order of equal elements).

### 3. **Insertion Sort**:
- **Time Complexity**:
  - Best: \(O(n)\) (if the list is already nearly sorted).
  - Average: \(O(n^2)\)
  - Worst: \(O(n^2)\)
- **Space Complexity**: \(O(1)\) (in-place).
- **Key Features**:
  - Works well with nearly sorted data and is efficient for small datasets.
  - **Stable**.
  - More efficient than selection sort and bubble sort in practice, especially for nearly sorted data due to its best-case time complexity of \(O(n)\).

### 4. **Merge Sort**:
- **Time Complexity**:
  - Best: \(O(n \log n)\)
  - Average: \(O(n \log n)\)
  - Worst: \(O(n \log n)\)
- **Space Complexity**: \(O(n)\) (not in-place due to auxiliary space for merging).
- **Key Features**:
  - **Stable**.
  - Efficient for large datasets.
  - Requires extra space, so not space-efficient for very large datasets or memory-constrained environments.
  - Used in scenarios where stability is important.

### 5. **Quick Sort**:
- **Time Complexity**:
  - Best: \(O(n \log n)\)
  - Average: \(O(n \log n)\)
  - Worst: \(O(n^2)\) (if the pivot is consistently chosen poorly, e.g., always the smallest or largest element).
- **Space Complexity**: \(O(\log n)\) (in-place, but the recursion stack uses space).
- **Key Features**:
  - Efficient and widely used in practice due to its average time complexity of \(O(n \log n)\).
  - **Not stable** (relative order of equal elements may change).
  - For large, random data sets, quick sort is often the fastest in practice.
  - Sorting in-place means it is more space-efficient than merge sort.

### 6. **Heap Sort**:
- **Time Complexity**:
  - Best: \(O(n \log n)\)
  - Average: \(O(n \log n)\)
  - Worst: \(O(n \log n)\)
- **Space Complexity**: \(O(1)\) (in-place).
- **Key Features**:
  - **Not stable**.
  - Time complexity is always \(O(n \log n)\), making it more predictable than quicksort.
  - Typically slower than quicksort in practice due to the overhead of maintaining the heap.
  - Useful in environments with memory constraints.

---

### Summary of Differences:

1. **Time Complexity**:
   - **Selection Sort**: \(O(n^2)\) in all cases, which is worse than algorithms like **Merge Sort**, **Quick Sort**, and **Heap Sort** with \(O(n \log n)\) on average and in the worst case.
   - **Insertion Sort** and **Bubble Sort** have the same worst-case complexity as selection sort but perform better in specific scenarios (e.g., nearly sorted data).

2. **Space Complexity**:
   - **Selection Sort** is as space-efficient as **Bubble Sort**, **Insertion Sort**, and **Heap Sort** with \(O(1)\) space.
   - **Merge Sort** requires \(O(n)\) extra space, while **Quick Sort** has a space complexity of \(O(\log n)\) due to recursion.

3. **Stability**:
   - **Selection Sort** and **Quick Sort** are **not stable**.
   - **Bubble Sort**, **Insertion Sort**, and **Merge Sort** are **stable**.

4. **Use Cases**:
   - **Selection Sort** is mainly used when memory space is very limited, or in educational contexts for learning.
   - **Quick Sort** is often the go-to for large, random datasets due to its average \(O(n \log n)\) time complexity and in-place sorting.
   - **Merge Sort** is preferred for data that requires stability or when you can afford the extra space overhead.
   - **Insertion Sort** and **Bubble Sort** are useful for small or nearly sorted datasets.

When we say that **Selection Sort is unstable** and **Bubble Sort is stable**, we are referring to the concept of **stability in sorting algorithms**. 

### Definition of Stability in Sorting Algorithms:
A **stable sorting algorithm** maintains the **relative order** of records with **equal keys** (values). In other words, if two elements have the same value, a stable sorting algorithm will preserve their original relative order from the input list after sorting.

### Stability of Bubble Sort:
- **Bubble Sort is stable** because it compares adjacent elements and only swaps them if necessary. 
- If two elements are equal, Bubble Sort **does not swap** them, which means their **relative order is preserved**.
  
  **Example**:
  ```python
  A = [(1, 'A'), (3, 'B'), (3, 'C'), (2, 'D')]
  ```
  - After sorting by the first element of the tuple (the number), Bubble Sort will give:
    ```python
    [(1, 'A'), (2, 'D'), (3, 'B'), (3, 'C')]
    ```
  - The relative order of the two `3`s, `(3, 'B')` and `(3, 'C')`, is preserved.

### Instability of Selection Sort:
- **Selection Sort is unstable** because it may swap elements that have equal values but are in different original positions. 
- During the selection process, it picks the minimum element and swaps it with the element at the beginning of the unsorted portion. If there are two equal elements and one appears earlier in the list, Selection Sort may swap them, disrupting their **relative order**.
  
  **Example**:
  ```python
  A = [(1, 'A'), (3, 'B'), (3, 'C'), (2, 'D')]
  ```
  - During Selection Sort, when it swaps the minimum element, it might choose to swap one of the `3`s (depending on how the algorithm is written), and the original relative order of `(3, 'B')` and `(3, 'C')` may not be preserved.
  - The result could look like:
    ```python
    [(1, 'A'), (2, 'D'), (3, 'C'), (3, 'B')]  # The order of the '3's changed.
    ```
  - The relative order of `(3, 'B')` and `(3, 'C')` is **not preserved**, so Selection Sort is considered **unstable**.

### Why Does Stability Matter?
- Stability is important in scenarios where elements have multiple fields and are sorted based on one of the fields while keeping the relative order intact for elements that are equal.
- For example, in **multi-key sorting**, such as sorting a list of students first by their scores and then by their names, stable sorting ensures that the original order of names (if the scores are the same) remains unchanged.

### Summary:
- **Bubble Sort is stable**: Equal elements retain their original relative order.
- **Selection Sort is unstable**: Equal elements might not retain their relative order after sorting.

### Key Reasons Why Bubble Sort is Rarely Used:

1. **Inefficient Time Complexity**:
   - **Worst-case and average-case time complexity**: \(O(n^2)\).
   - Even in the best case (with the optimized version), it still only achieves \(O(n)\), which is great for nearly sorted arrays, but in most cases, it’s still much slower than algorithms like **Quick Sort**, **Merge Sort**, or **Heap Sort**, which have average and worst-case time complexities of \(O(n \log n)\).
   - For large datasets, quadratic time complexity becomes impractical because the number of comparisons and swaps grows exponentially with the size of the input.

2. **Large Number of Comparisons and Swaps**:
   - Bubble Sort performs many unnecessary comparisons and swaps, even when elements are only slightly out of order.
   - Algorithms like **Quick Sort** or **Merge Sort** use divide-and-conquer techniques to sort more efficiently by splitting the problem into smaller subproblems.

3. **No Real Advantage Over Other Simple Sorting Algorithms**:
   - **Selection Sort** and **Insertion Sort**, which also have \(O(n^2)\) time complexity, are generally preferred over Bubble Sort. 
     - **Insertion Sort** is more efficient on small datasets and **nearly sorted lists**, as it requires fewer swaps and comparisons in many cases.
     - **Selection Sort** performs fewer swaps overall, which can be advantageous in some situations.
   - These algorithms are still used in specific scenarios but are generally faster and more efficient than Bubble Sort for small or moderately sized datasets.

4. **Lack of Scalability**:
   - For **large datasets**, the performance gap between Bubble Sort (\(O(n^2)\)) and more advanced algorithms (\(O(n \log n)\)) becomes significant.
   - Algorithms like **Merge Sort** and **Quick Sort** scale much better as the input size increases, making them suitable for large datasets.

5. **Minimal Practical Use Cases**:
   - Bubble Sort is often used for **educational purposes** to help beginners understand sorting algorithms and concepts like swapping and comparing elements.
   - In practice, **Bubble Sort** is rarely used because faster and more efficient sorting algorithms exist, which are better suited for both small and large datasets.

### Summary of Inefficiency:
- **Bubble Sort** is inefficient for large datasets due to its \(O(n^2)\) time complexity and the large number of comparisons and swaps it requires.
- In contrast, algorithms with \(O(n \log n)\) complexity, like **Merge Sort** and **Quick Sort**, are much faster and scale better for real-world use cases.

