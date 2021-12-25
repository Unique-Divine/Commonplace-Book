# 💻 Code  <!-- omit in toc -->

## Code Commonplace

**Table of Contents**
- [Code Commonplace](#code-commonplace)
- [Data Structures & Algorithms (DSA)](#data-structures--algorithms-dsa)
- [Python](#python)
- [Databases, SQL, DBMS](#databases-sql-dbms)
- [Web development](#web-development)
- [Git](#git)
- [Misc.](#misc)
  - [C++](#c)
  - [Design Patterns](#design-patterns)

***

## Data Structures & Algorithms (DSA)

[data-structures-algorithms](data-structures-algorithms.md)

## Python

[programming-languages/python](programming-languages/python.md)

## Databases, SQL, DBMS

[databases-sql-dbms](databases-sql-dbms)

## Web development

[web-dev](web-dev-dns-http.md)

## Git

[git](git.md)

## Misc.


------------------------------------------------------------

### C++

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

1. Step 1 is to install the gcc compiler.
2. Verify the install of g++ and gdb with `whereis g++` and `whereis gdb`. To install gdb (linux or WSL), use `sudo apt-get install build-essential gdb`.

[**Open MP**](https://www.openmp.org/wp-content/uploads/openmp-examples-4.5.0.pdf)

People use OpenMP for shared memory parallelization. To import:

```cpp
#include <omp.h>;
```

**Header files**

C++ programs consist of more than just .cpp files. They also use **header files**, which can have a .h extension, .hpp extension, or even none at all.

Q: What is a `.h` file? : header file

Q: What is the purpose of a header file?\
: Header files allow us to put declarations in one location and then import them wherever we need them. This can save a lot of typing in multi-file programs.

What’s contained in a `.h` file?

..

**References & Further Reading**

* [C header files](https://www.tutorialspoint.com/cprogramming/c_header_files.htm)
* [learncpp.com/.../header-files](https://www.learncpp.com/cpp-tutoria/l/header-files/)

***

### Design Patterns

Why use "design patterns"?

* Design patterns let your write better code more quickly by providing a clearer picture of how to implement the design
* Design patterns encourage code reuse and accomodate change by supplying well-tested mechanisms for delegation, composition, and other non-inheritance based reuse techniques
* Design patterns encourage more legible and maintainable code

Delegation? Composition?

* delegation: a pattern where a given object provides an interface to a set of operations. However, the actual work for those operations is performed by one or more other objects.
* composition: Creating objects with other objects as members. Should be used when a "has-a" relationship appears.

What are design patterns?

Which resources will you use to start learning about design patterns?

GOF patterns (C++). Then, potentially Head First Design Patterns (Java)/

**References & Further Reading**

[Introduction to Design Patterns Course](https://www.gofpatterns.com/design-patterns/module1/intro-design-patterns.php)
