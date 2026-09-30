# Implementing the Quick Sort Algorithm

Quick Sort is a sorting algorithm that uses the **Divide and Conquer** concept. This algorithm selects an element as the **pivot**, then divides the remaining elements into two parts based on the pivot's value.

In this implementation, the first element is used as the pivot:

- `left_part` stores elements with values ​​**less than or equal to the pivot**.
- `right_part` stores elements with values ​​**greater than the pivot**.
- Both parts are then processed again using `quick_sort()` **recursively**.
- Once both parts are sorted, the results are combined into `left_sorted + [pivot] + right_sorted`.

The condition:

```python
if len(array) <= 1:
    return array
```

is used as the **base case**, because an array with 0 or 1 element is already sorted.

Example:

```python
quick_sort([20, 3, 14, 1, 5])
```

Initial process:

```text
pivot = 20
left_part = [3, 14, 1, 5]
right_part = []
```

Then `left_part` is sorted recursively, resulting in:

```text
[1, 3, 5, 14]
```

Finally, the result is combined with the pivot:

```text
[1, 3, 5, 14] + [20] + []
```

Resulting in:

```text
[1, 3, 5, 14, 20]
```