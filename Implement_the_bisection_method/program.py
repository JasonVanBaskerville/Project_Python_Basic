def square_root_bisection(number, tolerance=0.001, max_iterations=100):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    if number > 1:
        low = 0
        high = number

    if number < 1:
        low = number
        high = 1

    for i in range(max_iterations):
        mid = (low + high) / 2
        square = mid ** 2
        root = number ** 0.5

        if abs(root - mid) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        elif square < number:
            low = mid
        else:
            high = mid

    print(f"Failed to converge within {max_iterations} iterations")
    return None

# square_root_bisection(0) should return 0.
square_root_bisection(0)

# square_root_bisection(0.001, 1e-7, 50) should return a number between 0.03162267660168379 and 0.031622876601683794.
square_root_bisection(0.001, 1e-7, 50)

# square_root_bisection(0.25, 1e-7, 50) should return a number between 0.4999999 and 0.5000001.
square_root_bisection(0.25, 1e-7, 50)

# square_root_bisection(1) should return 1.
square_root_bisection(1)

# square_root_bisection(225, 1e-3, 100) should return a number between 14.999 and 15.001.
square_root_bisection(225, 1e-3, 100)

# square_root_bisection(225, 1e-7, 10) should print Failed to converge within 10 iterations.
square_root_bisection(225, 1e-7, 10)