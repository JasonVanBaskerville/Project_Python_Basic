## GameCharacter

This program is an **Object-Oriented Programming (OOP)** exercise utilizing the concepts of **Encapsulation** and `@property`.

### Features
- Creates a character with `name`, `health`, `mana`, and `level`.
- `health` is constrained between `0` and `100`.
- `mana` is constrained between `0` and `50`.
- `level_up()` increases the level and restores health and mana to their maximum values.
- `__str__()` is used to display character information in a clean, readable format.

### OOP Concepts
- **Encapsulation**: internal data is stored using the attributes `_name`, `_health`, `_mana`, and `_level`.
- **Property & Setter**: used to control changes to `health` and `mana` values.
- **Method**: `level_up()` is used to perform an action on the object.
- **String Representation**: `__str__()` is used to display object information.