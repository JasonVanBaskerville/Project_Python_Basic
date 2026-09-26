## Settings Manager

This program is used to **manage user settings stored in a dictionary**, allowing for operations such as adding, modifying, deleting, and viewing settings.

### Features

* `lowercase()` → converts string keys and values ​​to lowercase.
* `add_setting()` → adds a new setting and checks if the key already exists.
* `update_setting()` → modifies the value of an existing setting.
* `delete_setting()` → removes a setting based on its key.
* `view_settings()` → displays all available settings or shows a message if the dictionary is empty.

The program also uses `isinstance()` to ensure that values ​​being converted to lowercase are indeed strings.

### Example

```python
settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}
```

Using the available functions, the user can perform **Create, Read, Update, and Delete (CRUD)** operations on the settings dictionary.