## Medical Records Validator

This program is used to **validate medical record data formats** to ensure that every data entry adheres to the structure and data types defined by the established rules.

### Validations performed

* `patient_id` → must follow a format like `P1001`
* `age` → must be a number and at least 18 years old
* `gender` → must be either `male` or `female`
* `diagnosis` → must be a string or `None`
* `medications` → must be a list containing strings
* `last_visit_id` → must follow a format like `V2301`

The program also checks:

* Whether the data is a `list` or `tuple`
* Whether each record is a `dictionary`
* Whether all required keys are present
* Whether the value of each field meets the constraints

If invalid data is found, the program displays an **error message along with the position of the problematic record**.

If all data complies with the rules, the program displays:

```text
Valid format.
```

This program serves as an exercise in using **functions, dictionaries, lists, loops, conditional statements, `isinstance()`, `sets`, `enumerate()`, regular expressions (`re`), and data validation**.