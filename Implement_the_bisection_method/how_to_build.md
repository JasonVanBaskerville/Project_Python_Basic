# Implement the Bisection Method

This program implements the **Bisection Method** to find an approximate square root of a number.

### How it works:
- Negative numbers raise a `ValueError` because their square roots are undefined in the set of real numbers.
- For `0` and `1`, the function returns the value immediately.
- For numbers greater than `1`, the search range spans from `0` to the `number`.
- For numbers between `0` and `1`, the search range spans from the `number` to `1`.
- In each iteration, the program calculates the midpoint (`mid`) and compares `mid²` with the `number`.
- The search range is narrowed until the difference falls within the specified `tolerance`.
- If the result is not found within `max_iterations`, the program displays a message indicating that the process failed to converge and returns `None`.

The program is also tested using various values—such as `0`, `0.001`, `0.25`, `1`, and `225`—with different tolerance levels and iteration counts.