## Build a Hash Table

This program creates a **Hash Table** data structure using Python. A Hash Table stores data as **key-value pairs** and uses a hash function to determine the data's storage location.

### Key Concepts

- **`hash()`** — converts each character of the key into a Unicode value using `ord()`, then sums them up to produce the hash value.
- **`add()`** — adds a key-value pair to the Hash Table. If a hash collision occurs, the data is stored within the same nested dictionary.
- **`remove()`** — removes data based on the key. If the key is not found, the method does nothing.
- **`lookup()`** — searches for a value based on the key. If the key is not found, the method returns `None`.
- **`collection`** — the main dictionary that stores hash values ​​as keys and nested dictionaries as containers for the key-value pairs.

### Collision Example

The keys `"dear"` and `"read"` produce the same hash because they contain the same characters in a different order. Both can still be stored because the original keys are used to distinguish the data:

```python
{
    414: {
        "dear": "friend",
        "read": "book"
    }
}
```

### Usage Example

```python
table1 = HashTable()

table1.add("golf", "sport")
table1.add("dear", "friend")
table1.add("read", "book")

print(table1.lookup("golf"))  # sport

table1.remove("golf")

print(table1.lookup("golf"))  # None
```

This project provides practice in using **hash functions, dictionaries, nested dictionaries, key-value pairs, and collision handling** within a Hash Table data structure.