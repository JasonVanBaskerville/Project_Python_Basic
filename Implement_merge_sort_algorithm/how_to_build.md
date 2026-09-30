## Implementing the Merge Sort Algorithm

In this project, I implemented the **Merge Sort** algorithm to sort an array in ascending order.

Merge Sort operates using a **divide and conquer** approach, recursively splitting the array into two halves until each segment contains only a single element. Subsequently, the segments are merged back together by comparing elements from both halves to produce a sorted array.

The core process consists of:
1. Splitting the array into `left_part` and `right_part`.
2. Recursively calling `merge_sort()` on both parts.
3. Comparing the smallest elements from both parts.
4. Placing the smaller element into the main array.
5. Appending any remaining unprocessed elements.

This implementation utilizes **Merge Sort with a time complexity of O(n log n)**.