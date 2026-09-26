# Build a Salary Tracker

A simple program to manage employee data and salaries based on job levels using **Object-Oriented Programming (OOP)** in Python.

## Features

The `Employee` class is used to store and manage:

- Employee name
- Level/position (`trainee`, `junior`, `mid-level`, `senior`)
- Salary based on level

The program also includes validation to:

- Ensure names and levels use the appropriate data types.
- Ensure the provided level is valid/available.
- Prevent employees from moving to a lower level.
- Prevent selecting the same level.
- Ensure the salary is not lower than the minimum salary for the specific level.

## Concepts Covered

This project practices several Python and OOP concepts, such as:

- Classes and objects
- Class attributes
- The `__init__` constructor
- Encapsulation
- `@property` and setters
- Data validation using `TypeError` and `ValueError`
- Special methods `__str__()` and `__repr__()`
- Dictionaries to store base salaries based on levels