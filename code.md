# Code Commonplace <!-- omit in toc -->

#### Table of Contents<!-- omit in toc -->
- [Data Structures & Algorithms (DSA)](#data-structures--algorithms-dsa)
  - [List-Based Collections](#list-based-collections)
    - [Linked lists](#linked-lists)
    - [Stacks](#stacks)
- [Python](#python)
  - [Standard Libarry](#standard-libarry)
    - [Reading and Writing Files](#reading-and-writing-files)
  - [Writing Tests](#writing-tests)
  - [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
    - [Abstract Base Classes](#abstract-base-classes)
    - [Data classes](#data-classes)
    - [Prefer composition over inheritance](#prefer-composition-over-inheritance)
  - [Miscellaneous](#miscellaneous)
- [Databases, SQL, DBMS](#databases-sql-dbms)
  - [Database Crash Course](#database-crash-course)
- [Web development](#web-development)
  - [Hugo Web Design](#hugo-web-design)
  - [HTTP, TCP, IP](#http-tcp-ip)
  - [HTML, CSS](#html-css)
- [Git](#git)
  - [Fundamental Concepts](#fundamental-concepts)
  - [Branching](#branching)
  - [Special Topics](#special-topics)
- [Misc.](#misc)
  - [C++](#c)
  - [Design Patterns](#design-patterns)


<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

---

# Data Structures & Algorithms (DSA)

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

Algorithm
: A fancy word for a simple thing: A program that solves a problem.


Algorithms topics
- Sorting: Insertion sort, merge sort, divide and conquer, quicksort, counting sort, Radix sort
- Stacks, queues
- Heaps, heapsort
- Binary search trees, Red-black trees
- Graphs, Breadth-first search, Depth-first search
- Shortest paths, Negative cycles, All-pairs shortest paths
- Hashing
- NP-Completeness
- Linked lists, arrays
- Greedy algorithms
- Dynamic programming

Introduction to Algorithms by Thomas H Cormen, Charles E Leiserson, buncha others (third edition)

#### Why study data structures and algorithms (DSA)?

> "4.5 years of learning programming and working as fullstack software engineer ... had interview with one of the FAANG companies this summer in Hong Kong but failed it due to the fact that I suck in DSA (Data Structures & Algorithms)."

> "I’m using to leetcode.com to learn data structures and algorithms since I got a rejection from FAANG after interviewing with them onsite."

[Role of DSA in Programming (July, 2020)](https://blog.codechef.com/2020/07/24/the-role-of-data-structure-and-algorithms-in-programming/)

---

## List-Based Collections

---

<!-- blurb on CSLists -->

An array (`CSArray`) is an ordered collection of elements that each have an address called an index.

### Linked lists

Python lists aren't lists in the traditional computer science sense. That would be a linked list. A **linked list** is a data structure consisting of a collection of nodes which together represent a sequence. 
- Linked lists are ordered like arrays, but there are no indices. The order is purely kept by the links.
- Each node is unaware of its location in the linked list because it's unindexed. The nodes are also unaware of how long the list is.

A **singly linked list** is a sequence of **nodes**. Each node in a singly linked list holds a value and keeps reference to the next node. This reference is the single link.

Q: Implement a `dataclass` for a node of a **singly** linked list.

```python
import dataclasses
from typing import Any, Optional

@dataclasses.dataclass
class Node:
    """Node of a singly linked list."""
    value: Any
    next: Optional['Node'] = None
```

A **doubly linked list** is a sequence of nodes that each hold a value and keep a reference to both the previous and next node. 

Q: Implement a `dataclass` for a node of a **doubly** linked list.

```python
import dataclasses
from typing import Any, Optional

@dataclasses.dataclass
class DLNode:
    """Node of a doubly linked list."""
    value: Any
    next: Optional['DLNode'] = None
    prev: Optional['DLNode'] = None
```

- [ ] Q: Similar to the array, the linked list is a linear data structure. What makes it linear?

The **head node** of a linked list is the first, or outermost, node. Singly and doubly linked lists can be implemented based just on the head node.

Q: Write a method-less class for a singly linked list.
```python
@dataclasses.dataclass
class Node:
    value: Any
    next: Optional['Node'] = None

@dataclasses.dataclass
class LinkedList:
    head: Node

    # ... methods
```

Q: Using the above `LinkedList` and `Node` classes, create a linked list instance that describes `"a" → "b" → "c"`, where arrows represent the node pointers and "a".

```python
ll = LinkedList(head = Node('a', Node('b', Node('c'))))
```

Insert an element at the beginning of a linked list.

### Stacks

Stacks are also list-based data strucures. Imagine a stack of pancakes. You can keep stacking elements on top and have easy access to the top-most element. 

Adding an element to a stack is called **pushing** and taking an element from the top of a stack is called **popping**. Both `Stack.pop` and `Stack.push` are $O(1)$ (constant time).

The value and pointers of the elements aren't specified by a stack, meaning that stacks can actually be implemented as linked lists, where the top of the stack is the head of a singly linked list. It just needs to have methods for adding and removing elements.

You may see the notation L.I.F.O. associated with stacks. It stands for "Last In, First Out". The last element pushed is the first one popped.

Python lists (PyList) have stack functionality built in with `PyList.pop()` and `PyList.append()`. 

---

#### DSA Resources: 

- Python implementations of tons of algorithms: https://github.com/TheAlgorithms/Python/blob/master/DIRECTORY.md
- Udacity course: https://classroom.udacity.com/courses/ud513/lessons/7174469398/concepts/71201055390923
- Python Algorithms book

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

---

# Python

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->


## Standard Libarry 

---

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
- Mode `'a'`: For appending data to the end of 'file'. 
- Mode `'w'`: For writing only. An existing file with the same name as 'file' will be erased.
- Mode `'r+'`: opens a file for both reading and writing.

Q: Why use the `with` keyword with the `open` method?

It is good practice to use the `with` keyword when dealing with file objects because the file will be properly closed after its suite finishes even if an exception is raised at some point. Using `with` is also much shorter than writing equivalent `try-finally` blocks.

```python
with open(file="some_file") as file:
    pass
file.closed
```
`True`

- Python glossary - file object [[docs]](https://docs.python.org/3/glossary.html#term-file-object)

Date: 21年6月

<!-- -------------------------------- -->

---

## Writing Tests 

---

<!-- -------------------------------- -->


#### Disabling warnings

To ignore pytest warnings at the command line: 
`pytest -p no:warnings`

See: https://docs.pytest.org/en/latest/how-to/capture-warnings.html#disabling-warnings-summary


<!-- -------------------------------- -->

---

## Object-Oriented Programming (OOP)

---

<!-- --------------------------------  -->

### Abstract Base Classes

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

### Data classes

Python's `dataclass` functionality allows you to write shorter code and initialize, print, compare, and order data much more easily. 

Why use data classes?

A class for a data container is often used differently. Many instances may need to be made. You probably want to order them, compare them, easily inspect the data inside them, etc. 

Regular classes don't provide much built-in convenient functionality for data oriented classes. Classes that build around a behavior may not have as many instances or be conducive to representing data structures. Because of this, some programming languages provide a type of class that is better tuned to storing data, e.g. C#'s struct type that is good for representing data structures. 

##### Simplest data class: All required arguments

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

Implement this as a `dataclass`:
```python
from dataclasses import dataclass

@dataclass
class Person:
    """A person that has a name, job, and age."""
    name: str
    job: str
    age: int
```

##### Data class with default arguments

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

##### Data class with attributes that depend on other parameters

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

### Prefer composition over inheritance

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

---

## Miscellaneous

#### ML Finance Project

#### [example w/ multivariate time series in PyTorch](https://stackabuse.com/time-series-prediction-using-lstm-with-pytorch-in-python/)

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

Q: Why must time series data be scaled for sequence predictions?
: When a network is fit on unscaled data, it is possible for large inputs to slow down the learning and convergence of your network and in some cases prevent the network from effectively learning your problem.

Q: What's the sklearn import for min-max scaling data?
```python
from sklearn import preprocessing
scaler = preprocessing.MinMaxScaler()
```

We know the field is fast moving. If the reader looking for more recent free reading resources, there are some good  introductory/tutorial/survey papers on Arxiv

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

---

#  Databases, SQL, DBMS

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

## Database Crash Course

#### Overview: SQL, Databases, and Spreadsheets
- High-level overview of database architecture
- What is a database?
- Where are databases powerful and where are they not?
- What is SQL?

SQL is a programming language used to interact with nearly all relational databases. SQL was first developed at IBM in the 1970s with major contributions from Oracle. Many extensions to SQL have been created since then. 

Spreadsheets (such as Microsoft Excel) differ from databases in that spreadsheets were originally designed for one user. They're great for smallers numbers of users who don't need complicated data manipulation. Databases, on the other hand, are designed to hold massive amounts of information and allow multiple users to quickly and securely access and query data with potentially complex logic all in real time. 

The strong suit of a database is not storage. It's search functionality. Or more correctly, a database's strength is the search functionality granted to it by a database management system (DMBS). 

- **Database management system (DBMS)**: A piece of software that manipulates a database such as SQL, MongoDB, PostgreSQL, MySQL, etc.

- **Structured Query Language (SQL)** is not a programming language in the normal sense. Instead, it's a **decorative, or declarative, programming language**, which means that you simply express what you want done. How it actually happens is not a big concern. A decorative programming language does things and then gives you what you want. Contrast this with a procedural language such as C++ or Python where the programmer writes step-by-step instructions in a program to exactly define *how* to accomplish a task. 
 
#### Relational vs. non-relational database:

SQL is the standard language for communicating with **relation database management systems (RDBMS)** such as Oracle, Microsoft SQL Server, PostegreSQL, and MySQL.

A **relational database** is structured, meaning the data is organized in tables. Often, the data within the tables of a relational database have relationships with one another, also called dependencies. On the other hand, a **non-relational database** is document-oriented, which means that all of the information gets stored within a single construct, or document, for each item in the database.  

SQL databases: 
- SQL databases are relational.
- SQL is short for Structured Query language. 
- PostgreSQL and MySQL are examples of SQL databases.

NoSQL Databases:
- NoSQL databases are non-relational.
- A NoSQL databases is less structured and less confined in format, thus allowing for more flexibility and adaptability.
- MongoDB is an example of a NoSQL database.

A database contains one or more tables. Tables have named columns with types like "text" or "number". Tables are like pd.DataFrames. 
- **Schemas** categorize the tables in a relational database.
- Each row in a table is called a **record** and each column is called a **field**.
- **Metadata** describes the structure of the data itself, such as the field length and datatype. Ex. in a company database the value 6.95 stored in a field is data about the price of a specific product. The information that this is a number data stored to two decimal places and valued in dollars is metadata.

#### Primary and composite keys

Usually in each table, we will have an ID called a **primary key**. The primary key uniquely identifies rows. This is usually a special ID or a name. 

We can also create a **composite key**, or composite primary key, which uses a combination of two or more values to identify rows. For example, let's say we're storing IDs for people. People are likely to have matching names, but it is unlikely that people have the same name, height, and address, so we could use these values with a composite key to uniquely identify people. 

#### SQL Syntax & Structure

Query
: A statement written in SQL, which may include commands and actions. To access records in a table, you send requests in the form of queries.

SQL has 3 categories of syntax terms: identifiers, literals, and keywords.
- **Identifier** (SQLSyntaxTerm): A unique identifier for an element in a database system. If a database contains a table called "Cars", then "Cars" is the identifier.
- **Literal** (SQLSyntaxTerm): A data value.
- **Keyword** (SQLSyntaxTerm): One of the words that has meaning to the system itself, e.g. `SELECT`, `WHERE`, `AND`, `FROM`, etc. 

#### SELECT statement

Simple SQL statements to create, modify, and read. Assume that you have two populated SQL databases with some information. 

Q: Return all rows from table `aTableName`:
```sql
SELECT * FROM aTableName
```
- `*`: indicates all columns


Q: Return all rows from columns `col1`, and `col2` of table `aTableName`:
```sql
SELECT col1, col2 FROM aTableName
```

Q: Return all rows from table `aTableName` with condition `col1 > 5`.
```sql
SELECT * FROM aTableName
WHERE col1 > 5;
```
- The above  code is spread accross two lines. SQL does not worry about line breaks. It only pays attention to semi-colons to end statements. You could even put `SELECT *` on its own line, for instance. 
- If you had a second condition (e.g. `col2 < 4`), you could **filter** for that too using the `AND` statement: 
  ```sql
  WHERE <condition1> AND <condition2> 
  ```

To add new items into the database, we use the `INSERT` command. Add 12 to `col1` and "ab" to `col2` of table `aTableName`:
```sql
INSERT INTO aTableName (col1, col2)
VALUES (12, "ab");
```

**Predicates** can be used in cmbination with `SELECT` to limit the number of records retrieved. The default predicate used is `ALL`, meaning the the following two statements are equivalent.

```sql
SELECT col1, col2 
FROM aTable
```

```sql
SELECT ALL col1, col2 
FROM aTable
```

`DISTINCT` is a predicate keyword for returning unique entries.

Q: Return the unique values of column `CarBrand` in the `Cars` table.
```sql
SELECT DISTINCT CarBrand
FROM Cars
```

Q: What happens if you include more than one column after `SELECT DISTINCT`?

`DISTINCT` basically eliminates duplicate values. When you query additional columns, it will return records that are distinct with respect to the each column. For example, 
```sql
SELECT DISTINCT FirstName, Role
FROM Coworkers
```
will only discard records that have the same "FirstName" and "Role". If two  co-workers have the same first name and different job titles, that counts as a distinct record, so there will be a duplicate entry in the first column.

<!-- continue with TOP, page 31 -->

### Miscellanous Database Topics <!-- omit in toc -->

#### Databases vs. Spreadsheets

Example: Suppose you're opening an online specialty cat store. You open a spreadsheet and track name, product, product, date, address, and quantity of items purchased as your variables for bookkeeping. This might work for a while with a small number of customers, products, and addresses listed. However after a while, the online store gets more popular and you run into issues when one customer, Jane Doe, has multiple addresses listed, when different customers share the same name, and in other messy situations. Customers might get mixed up and the wrong products might get sent to the wrong people. How do you resolve this?

Instead of having one spreadsheet, you separate different related information into database **tables**. For the cat store, we might have a "Customers" table, a "Products" table, and an "Orders" table. This separates the data in a much more efficient way. Now, if Jane changes addresses or phone numbers, her contact information simply gets updated in the "Customers" table. The "Product" table can keep track of all cat inventory. Each product will be listed along with its price, quantity, type, and a unique product ID. The "Orders" table would keep track of every sale you make. 

You can see that these tables must be connected to one another. It's these connections that form what we call a database. This system is much more scalable and efficient than the spreadsheet, however databases aren't the best for visualizing the connections between tables. It's all in the programming language of the database management system and difficult to see where improvements should be made.

This is where **entity relationship** diagrams (ERDs) come in. These are a way of visualing database structure. Each table is translated into an entity. Columns within each table are listed as **attributes**. In the previous example, the entities were customer, product, and order. The customer table has attributes such as customer ID, name, address, and phone number. The connections between different tables are visualized through **relationship lines**.


#### Data persistence

Persistence in modern English is defined as follows: 
1. Continued or prolonged existence of something. Ex. "the persistence of huge environmental problems". 
2. Firm or obstinate continuance of a course of action in spite of difficulty or opposition. "Companies must have patience and persistence".

In the context of data storage in computer systems, **persistence refers to a type of storage where data survives after its creation process has ended**. A data store is considered persistent if it writes to non-volatile storage.

Persistence, or the **persistence mechanism**, is also a term used in cyber security. Once malware gains access to a system, it looks to persist within the system. Malware with persistence has more potential to exploit the system and can sometimes continue to act after restarts and reboots. So what then is a persistence layer?

**Persistence layer**: Any software layer that makes it easier for a program to persist its state is generally called a persistence layer. Persistence layers usually do not achieve persistence *directly* but through the use of an underlying database management system. Persistence layers are also referred to as data access layers.

The persistence layer is usually a relational database in the data access object pattern, but it can be any persistence mechanism using an abstract API. The function os such an API is to hide all of the complexities of performing CRUD (Create, Read, Update, Delete) operations in the underlying storage mechanism from the application. 

**Create, Read, Update, Delete (CRUD)**: These are the four basic operations of persistent storage. 

**Database management system**: A database management system (DBMS) is a software system that enables users to define, create, maintain, and control access to a database. Examples of DBMS's include MySQL, PostgreSQL, Microsoft SQL Server, and many others. 

##### Why use a persistence layer?
Separating data access and the database engine from business/application logic allows you to easily migrate to different storage engines. Isolating the database logic in a single layer makes it easier to replace and modify in the future. In short, persistence layers make maintenance and extension easier.

source: [Oracle. What is a Database?](https://www.oracle.com/database/what-is-database/)

##### References

- Lucidchart, 2018. Database Tutorial for Beginners [[video]](https://youtu.be/wR0jg0eQsZA)
- 0612 TV w/ NERDfirst, 2017. A Database Crash Course! [[video]](https://youtu.be/0hKmmh_4t7w)
- Followup tutorial on entity relationship diagrams (ERDs): https://www.youtube.com/watch?v=QpdhBUYk7Kk
- Connolly, Thomas M.; Begg, Carolyn E. (2014). Database Systems – A Practical Approach to Design Implementation and Management (6th ed.). Pearson. ISBN 978-1292061184
- Data access object. [[Wikipedia]][wiki-DAO]. 
- Persistence (computer science). [[Wikipedia]][wiki-persistence].

[wiki-DAO]: https://en.wikipedia.org/wiki/Data_access_object#:~:text=In%20computer%20software%2C%20a%20data,exposing%20details%20of%20the%20database.
[wiki-persistence]: https://en.wikipedia.org/wiki/Persistence_(computer_science)#:~:text=complicated%20to%20debug.-,Persistence%20layers,an%20underlying%20database%20management%20system.



Chapters that look interesting from databases book: Worlds of Database Systems, Relational Model of Data, High-Level Database models, Databse Language SQL, Semistructured Data Model

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

---

#  Web development

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

## Hugo Web Design

Start Sep 16 (Mike Dane Tutorial Series)

#### Intro to Hugo -[(video)](https://youtu.be/qtIqKaDlqXo) 

- Hugo is a static site generator.
- Static website generators allow you to compromise between writing a bunch of static html pages and using a heavy, and potentially expensive, content management system.
- Why Hugo? It's extremely fast.
- 2 kinds of websites, dynamic and static. Dyanmic ex. Facebook. Facebook pages are dynamically generated for each user. For static websites, what you see is what you get.
- Static websites are notoriously harder to maintain b/c you lack some of the flexibility of things on a dynamic site. Usually you can't use much conditional logic, functions, or variables.
- However, static pages are extremely fast.
- Hugo is great for a blog, portfolio website, etc.
- Hugo doesn't explicity require you to write a single line of HTML code.
- Flexibility \| With that said, if you want to go in and change every little detail of the layout of the site, you cna do that. You can write as much of the HTML and have as much control as you'd like.
- Hugo is 100% free and open-source.

#### Intalling Hugo on Windows - [(video)](https://youtu.be/G7umPCU-8xc?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3) 

-   Mine's already installed. I'll skip this for now.
-   a
-   a

#### Creating a new site - [(video)](https://youtu.be/sB0HLHjgQ7E?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3) 

-   skip, a bit too easy

#### Installing & Using Themes - [(video)](https://youtu.be/L34JL_3Jkyc?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3) 

-   my themes are already installed

#### Creating & Organizing Content - [(video)](https://youtu.be/0GZxidrlaRM?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3) 

-   Hugo has 2 types of content: single pages and list pages
-   List content lists other content on the site. You can call this a list page.
-   Individual blog posts are single pages.
-   Your posts should not just be in the content directory. They should be in directories inside the content directory.

-   A list page is automatically created for directories inside thecontent folder. Hugo automatically does this. Note, this only occursfor directories at the "root\" level of the content directory. Forexample: `content/post/` would generate a list page at`site.com/post/`, but `content/post/dir0` would not.

-   If you want a list page to be generated for a dir that is not at theroot level of the content dir, you have to create an **indexfiled**, `_index.md`. For a convenient and efficient way to do thisfrom the cmd, use `hugo new post/dir0/_index.md` (above aboveexample), then there will be a list page for dir0. Content can alsobe added to`_index.md` and it should show up on the page.

-   Additionally, for list pages that are aautomatically generate by hugo, you can edit the content by adding an index.md to those as well. Ex. ` content/post/_index.md`.

#### Front Matter- [(video)](https://youtu.be/Yh2xKRJGff4?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3 ) 

- Front matter in Hugo is what is commonly called meta data.
- Front matter is data about our content files.
- The metadata automatically generated by Hugo at the top of md files when using `hugo new ` is front matter
- Front matter is stored in key-value pairs
- Front matter can be written in 3 different languages: YAML, TOML, and JSON
- The defualt lang for front matter in Hugo is YAML
  - YAML - indicated by "--",
  - TOML - indicated by \"+++\" and uses \"=\" instead of \":\",
  - JSON - indicated by 
- You can create your own custom front matter variables.

Front matter is super powerful in its utility.

#### Archetypes - [(video)](https://youtu.be/bcme8AzVh6o?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3 ) 

-   How does the default front matter from using `hugo new  .md` get selected? Short answer: archetypes
-   An archetype is basically the default front matter template for when you create a new content file.
-   Archetypes are modified under `static/themes/archetypes/default.md`
-   Suppose your content dir has a subdirectory, `content/dir0`. If you wanted to create an archetype for the files in dir0, you'd simply create `dir0.md` inside the archetypes dir.

#### Shortcodes - [(video)](https://youtu.be/2xkNJL4gJ9E?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3 ) 

-   Shortcodes are predefined chunks of HTML that you can insert into your markdown files.

-   Let's say you have a md file that you want to spice up by adding in some custom HTML. For instance, maybe you'd like to embed a YouTube video. Normally this would require lots of HTML that you'd have to paste it. Shortcodes can allow you to sidestep this. Hugo comes with a YouTube video shortcode predefined.

-   General shortcode syntax `< shortcode_name param0 >`

-   Youtube shortcode \| For a YouTube video with url, `youtube.com/watch?v=random-text\`, the shortcode we'd use to embed would be `< youtube random-text >` because "random-text" is the id of the youtube video and the only parameter for that shortcode.

#### Taxonomies - [(video)](https://youtu.be/pCPCQgqC8RA?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3 )

-   Taxonomies in hugo are basically ways that you can logically group
    different pieces of content together in order to organize it in a
    more efficient way.

-   Hugo provids 2 defualt taxonomies: tags & categories

-   All taxonomy information is declared in front matter. In YAML, tags
    has the syntax `tags: ["tag0", "tag1", \ldots]`

#### Templates - [(video)](https://youtu.be/gnJbPO-GFIw)

-   Templates here mostly refers to HTML templates. If you're not
    comfortable writing HTML, CSS, and coding for the web, templates
    might be a little bit above your head.

-   A hugo theme is actually made up of hugo templates.

-   Any template that you use in Hugo is going to be inside
    `themes/theme-name/layouts`. This is where all the templates live.

-   ` /layouts/default` usually contains a default style for list and
    single pages by use of `list.html` and `single.html`.

#### List Templates - [(video)](https://youtu.be/8b2YTSMdMps)

-   List templates give default HTML layout to list content files.

-   .

#### Resources 

- [A clear and concise beginner hugo tutorial](https://www.linkedin.com/learninglearning-static-site-building-with-hugo-2/build-a-static-site-with-hugoresume=false)
- [CSS Crash Course for Absolute Beginners](https://youtu.be/yfoY53QXEnI)

## HTTP, TCP, IP

#### HTTP

HTTP = Hypertext Transfer Protocol

HTTP is a protocol that allows the fetching of resources such as HTML
documents. It allows web-based apps to communicate and exchange data.

HTTP is a client-server protocol. This means requests are initiated by a
recipient, usually the web browser, and a complete document is
constructed from the files fetched such as text, layout description,
images, videos, scripts, etc.

-   The client is the one making the request.

-   The server responds to this request.

##### Three important things about HTTP 

1.  HTTP is connectionless: After making the request, the client disconnects from the server. Then when the response is ready, the server re-establishes the connection again and delivers the response.
2.  HTTP can deliver any sort of data.
3.  HTTP is stateless: The client and server know about each other only during the current request. If the current request closes and the two computers want to connect again, they need to provide information to each other anew. In other words, statelessness means that the connection between the browser and the server is lost once the transaction ends.

To learn about requests and repsonses:
<https://youtu.be/eesqK59rhGA?t=275>

#### TCP/IP

The internet protocol suite is the conceptual model and set of
communications protocols used in the internet and similar computer
networks. It is commonly known as TCP/IP because the foundational
protocols in the suite are the Transmission Control Protocol (TCP) and
Internet Protocol (IP).

Communication prootocl: A system of rules that allow two or more
entitites of a communications system to transmit information via any
kind of variation of a physical quantity.

##### Internet Protocol (IP): {#internet-protocol-ip .unnumbered}

IP has the task of delivering packets from from the source host to the
destination host solely based on the IP addresses in the packet headers.
For this purpose, IP defines packet structures that encapsulate the data
to be delivered.It also defines addressing methods that are used to
label the datagrame with source and destination information.

- (network) packets: Formatted units of data carried by a packet-switched network. A packet consists of control information and user data; the latter is also known as the payload. Control information provides data for delivering the payload (e.g. source and destination network addresses, error detection codes, or sequencing information).

Q: What's an IP address?

An Internet Protocol address, or IP address, is a numerical label assigned to each device connected to a computer network tha tuses the Internet Protocol for communication.

##### Bandwitdth (computing): 

(Computing) bandwitdth is the maximum rate of data transfer across a
given path. Bandwidth can be characterized as network bandwidth, data
bandwidth, or digital bandwidth.

Computing bandwidth is different from the bandwidth defined in the field
of signal processing, signal bandwidth. Signal bandwidth is the
frequency range between lowest and highest attainable frequency while
meeting a well-defined impairment level in signal power. It's measured
in hertz.

In relation to internet protocol, we often talk about consume dbandwidth
in bit/s, which corresponds to achieved throughput or goodput, i.e. the
avg rate of successful data transfer through a communication path.

Q: Why is network bandwidth an average rate instead of a current rate?

A channel with $v_\beta$ may not necessarily transmit data at $v_t$ rate
since protocols, encryption, and other factors can add overhead. For
instance, internet traffic often uses TCP, which requires a three-way
handshake for each transaction. TCP is efficient, but it does add
significant overhead compared to simpler protocols. Additionally, data
packets may be lost, further reducing the data throughput.

Packet loss?
: Packet loss occurs when one or more packets of data travelling across a
computer network fail to reach their destination. Packet loss is either
caused by errors in data transmission, typically across wireless
networks, or network congestion. Packet loss is measured as a percentage
of packets lost with respect to packets sent.

Packet switching
: Packet switching is a method of grouping data that is transmitted over a
digital netowrk into packets. Packets are made of a header and a
payload. Data in the header is used by networking hardware to direct the
packet to its destination, where the payload is extracted and used by
application software. Packet switching is the primary basis for data
communications in computer networks worldwide.

#### Resources {#resources-1 .unnumbered}

-   <https://en.wikipedia.org/wiki/Internet_protocol_suite>

-   .

## HTML, CSS



<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

---

# Git

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

Git (cookbook)

## Fundamental Concepts

#### Local branch vs. remote branch

- **local branch**: a branch only the local user can see. It exists only on your local machine.
  - Ex. Create local branch named "myNewBranch": `git branch myNewBranch`

- **remote branch**: a branch on a remote location (in most cases 'origin'). Local branches can be pushed to 'origin' (a remote branch), where other users can track it.
  - Ex. Push local branch, "myNewBranch", to the remote, "origin" so that a new branch named "myNewBranch" is created on the remote machine ("origin"):  
  `git push -u origin myNewBranch`

- **remote tracking branch**: A local copy of a remote branch. When 'myNewBranch' is pushed to 'origin' using the command above, a remote tracking branch named 'origin/myNewBranch' is created on your local machine.
- **local tracking branch**: a local branch that is tracking another
branch.

source(s): [SNce & Brian Webster.stackoverflow.com](https://stackoverflow.com/questions/16408300/what-are-the-differences-between-local-branch-local-tracking-branch-remote-bra)

#### HEAD, master, and origin

I highly recommend the book "Pro Git" by Scott Chacon. Take time and
really read it, while exploring an actual git repo as you do.

- **HEAD**: the current commit your repo is on. Most of the time HEAD points to the latest commit in your current branch, but that doesn't have to be the case. HEAD really just means "what is my repo currently pointing at".  
  In the event that the commit HEAD refers to is not the tip of any branch, this is called a "**detached head**".
- **master**: the name of the default branch that git creates for you when first creating a repo. In most cases, "master" means "the main branch". Most shops have everyone pushing to master, and master is considered the definitive view of the repo. But it's also common for release branches to be made off of master for releasing. Your local repo has its own master branch, that almost always follows the master of a remote repo.
- **origin**: the default name that git gives to your main remote repo. Your box has its own repo, and you most likely push out to some remote repo that you and all your coworkers push to. That remote repo is almost always called origin, but it doesn't have to be.
- `HEAD` is an official notion in git. `HEAD` always has a well-defined meaning. `master` and `origin` are common names usually used in git, but they don't have to be.

source: [HEAD, master, and origin. Matt Greer & Jacqueline P. via
stackoverflow.com](https://stackoverflow.com/questions/8196544/what-are-the-git-concepts-of-head-master-origin)

---

## Branching

Suppose your application is stable. Later, you discover a gigantic bug
that was passing silently. You want to write some tests, fix the bug,
and eventually have a stable, passing application once again. To do
this, you'd create a branch for the fix and push the branch to the
remote so that all of the developers on your team can collaborate and
make the fix.

Once all of the necessary changes have been made and the application is
stable, someone from the team would commit merge the commits from the
other branch into master. Since the commit history from the branch will
have been saved to master, the new branch could be deleted without loss
of information (if you no longer wanted to work on this branch).

View branches:  `git branch`

Switch branches:  `git checkout [branch-name]`

#### Merging

Merge the specified branch's history into the current one.
`git merge [branch]`

#### Deleting branches

Delete local branch
`git branch -d [branch-name]`

Delete remote branch
`git push origin --delete [branch-name]`

---

#### Git flow

<!-- TODO: Write about git-flow and branching models  -->

When working on a new feature, branch off from the `develop` branch:  
```
git checkout -b newFeature develop
```

Merge finished features into the development branch to add them to the upcoming release. Use the "no fast forward" flag, `--no-ff`, to cause the merge to create a new commit object even if the merge could be performed with a fast-forward. This avoids losing information about the historical existence of a feature branch and groups together all commits that together added the feature.
```
git checkout develop
git merge --no-ff newFeature
git branch -d newFeature
git push origin develop
```

---

## Special Topics

#### SSH keys

An SSH key is an alternative to username/password authorization on
GitHub. This will allow you to bypass entering your username and
password for future GitHub commands.

SSH keys come in pairs, a public key that gets shared with services like
GitHub, and a private key that is stored only on your computer. If the
keys match, you're granted access.

The cryptography behind SSH keys ensures that no one can reverse
engineer your private key from the public one.

[SSH Keys for GitHub [article]](https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html)

Generating a new SSH key: Follow [Generating a new SSH key and adding it to the ssh-agent [article]](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

#### Permanently removing files from commit history

WHy do this? You may have commited a password, some other sensitive
information, or a large file that you want to remove from github. If the
change is only a few commits back, you can "rebase" changes out of the
history. I actually need to do this for a much older set of files and
accidentally uploaded a textbook that takes up almost a GB of space.

`git filter-branch --force --index-filter "git rm --cached --ignore-unmatch PathToSensitiveFile" --prune-empty --tag-name-filter cat -- --all`

All you need to change is the `PathToSensitiveFile` item. Once you've used this command for all of the files you'd like to get rid of, update the origin by typing `git push origin --force --all`.

#### Large File Storage

See https://git-lfs.github.com

##### References:
- A successful Git branching model. [[web]](https://nvie.com/posts/a-successful-git-branching-model/)


<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

---

#  Misc. 

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

## C++ 


C++ source code files end with a .cpp extension.

Hello world program: Run these and find out which one works.
```cpp
#include <iostream>;

int main() 
{
  std::cout << "Hello, world!";
  return 0;
}
```

Compiling and executing the C++ program:

1.  Step 1 is to install the gcc compiler.
2.  Verify the install of g++ and gdb with `whereis g++` and `whereis gdb`. To install gdb (linux or WSL), use `sudo apt-get install build-essential gdb`.

##### [Open MP](https://www.openmp.org//wp-content/uploads/openmp-examples-4.5.0.pdf)

People use OpenMP for shared memory parallelization. To import:
```cpp
#include <omp.h>;
```

#### Header files

C++ programs consist of more than just .cpp files. They also use **header files**, which can have a .h extension, .hpp extension, or even none at all.

Q: What is a `.h` file?
: header file

Q: What is the purpose of a header file?  
: Header files allow us to put declarations in one location and then import them wherever we need them. This can save a lot of typing in multi-file programs.

What’s contained in a `.h` file?

..

#### References & Further Reading

- [C header files](https://www.tutorialspoint.com/cprogramming/c_header_files.htm)
- [learncpp.com/.../header-files](https://www.learncpp.com/cpp-tutorial/header-files/)


---

## Design Patterns

Why use "design patterns"?

- Design patterns let your write better code more quickly by providing a clearer picture of how to implement the design
- Design patterns encourage code reuse and accomodate change by supplying well-tested mechanisms for delegation, composition, and other non-inheritance based reuse techniques
- Design patterns encourage more legible and maintainable code

Delegation? Composition?

- delegation: a pattern where a given object provides an interface to a set of operations. However, the actual work for those operations is performed by one or more other objects.
- composition: Creating objects with other objects as members. Should be used when a "has-a" relationship appears.

What are design patterns?

Which resources will you use to start learning about design patterns?

GOF patterns (C++). Then, potentially Head First Design Patterns (Java)/

#### References & Further Reading

[Introduction to Design Patterns Course](https://www.gofpatterns.com/design-patterns/module1/intro-design-patterns.php)

