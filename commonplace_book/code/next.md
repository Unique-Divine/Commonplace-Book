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
