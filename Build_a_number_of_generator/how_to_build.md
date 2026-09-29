### Build a Range of Numbers Generator

This program creates a list of numbers from `start_num` to `end_num` using **recursion**.

- If `end_num < start_num`, the function returns an empty list `[]`.
- The function calls itself with `end_num - 1` until it reaches the starting limit.
- Then, each `end_num` is added to the list using `.append()`.
- The final result is a list of numbers from `start_num` to `end_num`.

Example:

```python
range_of_numbers(3, 9)
# Output: [3, 4, 5, 6, 7, 8, 9]
```