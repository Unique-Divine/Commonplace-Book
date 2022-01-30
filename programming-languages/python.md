<!-- python.md -->

## Python     <!-- omit in toc -->

- [Standard Library](#standard-library)
  - [Reading and Writing Files](#reading-and-writing-files)
  - [HTTP Requests](#http-requests)
  - [Functools](#functools)
  - [Sort() and sorted()](#sort-and-sorted)
  - [Binary and other bases](#binary-and-other-bases)
- [Writing Tests](#writing-tests)
- [Working with Databases](#working-with-databases)
  - [MongoDB (pymongo)](#mongodb-pymongo)
- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
- [Protocol Buffers](#protocol-buffers)
- [Miscellaneous](#miscellaneous)

***

## Standard Library

***

### Reading and Writing Files

`open()` returns a file object.

File objects mediate access to on-disk files. File objects are also called streams.

Q: `file_name (str)` is the name of a file. How do you read the file line by line in Python?

```python
with open(file=file_name, mode="r") as file:
    for idx, line in enumerate(file):
        pass # line (str): A line in the file
```

The two arguments of `open()` are 'file' and 'mode'.

Modes of `open()`:

* Mode `'a'`: For appending data to the end of 'file'.
* Mode `'w'`: For writing only. An existing file with the same name as 'file' will be erased.
* Mode `'r+'`: opens a file for both reading and writing.

Q: Why use the `with` keyword with the `open` method?

It is good practice to use the `with` keyword when dealing with file objects because the file will be properly closed after its suite finishes even if an exception is raised at some point. Using `with` is also much shorter than writing equivalent `try-finally` blocks.

```python
with open(file="some_file") as file:
    pass
file.closed
```

`True`

* Python glossary - file object [[docs]](https://docs.python.org/3/glossary.html#term-file-object)

Date: 21年6月

***

### HTTP Requests

`pip install requests`

[Hypertext Transfer Protocol (HTTP)](https://en.wikipedia.org/wiki/Hypertext\_Transfer\_Protocol#Request\_methods) is a request-response protocol commonly used for sending data through web browsers.

**GET**

The GET request is for retrieving data without altering its state.

```python
url: str
response: requests.Response = requests.get(url)
```

**POST**

POST

The two simplest kinds of

***

### Functools

Python's [functools](https://docs.python.org/3/library/functools.html#module-functools) module is used for higher-order functions and operations on callable objects. It's a part of the standard library

Date: 21年8月

***

### Sort() and sorted()

```python
import dataclasses

@dataclasses.dataclass
class Student:
    name: str
    grade: str
    age: int

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

students = [Student('John', 'A', 15),
            Student('Jane', 'B', 12),
            Student('Dave', 'B', 10),]
```

Q: Sort the students by age in ascending order.

```python
sorted(students, key = lambda student: student.age)
```

Q: Sort the students by age in descending order.

```python
sorted(students, key = lambda student: student.age, reverse=True)
```

Q: What is sorting stability? → **Stable** sorting algorithms maintain the relative order of records with equal keys, sorting repeated elements in the same order that they appear in the input.

Cloze:

* Python sorts are guaranteed to be stable.
* Because of this, when multiple records have the same key, their original order is preserved.

Q: Sort the students by descending grade and then ascending age.

```python
students = sorted(students, key=lambda s: s.age)
students = sorted(students, key=lambda s: s.grade, reverse=True)
```

***

### Binary and other bases

Q: Return a binary representation of the given number.

```python
def int2binary(i: int) -> str:
    ...
```

→

```python
def int2binary(i: int) -> str:
    return bin(i)

>>> int2binary(3)
'0b11'
```

Q: A binary representation string has "0b" at the front. If you have an integer, `i`, and want its binary representation without the "0b", how can you return that efficiently?

```python
i: int
>>> f"{i:b}"
>>> format(i, "b")  # equivalent
```

See https://www.programiz.com/python-programming/methods/built-in/format

Q:

```python
def add_binary(a: str, b: str):
    ...
```

Given two binary strings, `a` and `b`, return their sum as a binary string. As binary strings, `a` and `b` consist only of "0" and "1" characters.

```python
def add_binary(a: str, b: str) -> str:
    a: int = int(a, base=2)
    b: int = int(b, base=2)
    return f"{a + b:b}"
    # return format(a + b, "b") # equivalent 
```

***

Q: Return the index of the first occurence of 'needle' in 'haystack', or return -1 if 'needle' is not part of 'haystack'. Return 0 if 'needle' is an empty string.

```python
def find_needle(haystack: str, needle: str) -> int:
    ...
```

```python
def find_needle(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    str_len: int = len(needle)
    for i in range(len(haystack) - str_len + 1):
        if haystack[i:i + str_len] == needle:
            return i
    return -1
```

Q: How do you combine an iterable of strings into one string in Python? A: Use `s.join(txt)`, where `s` is a string that specifies how to join and `txt` is the iterable of strings.

Q: Return the strings combined into one.

```python
text = ['Stay', 'gold,', 'Ponyboy.']
```

```python
>>> " ".join(text)
'Stay gold, Ponyboy.'
```

Q: Implement a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.

```python
def longest_common_prefix(strs: List[str]) -> str:
    ...
```

A:

```python
def longest_common_prefix(strs: List[str]) -> str:
    member: str = strs[0]
    common_prefix: List[str] = []
    max_idx: int = min([len(s) for s in strs])
    for i, char in enumerate(member):
        if i == max_idx:
            break
        if all([char == s[i] for s in strs]):
            common_prefix.append(char)
        else:
            break
    if len(common_prefix) == 0:
        return ""
    else:
        return "".join(common_prefix)
```

Q: Implement a function that reverses an array of strings in-place without creating another array.

```python
def reverse(strs: List[str]) -> None:
    ...
```

A:

```python
def reverse(strs: List[str]) -> None:
    stop_idx = len(strs) // 2
    for i, s in enumerate(strs):
        if i == stop_idx:
            break
        back_s = strs[-(i + 1)]
        strs[i] = back_s
        strs[-(i + 1)] = s
```

#### Display number in scientific notation.

```python
def num_in_scientific_notation(num: float) -> str: 
    return "{:e}".format(num)
```



***

## Writing Tests

***

**Disabling warnings**

To ignore pytest warnings at the command line: `pytest -p no:warnings`

See: https://docs.pytest.org/en/latest/how-to/capture-warnings.html#disabling-warnings-summary

#### Pytest Mock

The standard solution to creating mock objects in python is the [`unittest.mock` library](https://docs.python.org/3/library/unittest.mock.html). This section goes over how to create mocks in pytest with [pytest-mock](https://github.com/pytest-dev/pytest-mock)

***

## Working with Databases

***

### MongoDB (pymongo)

Pymongo assumes MongoDB is installed and running on the default host and port. If this is not the case, go to: https://docs.mongodb.com/manual/installation/ .

You'll notice there are two installation types to choose from: community and enterprise edition. According to [a thread on the mongodb forums](https://www.mongodb.com/community/forums/t/difference-between-enterprise-and-community-server-and-will-they-conflict-if-both-are-installed/76695),

> "Core server features for developers are generally the same, but a MongoDB Enterprise subscription includes additional operational and management features, a commercial license (warranty & idemnification), as well as access to proactice support and on-demand training.

In my case, I only needed the community edition.

There are two main steps for this installation.

1. Install MondoDB Server: [[installation instructions (Windows)]](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)
2. Install MongoDB Shell (mongosh): [[installation instructions]](https://docs.mongodb.com/mongodb-shell/install/)

The installation instructions for Community Edition are toward the bottom of the page (at the above link) where it says "Procedure". You're finished with step 1 when you can start MongoDB with\
`"C:\Program Files\MongoDB\Server\5.0\bin\mongod.exe" --dbpath="c:\data\db"`

1. Connect to a MongoDB deployment using the mongosh [\[docs\]](https://docs.mongodb.com/mongodb-shell/connect/#std-label-mdb-shell-connect).

[Continue from here](https://docs.mongodb.com/mongodb-shell/connect/#std-label-mdb-shell-connect)

At this point you should be able to type `mongosh` at the prompt and see the MongoDB Shell run. However, the commands `mongo`, `mongod`, and `mongos` won't run on Windows. To enable these commands, you need to add shortcuts to each command's corresponding executable to the system's environment variables.

1. Hit the Windows key, then type environment variables and hit enter. Alternatively, open the Control Panel and select "Edit the system environment variables".
2. Under the "Advanced" tab, select `Environment Variables`.
3. Under "System Variables", select `New`.
4.  Add each command's name to one field its executable path to the other field. For me, `mongo`'s executable was at

    ```
    "C:\Program Files\MongoDB\Server\5.0\bin\mongo.exe"
    ```

    The other two executables were in the same directory.

Now, `mongo` and `mongod` work, but what do they do?

`mongo`: Opens the Mongo Shell, an interactive command line interface that uses JavaScript and a related API to interact with the MongoDB client. Mongo shell is the default client for the MongoDB database server.

- Used for data manipulation
- Used for management of database instances

`mongod`: Manages all of the MongoDB server tasks. `mongod` is a background process used by MongoDB. It's short for "Mongo Daemon".

**References MongoDB:**

- Jayatilake, Navindu. 2019. How to get started with MongoDB in 10 minutes. [[article]](https://www.freecodecamp.org/news/learn-mongodb-a4ce205e7739/)
- [Pymongo tutorial](https://pymongo.readthedocs.io/en/stable/tutorial.html)

***

## Object-Oriented Programming (OOP)

***

**Abstract Base Classes**

An abstract base class specifies the interface that a class should adhere to and acts as an agreement between different parts of a program.

Q: Import the abstract base class and abstract method.

```python
from abc import ABC, abstractmethod
```

Q: Define a short abstract base class, "HelloWorld", with an abstract method called "hello" that should return a string.

```python
from abc import ABC, abstractmethod

class HelloWorld(ABC):
    
    @abstractmethod
    def hello(self) -> str:
        pass
```

Attempting to create an instance of an abstract base class (ABC) raises an error. You can, however, **create subclasses that inherit from the ABC**. An ABC purely defines the kind of methods that a class that inherits from the ABC should have.

```python
# Assume the ABC, HelloWorld, is implemented in the same file.
class JapaneseHelloWorld(HelloWorld):
    def hello(self) -> str:
        return "こんにちは、世界！"

class ChineseHelloWorld(HelloWorld):
    def hello(self) -> str:
        return "你好世界！"
```

Attempting to create an instance of one of the concrete classes, "JapaneseHelloWorld" and "ChineseHelloWorld", without implementing the "hello" method would raise an error too.

#### Data classes

Python's `dataclass` functionality allows you to write shorter code and initialize, print, compare, and order data much more easily.

Why use data classes?

A class for a data container is often used differently. Many instances may need to be made. You probably want to order them, compare them, easily inspect the data inside them, etc.

Regular classes don't provide much built-in convenient functionality for data oriented classes. Classes that build around a behavior may not have as many instances or be conducive to representing data structures. Because of this, some programming languages provide a type of class that is better tuned to storing data, e.g. C#'s struct type that is good for representing data structures.

**Simplest data class: All required arguments**

Data classes have a built-in initialize that will help you quickly fill in an object with data. There are easy ways to print compare and order them.

```python
# Regular class
class Person:
    """A person that has a name, job, and age."""
    name: str
    job: str
    age: int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age

p1 = Person(name='Joe', job='SDE', age=25)
```

Q: Implement this as a `dataclass`:

```python
from dataclasses import dataclass

@dataclass
class Person:
    """A person that has a name, job, and age."""
    name: str
    job: str
    age: int
```

**Data class with default arguments**

Let's say all of our people usually have the same job title, which is software development engineer ("SDE"). We'd want to set this as a default parameter to save some typing.

```python
from dataclasses import dataclass

@dataclass
class Person:
    """A person that has a name, job, and age."""
    name: str
    job: str = "SDE"
    age: int

p1 = Person(name='Joe', age=25)
```

**Data class with attributes that depend on other parameters**

Dynamically generated attributes can be defined in data classes using the `field` functionality in combination with `__post_init__`.

For example, let's say that the 'age' parameter automatically specifies a job if it's low enough. Otherwise, 'job' will default to "SDE" like before.

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    """A person that has a name, job, and age."""
    name: str
    job: str = field(default = "SDE", init = False)
    age: int

    def __post_init__(self):
        age = self.age
        if (self.job == "SDE") and (age <= 18):
            if age >= 14 and age <= 18:
                self.job = "Student - high school"
            elif age >= 12 and age <= 14:
                self.job = "Student - middle school"
            elif age >= 5 and age <= 12:
                self.job = "Student - elementary school"
            else:
                self.job = "Baby, toddler, or pre-K"
```

Reference: ArjanCodes. 2021. If you're not using Python DATA CLASSES yet, you should. 🚀 [[YouTube]](https://youtu.be/vRVVyl9uaZc)

#### Prefer composition over inheritance

Inheritance makes it difficult to duplicate functionality to different classes.

With composition, our goal is to separate out concepts so that they can be combined in meaningful ways. We're not creating hierarchies of classes.

If we have a class that we want to make subclasses of, it's beneficial to make the first one an abstract base class.

```python
from abc import ABC, abstractmethod
from typing import Optional 

class FFNN(ABC):  
    """Represents a PyTorch module for a feed-forward neural network."""

    @abstractmethod
    def forward()
        """TODO"""
```

Reference: ArjanCodes. Why COMPOSITION is better than INHERITANCE - detailed Python example. 2021. [[YouTube]](https://youtu.be/0mcP8ZpUR38)

#### `NamedTuple` and `TypedDict`

***

## Protocol Buffers

Terms to know: .proto file, protocol buffer compiler, protcol buffer API, messages of a protocol buffer API

Protocol buffers are the flexible, efficient, automated solution to solve the problem of how to serialize and retrieve structured data between programming interfaces, e.g. C++ and Python.

#### How does a protocol buffer solve this problem?
A **protocol buffer compiler** creates a class that implements automatic encoding and parsing of the protocol buffer data with an efficient binary format. The generated class provides attributes and fields for the objects that make up a protocol buffer, abstracting away the complexity of reading and writing the protocol buffer as a unit.
- The protocol buffer format supports future development efforts by making it easy to extend the format over time in such that the code can still read data encoded with an  old format. 

#### Protocol Format


References:
- Google. Protocol Buffer Basics: Python [[docs]](https://developers.google.com/protocol-buffers/docs/pythontutorial)

***

## Miscellaneous

**Google Code Styling with YAPF**

Insall YAPF via pip: `pip install yapf`

To see usage instructions: `yapf --help`

**ML Finance Project**

[**example w/ multivariate time series in PyTorch**](https://stackabuse.com/time-series-prediction-using-lstm-with-pytorch-in-python/)

Q: Neural networks can be constructed using the `torch.nn` Python module.

Q: Import the package for constructing neural networks in PyTorch.

```python
import torch.nn as nn
```

Q: Seaborn comes with built-in datasets.

Q: Load seaborn’s flights dataset.

```python
flight_data = sns.load_dataset("flights")
```

Q: Why must time series data be scaled for sequence predictions? : When a network is fit on unscaled data, it is possible for large inputs to slow down the learning and convergence of your network and in some cases prevent the network from effectively learning your problem.

Q: What's the sklearn import for min-max scaling data?

```python
from sklearn import preprocessing
scaler = preprocessing.MinMaxScaler()
```

We know the field is fast moving. If the reader looking for more recent free reading resources, there are some good introductory/tutorial/survey papers on Arxiv

