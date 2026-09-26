## Pin Extractor

This program is used to **extract a secret code from a set of poems**. The secret code is generated based on the **length of a specific word in each line of the poem**.

### How It Works

The main function used is:

```python
def pin_extractor(poems):
```

The function accepts a collection of poems in the form of a list.

For each poem:

1. The poem is split into lines using `split('\n')`.
2. Each line is split into words using `split()`.
3. The program uses the line position (`line_index`) to determine which word to use.

   * Line 0 → takes the 0th word
   * Line 1 → takes the 1st word
   * Line 2 → takes the 2nd word
   * and so on.
4. The program calculates the character count of that word using `len()`.
5. These character counts are combined to form a code.
6. If a line does not contain a word at the required position, the program inserts the number `0`.

Example:

```text
The grass is green
here and there
hoping for rain
before it turns yellow
```

Word selection:

```text
Line 0 → The      → 3 characters
Line 1 → and      → 3 characters
Line 2 → rain     → 4 characters
Line 3 → yellow   → 6 characters
```

Resulting code:

```text
3346
```

### Key Parts

```python
for line_index, line in enumerate(lines):
```

`enumerate()` is used so the program obtains both the **line index number** and the line content.

```python
words = line.split()
```

Used to split each line into a list of words.

```python
if len(words) > line_index:
```

Used to ensure that a word exists at the required index. ```python
secret_code += str(len(words[line_index]))
```

Calculates the character count of the selected word, converts it into a string, and appends it to `secret_code`.

```python
else:
    secret_code += '0'
```

If a word is not available at that position, the program appends `0`.

### Output

When three poems are passed to the function:

```python
print(pin_extractor([poem, poem2, poem3]))
```

the program produces:

```text
['3550', '3346', '4311']
```

Thus, this program serves as an exercise in using **functions, loops, `enumerate()`, string manipulation, lists, indexing, and conditional statements** in Python.