### Implement the Binary Search Algorithm

This program searches for a value within a **sorted list** using the **Binary Search** algorithm.

- `low` and `high` define the search boundaries.
- `mid` is used to determine the middle position of the list.
- Each middle value checked is stored in `path_to_target`.
- If the value is found, the function returns the search path and the value's index.
- If the value is greater than the middle value, the search continues in the right half.
- If the value is smaller, the search continues in the left half.
- If the value is not found, the function returns `Value not found`.

Example:

```python
binary_search([1, 2, 3, 4, 5], 3)
# Output: ([3], 'Value found at index 2')
```