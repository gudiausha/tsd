Binary search is an efficient algorithm used when you need to find an element or determine its presence in a **sorted array or list**. Here are the key scenarios when binary search is applicable:

### 1. **Sorted Data Structure**
   - **Requirement**: The array or list must be sorted in ascending or descending order. Binary search won't work on unsorted data.
   - **Example**: If you have a list of sorted numbers `[1, 3, 5, 7, 9, 11]` and you need to find if `5` is in the list, binary search is ideal.

### 2. **Large Dataset**
   - **Efficiency**: Binary search is more efficient than linear search (O(n)) for large datasets because it reduces the search space by half each time, operating in **O(log n)** time.
   - **Example**: Searching for a specific name in a telephone directory or a large database.

### 3. **Fast Search Requirement**
   - **Use Case**: When you need quick look-up operations, such as in real-time applications or systems where performance is critical.
   - **Example**: Searching for a word in a dictionary app.

### 4. **Determining Insertion Points**
   - **Use Case**: Binary search can also be used to find the index at which a new element should be inserted to maintain sorted order.
   - **Example**: In a sorted list `[2, 4, 6, 8, 10]`, determining where to insert `7` can be done using binary search.

### 5. **Finding the First or Last Occurrence**
   - **Use Case**: When searching for the first or last occurrence of a duplicate element in a sorted array.
   - **Example**: In a list `[1, 2, 2, 2, 4, 5]`, finding the index of the first or last `2`.

### Summary of When to Use Binary Search:
- The dataset must be sorted.
- The dataset size is significant and linear search would be too slow.
- You need to perform repeated or fast search operations.

If your data is not sorted, binary search is **not applicable**, and you may need to sort it first or use a different search method.

---

When implementing or using binary search, it’s essential to handle various edge cases to ensure the algorithm works correctly across all possible scenarios. Here are some common edge cases to watch out for:

### 1. **Empty Array**
   - **Case**: The array has no elements.
   - **Outcome**: The search should immediately return `-1` or an indication that the target element is not found.
   - **Example**: Searching in `[]`.

### 2. **Single Element Array**
   - **Case**: The array contains only one element.
   - **Outcome**: The algorithm should correctly identify whether the single element matches the target.
   - **Example**: Searching for `5` in `[5]` or searching for `3` in `[5]`.

### 3. **Target Not Present**
   - **Case**: The target element is not present in the array.
   - **Outcome**: The algorithm should return `-1` or an appropriate "not found" indicator.
   - **Example**: Searching for `7` in `[1, 3, 5, 9, 11]`.

### 4. **First or Last Element**
   - **Case**: The target element is at the beginning or end of the array.
   - **Outcome**: The algorithm should correctly identify these positions.
   - **Example**: Searching for `1` in `[1, 3, 5, 7, 9]` or searching for `9` in `[1, 3, 5, 7, 9]`.

### 5. **Duplicate Elements**
   - **Case**: The array contains duplicate elements, and you want to find the first or last occurrence of the target.
   - **Outcome**: Modify the algorithm to continue searching until the first or last instance of the element is found.
   - **Example**: Searching for `2` in `[1, 2, 2, 2, 3, 4]` to return the index of the first `2` or the last `2`.

### 6. **Even/Odd Number of Elements**
   - **Case**: The array has an even or odd number of elements.
   - **Outcome**: Ensure the algorithm correctly handles midpoint calculation, especially in cases where integer division is involved.
   - **Example**: Searching in `[1, 3, 5, 7]` (even) or `[1, 3, 5]` (odd).

### 7. **Array with Negative Numbers**
   - **Case**: The array includes negative numbers, and the target could be negative.
   - **Outcome**: The algorithm should still function correctly as long as the array remains sorted.
   - **Example**: Searching for `-3` in `[-5, -3, -1, 0, 2, 4]`.

### 8. **Target Smaller or Larger Than All Elements**
   - **Case**: The target element is smaller than the smallest element or larger than the largest element in the array.
   - **Outcome**: The search should return `-1` or "not found."
   - **Example**: Searching for `0` in `[1, 3, 5, 7]` or `10` in `[1, 3, 5, 7]`.

### 9. **Integer Overflow in Midpoint Calculation**
   - **Case**: When using `(low + high) / 2`, `low + high` could cause an integer overflow in languages where integers have fixed sizes.
   - **Solution**: Use `low + (high - low) / 2` instead to avoid overflow.

### 10. **Array with Only One Type of Element**
   - **Case**: The array consists of identical elements.
   - **Outcome**: Ensure the algorithm handles this and returns the correct index if the target matches or `-1` if it doesn’t.
   - **Example**: Searching for `3` in `[3, 3, 3, 3]` or `5` in `[3, 3, 3, 3]`.

### 11. **Floating Point Precision**
   - **Case**: When dealing with arrays of floating-point numbers, precision issues may arise.
   - **Outcome**: Ensure appropriate precision handling when comparing values.
   - **Example**: Searching for `3.00001` in `[3.0, 3.00001, 3.00002]`.

### Handling these edge cases ensures that your binary search implementation is robust and works correctly across different scenarios.

---

For non-sorted arrays, the most suitable search algorithm is:

### 1. **Linear Search**
- **How it works**: The algorithm scans each element of the array one by one, from the start to the end, until the target element is found or the array is fully traversed.
- **Time Complexity**: 
  - **Worst-case**: \( O(n) \)
  - **Best-case**: \( O(1) \) (if the target is found at the beginning)
- **Space Complexity**: \( O(1) \) (no extra space is needed)
- **Use case**: Simple to implement and effective for small datasets or when the array is unsorted.

### Other Considerations:
- **Hashing**: If you need faster lookups in an unsorted collection and are willing to use additional space, you can use a hash table (or dictionary) to store elements as keys. This allows:
  - **Average-case time complexity**: \( O(1) \) for lookups.
  - **Space complexity**: \( O(n) \).
  - **Use case**: When you have multiple search operations and can preprocess the data into a hash table.

### Not Suitable for Non-Sorted Arrays:
- **Binary Search**: This requires the array to be sorted beforehand and has a time complexity of \( O(\log n) \). It cannot be applied directly to unsorted arrays.

### Summary:
- For non-sorted arrays, **linear search** is the go-to method due to its simplicity and versatility.
- For more efficient searching with preprocessing, use **hash tables** if additional space is acceptable and repeated searches are needed.

---

Binary and Linear Search Visualizer.: https://www.cs.usfca.edu/~galles/visualization/Search.html