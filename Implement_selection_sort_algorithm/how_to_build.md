## Implement the Selection Sort Algorithm

Selection Sort is a sorting algorithm that works by finding the **smallest value** in the unsorted portion of the list and then swapping it with the first element of that section.

In this implementation:
- `min_index` stores the index of the smallest value.
- The `j` loop searches for the smallest value within the unsorted portion of the list.
- If a smaller value is found, `min_index` is updated.
- Once the search is complete, the values ​​are swapped using tuple assignment.
- The `if min_index != i` check prevents unnecessary swaps when the element is already in the correct position.

Example:

```python
selection_sort([33, 1, 89, 2, 67, 245])
```

Result:

```text
[1, 2, 33, 67, 89, 245]
```

This algorithm sorts the list in **ascending order** and modifies the list directly (*in-place*).