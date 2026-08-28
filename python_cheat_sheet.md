# Python Cheat Sheet

**English** | [日本語](./README.md)

> [!NOTE]
> This English version was translated using AI.

A quick reference to commonly used Python syntax and operations, organized by topic.

> [!NOTE]
> The code fences use the `python` language identifier so that editors such as VS Code can apply syntax highlighting.

## Table of Contents

- [Strings](#strings)
  - [Searching, Splitting, and Replacing](#searching-splitting-and-replacing)
  - [f-string Formatting](#f-string-formatting)
  - [Raw Strings and Encoding](#raw-strings-and-encoding)
  - [Comprehensions and Unpacking](#comprehensions-and-unpacking)
- [Data Structures](#data-structures)
  - [Lists](#lists-list)
  - [Tuples](#tuples-tuple)
  - [Sets](#sets-set)
  - [Dictionaries](#dictionaries-dict)
- [Built-in Functions](#built-in-functions)
- [Functions](#functions)
  - [Parameter Types](#parameter-types)
  - [Mutable Default Arguments](#mutable-default-arguments)
  - [Lambdas, Higher-Order Functions, and Scope](#lambdas-higher-order-functions-and-scope)
- [Classes and Instances](#classes-and-instances)
  - [Inheritance, super(), and property](#inheritance-super-and-property)
- [Decorators](#decorators)
- [Modules, Packages, Namespaces, and Scope](#modules-packages-namespaces-and-scope)
- [File Operations](#file-operations)
  - [Text Files](#text-files)
  - [JSON Files](#json-files)
  - [CSV Files](#csv-files)
  - [File Modes](#file-modes)
- [Exception Handling](#exception-handling)
- [Regular Expressions](#regular-expressions)

---

## Strings

### Searching, Splitting, and Replacing

```python
s = " Python,cheat sheet,search split replace "
text = s.strip()                       # Remove leading/trailing whitespace

text.startswith("Python")             # Test a prefix: True
text.endswith("replace")              # Test a suffix: True
"Python" in text                      # Test for a substring: True

parts = text.split(",")                # Split into a list
joined = " / ".join(parts)             # Join strings
replaced = text.replace(
    "cheat sheet", "reference"
)                                      # Replace text

found_index = text.find("Py")          # First index, or -1 if not found
without_prefix = text.removeprefix(
    "Python,"
)                                      # Remove the prefix if present

head, separator, tail = text.partition(",")
# Split into the text before, the separator, and the text after
```

Strings are immutable. String methods normally return a new string instead of changing the original. Use `casefold()` for robust case-insensitive comparisons.

```python
"Python".casefold() == "PYTHON".casefold()  # True
```

### f-string Formatting

```python
name, price, rate = "Book", 123456, 0.075

f"{name}: ${price:,}"   # 'Book: $123,456'
f"{rate:.1%}"           # '7.5%'
f"{price:>10}"          # Right-align in a field of width 10
f"{price:0>10}"         # Pad the left side with zeros
f"{name!r}"             # repr() form: "'Book'"
f"{price=}"             # 'price=123456' (useful for debugging)
```

### Raw Strings and Encoding

Raw strings treat backslashes literally in most cases.

```python
path = r"C:\new\test"

data = "Python".encode("utf-8")  # String to bytes
text = data.decode("utf-8")       # Bytes to string
```

### Comprehensions and Unpacking

```python
# List comprehension: select even numbers and square them
squares = [x * x for x in range(6) if x % 2 == 0]
# [0, 4, 16]

# Dictionary comprehension
lookup = {x: x * x for x in range(3)}
# {0: 0, 1: 1, 2: 4}

# Set comprehension: duplicates removed; order not guaranteed
names = ["Alice", "Bob", "Charlie", "alice"]
unique = {name.lower() for name in names}
# {'alice', 'bob', 'charlie'} (display order may vary)

labels = [name + " (member)" for name in names]
print(*labels, sep=", ")
```

Use `*` to unpack an iterable and `**` to unpack a dictionary.

```python
numbers = [1, 2]
more_numbers = [0, *numbers, 3]      # [0, 1, 2, 3]

options = {"flag": True}
config = {"mode": "fast", **options}
# {'mode': 'fast', 'flag': True}

print(*numbers)                      # Same as print(1, 2)
```

---

## Data Structures

| Type | Ordered | Mutable | Duplicates | Typical use |
|---|---|---|---|---|
| `list` | Yes | Yes | Yes | An ordered collection of items |
| `tuple` | Yes | No | Yes | A fixed group of values |
| `set` | Not guaranteed | Yes | No | Deduplication and set operations |
| `dict` | Yes | Yes | Keys: no | Key-value mappings |

### Lists `list`

Lists are ordered and mutable.

```python
names = ["Alice", "Bob", "Charlie", "alice"]

first = names[0]                     # First item
last = names[-1]                     # Last item
part = names[1:3]                    # [start:stop:step]

names.append("David")                # Add one item at the end
names.extend(["Eve", "Frank"])       # Add multiple items at the end
names.insert(1, "Grace")             # Add an item at an index

names.remove("Charlie")              # Remove the first matching value
popped = names.pop()                  # Remove and return the last item
del names[0]                          # Delete an item by index

names.sort(reverse=True)              # Sort the original list descending
names.reverse()                       # Reverse the original list

"David" in names                     # Membership test
len(names)                            # Number of items
names.count("Alice")                 # Number of matches
names.index("David")                 # Index of the first match
```

> [!TIP]
> `list.sort()` changes the original list and returns `None`. Use `sorted(names)` when you need a new sorted list.

### Tuples `tuple`

Tuples are ordered and cannot be changed after creation.

```python
point = (10, 20)
single = (10,)                       # A one-item tuple needs a comma

x, y = point                         # Unpack values
x, y = y, x                          # Swap values
```

### Sets `set`

Sets contain no duplicate elements and support set operations.

```python
a = {1, 2, 3}
b = {3, 4}
empty = set()                        # {} creates an empty dictionary

a | b                                # Union: {1, 2, 3, 4}
a & b                                # Intersection: {3}
a - b                                # Difference: {1, 2}
a ^ b                                # Symmetric difference: {1, 2, 4}

a.add(5)                             # Add an element
a.discard(9)                         # Remove it if present; no error if absent
a.clear()                            # Remove all elements
```

### Dictionaries `dict`

Dictionaries store key-value pairs.

```python
user = {"name": "Mika", "age": 20}

name = user["name"]                  # Raises KeyError if missing
city = user.get("city", "Tokyo")    # Return a default if missing

user["age"] = 21                    # Add or overwrite a value
user["active"] = True
user.update(city="Osaka", active=False)
user.update({"city": "Kyoto"})

keys = user.keys()                   # View of keys
values = user.values()               # View of values
items = user.items()                 # View of (key, value) pairs

for key, value in user.items():
    print(key, value)

age = user.pop("age")                # Remove the key and return its value
"name" in user                       # Test whether a key exists
```

---

## Built-in Functions

| Category | Common functions |
|---|---|
| Types and tests | `type(x)`, `isinstance(x, T)`, `issubclass(A, B)`, `callable(x)`, `hash(x)` |
| Conversion | `str(x)`, `int(x)`, `float(x)`, `bool(x)`, `list(it)`, `tuple(it)`, `dict(it)`, `set(it)` |
| Aggregation | `len(x)`, `min(it)`, `max(it)`, `sum(it)`, `abs(x)` |
| Ordering | `sorted(it, key=..., reverse=True)`, `reversed(seq)` |
| Iteration | `range(start, stop, step)`, `enumerate(it, start=0)`, `zip(a, b)` |
| Transformation | `map(fn, it)`, `filter(fn, it)` |
| Conditions | `any(it)`, `all(it)` |
| Attributes | `getattr(obj, "name", default)`, `setattr(obj, "name", value)` |
| Input/output | `print(*values, sep=" ", end="\n")`, `input(prompt)` |

```python
names = ["Aoi", "Mika"]
scores = [90, 80]

for index, name in enumerate(names, start=1):
    print(index, name)                # Iterate with an index

for name, score in zip(names, scores):
    print(name, score)                # Iterate over multiple sequences

has_passed = any(score >= 60 for score in scores)
all_passed = all(score >= 60 for score in scores)
```

---

## Functions

```python
def greeting(name: str, prefix: str = "Hi") -> str:
    """Return a greeting."""
    return f"{prefix}, {name}!"


greeting("Aoi")                         # Positional argument
greeting(name="Aoi", prefix="Hello")  # Keyword arguments
```

### Parameter Types

```python
def func(pos_only, /, normal=0, *args, flag=False, **kwargs):
    return pos_only, normal, args, flag, kwargs
```

| Syntax | Meaning |
|---|---|
| `pos_only` | A positional argument |
| `/` | Parameters before this marker are positional-only |
| `normal=0` | May be positional or keyword; default is `0` |
| `*args` | Collects extra positional arguments into a tuple |
| `flag=False` | A keyword-only parameter with a default |
| `**kwargs` | Collects extra keyword arguments into a dictionary |

```python
result = func(1, 2, 3, 4, flag=True, mode="fast")
# (1, 2, (3, 4), True, {'mode': 'fast'})
```

### Mutable Default Arguments

A mutable default value is created once and shared across calls.

```python
# Avoid this unless shared state is intentional
def bad_default(items=[]):
    items.append(1)
    return items
```

Use `None` when each call should receive a new collection.

```python
def add(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

### Lambdas, Higher-Order Functions, and Scope

A `lambda` expression creates a small anonymous function.

```python
double = lambda x: x * 2
double(5)                            # 10

# Equivalent behavior
def double(x):
    return x * 2
```

A higher-order function accepts a function as an argument or returns one.

```python
rows = [
    {"score": 80},
    {"score": 90},
    {"score": 70},
]

result = sorted(
    rows,
    key=lambda row: row["score"],
    reverse=True,
)
# [{'score': 90}, {'score': 80}, {'score': 70}]
```

Use `nonlocal` to modify a variable in an enclosing function scope.

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()
c()                                  # 1
c()                                  # 2
```

---

## Classes and Instances

```python
class User:
    species = "human"                # Class attribute

    def __init__(self, name: str):
        self.name = name              # Instance attribute

    def greet(self) -> str:
        return f"Hi, {self.name}"


user = User("Aoi")                   # Create an instance
user.name                             # 'Aoi'
user.greet()                          # 'Hi, Aoi'
isinstance(user, User)                # True
```

### Inheritance, `super()`, and `property`

```python
class Admin(User):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name)         # Initialize the parent class
        self._level = level

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int) -> None:
        if value < 1:
            raise ValueError("level must be at least 1")
        self._level = value

    @level.deleter
    def level(self) -> None:
        del self._level


admin = Admin("Aoi", level=2)
admin.level                           # Call the getter
admin.level = 3                       # Call the setter
del admin.level                       # Call the deleter
```

By convention, a name beginning with `_` is treated as non-public. Unlike Java's `private`, this is not an enforced access restriction.

---

## Decorators

A decorator receives an existing callable and returns an object with added or changed behavior. Apply one with `@decorator_name`.

```python
from functools import wraps


def repeat(count):
    def decorator(func):
        @wraps(func)                   # Preserve name, docstring, and metadata
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(count):
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")                        # Print the greeting three times
```

`@repeat(3)` is roughly equivalent to:

```python
greet = repeat(3)(greet)
```

---

## Modules, Packages, Namespaces, and Scope

```python
import math
import pathlib as pl                  # Import with an alias
from collections import Counter       # Import a name from a module

fruits = ["apple", "banana", "apple", "orange"]
counts = Counter(fruits)              # Count occurrences

math.sqrt(9)
pl.Path("data.txt")
```

A module is normally one `.py` file. A package groups modules in a directory and commonly contains an `__init__.py` file, although namespace packages may omit it. A relative import inside a package can look like `from .utils import helper`.

Use the `__name__` guard to run code only when the file is executed directly, not when it is imported.

```python
def main():
    print("run")


if __name__ == "__main__":
    main()                             # Runs for: python tool.py
```

---

## File Operations

`pathlib.Path` provides a convenient interface for paths, existence checks, and file I/O.

```python
from pathlib import Path

path = Path("sample.txt")
```

A relative path is resolved from the current working directory. To resolve a file relative to the script itself, use:

```python
path = Path(__file__).parent / "sample.txt"
```

### Text Files

Files opened in a `with` block are closed automatically.

```python
from pathlib import Path

path = Path("sample.txt")

# Write and replace existing contents
with path.open("w", encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("Python cheat sheet\n")

# Write the complete file at once
path.write_text(
    "Hello, World!\nPython cheat sheet\n",
    encoding="utf-8",
)

# Read through a file object
with path.open("r", encoding="utf-8") as file:
    content = file.read()

# Read the complete file at once
content = path.read_text(encoding="utf-8")
```

Create an empty file only if it does not exist:

```python
path = Path("rows.csv")

if not path.exists():
    print(f"{path} does not exist; creating it")
    path.touch()

# Shorter; an existing file does not cause an error
path.touch(exist_ok=True)
```

### JSON Files

`json.dump()` writes Python data to a JSON file, while `json.load()` reads JSON data into Python.

```python
import json
from pathlib import Path

json_path = Path("sample.json")
data = {"name": "Alice", "age": 30}

with json_path.open("w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

with json_path.open("r", encoding="utf-8") as file:
    loaded_data = json.load(file)
```

- `ensure_ascii=False` preserves non-ASCII characters instead of escaping them.
- `indent=4` makes the output easier to read by indenting it with four spaces.

### CSV Files

Use the `csv` module so that delimiters, quotation marks, and embedded newlines are handled correctly.

#### Write Dictionaries

```python
import csv
from pathlib import Path

path = Path("rows.csv")

with path.open("w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})
    writer.writerow({"name": "Bob", "age": 25})
```

#### Read Dictionaries

```python
with path.open("r", newline="", encoding="utf-8-sig") as file:
    rows = list(csv.DictReader(file))

for row in rows:
    print(row)
```

Values read by `DictReader` are normally strings:

```python
{"name": "Alice", "age": "30"}
{"name": "Bob", "age": "25"}
```

#### Write Multiple Rows

```python
data = [
    ["ID", "Name", "Age"],
    [1, "Taro Yamada", 16],
    [2, "Hanako Sato", 16],
]

with open("base.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

#### Append Rows

Mode `"a"` appends to an existing file or creates a new one.

```python
new_data = [
    [11, "Shota Yamaguchi", 17],
    [12, "Emi Kondo", 16],
]

with open(
    "sample.csv",
    "a",
    newline="",
    encoding="utf-8-sig",
) as file:
    writer = csv.writer(file)
    writer.writerows(new_data)
```

Mode `"a+"` permits both appending and reading. Seek to the beginning before reading because writes occur at the end.

```python
with open(
    "rows.csv",
    "a+",
    newline="",
    encoding="utf-8-sig",
) as file:
    file.seek(0)
    rows = list(csv.DictReader(file))
```

- `newline=""` lets the `csv` module control newline handling.
- `encoding="utf-8-sig"` handles the UTF-8 byte-order mark often useful with Windows Excel.
- `read_text().splitlines()` splits text into lines but does not parse CSV quoting rules.

### File Modes

| Mode | Operation | If the file exists | If it is missing |
|---|---|---|---|
| `"r"` | Read | Read it | Raise `FileNotFoundError` |
| `"w"` | Write | Truncate and overwrite | Create it |
| `"a"` | Append | Add at the end | Create it |
| `"x"` | Exclusive creation | Raise `FileExistsError` | Create it |
| `"a+"` | Read and append | Write at the end | Create it |

---

## Exception Handling

Exception handling defines what the program should do when an operation fails.

```python
def save(value):
    print(f"Saved: {value}")


def cleanup():
    print("Cleanup complete")


input_text = "123"

try:
    value = int(input_text)           # Operation that may fail
except (ValueError, TypeError) as error:
    print(f"Not an integer: {error}")
else:
    save(value)                       # Runs only if no exception occurred
finally:
    cleanup()                         # Always runs at the end
```

| Keyword | Purpose |
|---|---|
| `try` | Contains operations that may raise an exception |
| `except` | Handles specified exception types |
| `else` | Runs only when the `try` block succeeds |
| `finally` | Runs at the end whether or not an exception occurred |
| `raise` | Raises an exception explicitly |

Avoid a bare `except:` in most code because it also catches exceptions used for interpreter exit and cancellation.

Define a custom exception by inheriting from a suitable built-in exception:

```python
class InputError(ValueError):
    """Raised when input is invalid."""


try:
    value = int("abc")
except ValueError as error:
    raise InputError("An integer is required") from error
```

Common exceptions:

| Exception | Typical cause |
|---|---|
| `TypeError` | An operation received an inappropriate type |
| `ValueError` | The type is valid, but the value is inappropriate |
| `KeyError` | A dictionary key does not exist |
| `IndexError` | A sequence index is out of range |
| `FileNotFoundError` | A requested file does not exist |

---

## Regular Expressions

The `re` module searches, extracts, replaces, and splits text using patterns. Raw strings such as `r"..."` are recommended because regular expressions use many backslashes.

### Searching and Groups

```python
import re

pattern = re.compile(r"(?P<name>[A-Za-z]+)@([\w.-]+)")
match = pattern.search("Contact: user@example.com")

if match:
    print(match.group(0))              # user@example.com
    print(match.group("name"))         # user
    print(match.group(2))              # example.com
```

`search()` returns the first match object or `None`. This email pattern is a simple learning example, not a complete email-address validator.

| Pattern | Meaning |
|---|---|
| `(?P<name>...)` | A named group called `name` |
| `[A-Za-z]` | An uppercase or lowercase ASCII letter |
| `+` | One or more repetitions |
| `@` | The literal `@` character |
| `(...)` | A capturing group |
| `\w` | A word character, such as a letter, digit, or underscore |
| `[\w.-]+` | One or more word characters, periods, or hyphens |

### Extracting, Replacing, and Splitting

```python
numbers = re.findall(r"\d+", "A12 B34")
# ['12', '34']

numbers_as_int = [int(value) for value in numbers]
# [12, 34]

result = re.sub(r"\s+", " ", "a    b")
# 'a b'

parts = re.split(r"[,;]", "a,b;c")
# ['a', 'b', 'c']
```

| Symbol | Meaning |
|---|---|
| `.` | Any character except a newline |
| `^` / `$` | Start/end of the string |
| `*` | Zero or more repetitions |
| `+` | One or more repetitions |
| `?` | Zero or one repetition |
| `[abc]` | One of `a`, `b`, or `c` |
| `\d` / `\w` / `\s` | Digit / word character / whitespace |

---

## Related File

- Source Python file: [`cheat_sheet.py`](./cheat_sheet.py)
