# Sorting Algorithms 


## 1. Bubble Sort
### Overview:
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

### Use Case:
Bubble Sort is suitable for small datasets or nearly sorted datasets. It is not recommended for large datasets due to its O(n^2) time complexity.

### Characteristics:
- **Stability:** Bubble Sort is stable.
- **In-Place:** Yes.
- **Real-world Example:** Educational purposes or small datasets.

### Time and Space Complexity:
- Time Complexity: O(n^2)
- Space Complexity: O(1)

## 2. Selection Sort
### Overview:
Selection Sort divides the input list into a sorted and an unsorted region. It repeatedly selects the minimum element from the unsorted region and swaps it with the first element of the unsorted region.

### Use Case:
Selection Sort is suitable for small datasets or when the cost of swapping elements is less than comparisons. It has O(n^2) time complexity.

### Characteristics:
- **Stability:** Not stable.
- **In-Place:** Yes.
- **Real-world Example:** When memory writes are costly.

### Time and Space Complexity:
- Time Complexity: O(n^2)
- Space Complexity: O(1)

## 3. Insertion Sort
### Overview:
Insertion Sort builds a sorted array one element at a time by repeatedly taking an element from the unsorted part and inserting it into its correct position in the sorted part.

### Use Case:
Insertion Sort is efficient for small datasets or nearly sorted datasets. It works well for online algorithms where elements are coming one by one.

### Characteristics:
- **Stability:** Stable.
- **In-Place:** Yes.
- **Real-world Example:** When the dataset is partially ordered.

### Time and Space Complexity:
- Time Complexity: O(n^2)
- Space Complexity: O(1)

## 4. Merge Sort
### Overview:
Merge Sort is a divide-and-conquer algorithm that recursively divides the array into halves, sorts them, and then merges the sorted halves.

### Use Case:
Merge Sort is suitable for large datasets and provides stable sorting. It has a consistent O(n log n) time complexity.

### Characteristics:
- **Stability:** Stable.
- **In-Place:** No (requires additional space for merging).
- **Real-world Example:** External sorting, where data doesn’t fit into memory.

### Time and Space Complexity:
- Time Complexity: O(n log n)
- Space Complexity: O(n)

## 5. Quick Sort
### Overview:
Quick Sort is a divide-and-conquer algorithm that selects a "pivot" element and partitions the array into two sub-arrays according to the pivot. It then recursively sorts the sub-arrays.

### Use Case:
Quick Sort is efficient for large datasets and is widely used in practice. It has an average-case time complexity of O(n log n).

### Characteristics:
- **Stability:** Not stable.
- **In-Place:** Yes.
- **Real-world Example:** General-purpose sorting.

### Time and Space Complexity:
- Time Complexity: O(n^2) in worst case, O(n log n) on average
- Space Complexity: O(log n) on average

## 6. Cycle Sort
### Overview:
Cycle Sort is an in-place, non-comparing sorting algorithm that works by rotating elements in different cycles.

### Use Case:
Cycle Sort is suitable when memory writes are costly and for situations where the number of writes needs to be minimized.

### Characteristics:
- **Stability:** Not stable.
- **In-Place:** Yes.
- **Real-world Example:** When minimizing the number of memory writes is crucial.

### Time and Space Complexity:
- Time Complexity: O(n^2)
- Space Complexity: O(1)

## 7. Heap Sort
### Overview:
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to build a heap and extract the maximum element repeatedly.

### Use Case:
Heap Sort is suitable for scenarios where a stable sort is not a priority, and an in-place sort with O(n log n) time complexity is needed.

### Characteristics:
- **Stability:** Not stable.
- **In-Place:** Yes.
- **Real-world Example:** Priority queue implementations.

### Time and Space Complexity:
- Time Complexity: O(n log n)
- Space Complexity: O(1)

## 8. Counting Sort
### Overview:
Counting Sort is a non-comparing sorting algorithm that uses an auxiliary array to count the occurrences of each element and then reconstructs the sorted array.

### Use Case:
Counting Sort is effective for sorting integers when the range of possible values is known and not too large.

### Characteristics:
- **Stability:** Stable.
- **In-Place:** No (requires additional space for counting).
- **Real-world Example:** Sorting grades of students in a class.

### Time and Space Complexity:
- Time Complexity: O(n + k), where k is the range of input values.
- Space Complexity: O(k)

## 9. Radix Sort
### Overview:
Radix Sort is a non-comparing sorting algorithm that distributes elements into buckets according to their digits.

### Use Case:
Radix Sort is suitable for sorting integers or strings with fixed-length keys.

### Characteristics:
- **Stability:** Stable.
- **In-Place:** No (requires additional space for buckets).
- **Real-world Example:** Sorting phone numbers based on area code.

### Time and Space Complexity:
- Time Complexity: O(d * (n + k)), where d is the number of digits.
- Space Complexity: O(n + k)

## 10. Bucket Sort
### Overview:
Bucket Sort divides the input into a fixed number of equally spaced ranges, or "buckets," and then individually sorts each bucket.

### Use Case:
Bucket Sort is effective for uniformly distributed data and can achieve linear time complexity when the input is uniformly distributed.

### Characteristics:
- **Stability:** Depends on the sorting algorithm used for the buckets.
- **In-Place:** No (requires additional space for buckets).
- **Real-world Example:** Sorting heights of people in a range.

### Time and Space Complexity:
- Time Complexity: O(n^2) in worst case, O(n + k) on average.
- Space Complexity: O(n + k)

## 11. Tim Sort
### Overview:
Tim Sort is a hybrid sorting algorithm derived from merge sort and insertion sort. It is designed to perform well on many kinds of real-world data.

### Use Case:
Tim Sort is well-suited for sorting large datasets with varied characteristics.

### Characteristics:
- **Stability:** Stable.
- **In-Place:** No (requires additional space for merging).
- **Real-world Example:** Default sorting algorithm in Python.

### Time and Space Complexity:
- Time Complexity: O(n log n)
- Space Complexity: O(n)

## 12. Intro Sort
### Overview:
Intro Sort is a hybrid sorting algorithm that combines Quick Sort, Heap Sort, and Insertion Sort. It aims to provide good average-case performance.

### Use Case:
Intro Sort is suitable for scenarios where the input size is large, and a good average-case performance is desired.

### Characteristics:
- **Stability:** Not stable.
- **In-Place:** Yes.
- **Real-world Example:** Standard sorting algorithm in C++'s `std::sort()`.

### Time and Space Complexity:
- Time Complexity: O(n log n)
- Space Complexity: O(log n)


