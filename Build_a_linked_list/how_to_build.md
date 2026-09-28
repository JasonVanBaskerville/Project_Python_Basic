## Build a Linked List

This program creates a **Linked List** data structure using Python. A Linked List consists of multiple **Nodes**, where each Node stores data (`element`) and a reference to the next Node (`next`).

### Key Concepts

- **`Node`** — stores a value and the address of the next Node.
- **`head`** — points to the first Node in the Linked List.
- **`length`** — stores the number of Nodes in the Linked List.
- **`add()`** — adds a new Node to the end of the Linked List.
- **`remove()`** — removes a Node based on its `element` value.
- **`is_empty()`** — checks if the Linked List is empty.

### Usage Example

```python
my_list = LinkedList()

print(my_list.is_empty())  # True

my_list.add(1)
my_list.add(2)

print(my_list.is_empty())  # False
print(my_list.length)      # 2

my_list.remove(1)
print(my_list.length)      # 1
```

In this example, the Linked List is initially empty. Then, the values ​​`1` and `2` are added, resulting in 2 Nodes. After `1` is removed, the number of Nodes becomes 1.