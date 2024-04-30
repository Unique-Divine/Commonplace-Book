# Golang              <!-- omit in toc -->

- [Init](#init)
  - [1. Installation](#1-installation)
  - [2. Basics](#2-basics)
  - [Structures](#structures)
- [Debugging](#debugging)
- [Testing](#testing)

## Init

### 1. Installation

#### Installation with sudo: not recommended

To install go version 1.13 on linux:

```bash
sudo apt-get upgrade
sudo apt-get update
sudo apt-get install golang-go
```

After resetting the terminal window, run `go version` to verify that this worked properly.

To uninstall golang with sudo, use
```sh
sudo apt-get remove golang-go
sudo apt-get remove --auto-remove golang-go
```

Q: When might you want to uninstall golang on Ubuntu?  
A: If you find that `go version` and `sudo go version` are returning different results, you most likely have installed using `sudo apt-get` and it's causing problems. 

#### Installation 


Ref: https://sal.as/post/install-golan-on-wsl/

### 2. Basics

Write a hello world golang program:
```go
// hello.go
package main

import "fmt"

func main() {
  fmt.Println("Hello, 世界")
}
```

There's a similar function to `fmt.Println` called `println`. Why use `fmt`?

In the "Bootstrapping" section of the [spec](), it says that "Current implementations provide several built-in functions useful during bootstrapping. These functions are documented for completeness but are not guaranteed to stay in the language. They do not return a result."
"Thus, [functions like `println` that are built into the language] are useful to developers because they lack dependencies (being built into the compiler) but not in production code. It also important to note that print and println report to `stderr`, not `stdout`." - Alexander on StackOverflow

Q: Run a golang code file named `hello.go` without building.
Use `go run hello.go` at the command prompt.

Q: Run a golang code file, `hello.go`, saving the compiled result for later use.
Use `go build hello.go`.

Q: After compiling with `go build hello.go`, run the file by...
executing the binary file with `./hello` at the prompt

Q: Import the packages for dealing with the operating system and and printing formatted output.
```go
import (
  "fmt"
  "os"
)
```

All of your projects live in the same place, your workspace. By default, this is a folder called "go" in your user directory. You can check this location by running `go env GOPATH`.

Functions start with the `func` keyword.

Write a function that sums two integers.

```golang
func sum(x: int, y: int) int {
  return x + y
}
```

Initialize a variable `powerLevel` to 5 with explicit typing.
```golang
var powerLevel int = 5
```

Initialize a variable `powerLevel` to 5 with implicit typing.
```golang
powerLevel := 5
```

Write conditional logic that prints "oof" if `x` is greater than 0.
```golang
if x > 0 {
  fmt.Println("oof")
}
```

Write conditional logic that prints "whale" if `x` is greater than 10, "minnow" if `x` is less than 1, and "shark" otherwise.
```golang
if x > 10 {
  fmt.Println("whale")
} else if x < 1 {
  fmt.Println("minnow")
} else {
  fmt.Println("shark")
}
```

Create and an array, "point", that holds 2 ints.
```golang
var point [2]int
```

Create a slice of ints called "arr".
```golang
var arr []int
```

What will this function return?
```golang
func foo() {
  var arr []int
  return arr
}
```
A: An empty slice, `[]`.

Write the type definition for a dictionary that maps strings to integers.
`map[string]int`

Write the type definition for a dictionary that maps `wallet` (`Wallet`) to `balance` (int).
`map[Wallet]int`

Declare a dictionary variable, `strIntMap`, that maps strings to integers.
```golang
var strIntMap map[string]int
```

Def: To **Declare** a variable is to introduce the variable to the program by defining its type and name.

**Assigning to a variable** means providing the variable with a value.

To **initialize** a variable is to assign the variable with an intitial value.

**Instantiate** means to "create an instance of".

Will the following code run?
```golang
func main() {
  var facts map[int]string
  facts[0] = "False"
  facts[1] = "True"
  fmt.Println(facts)
}
```
A: No, you'll get `panic: assignment to entry in nil map` because that's not how to initialize a map in go. You must use `make`: `make(map[int]string)`.

Initialize a dictionary, `goku`, that maps "powerLevel" to 9001.
```golang
var goku = make(map[string]int)
goku["powerLevel"] = 9001
```

Q: What's another way to write this that will work?
```golang
var facts = make(map[int]string)
```

A:
```golang
facts := make(map[int]string)
```

How do you delete the "age" key-value pair?
```golang
var goku = make(map[string]int)
goku["powerLevel"] = 9001
goku["age"] = 40
```
A: `delete(goku, "age")`

Cl: The `delete` method operates on `map`s.

Q: Print the values 0 through 4 going incrementing by 1.
```golang
func main() {
  for i := 0; i < 4; i++ {
    fmt.Println(i)
  }
}
```

Q: Initalize a slice, `letters`, containing the letters "a", "b", "c"
```golang
arr := []string{"a", "b", "c"}
// var arr = []string{"a", "b", "c"}
```

Q: Given that `arr := []string{"a", "b", "c"}`, iterate through the slice printing the indices and values.
```golang
for index, value := range arr {
  fmt.Println(index, value)
}
```

Given that
```golang
goku := make(map[string]int)
goku["powerLevel"] = 9001
goku["age"] = 40
```
Iterate through the dictionary printing the keys and values.
```golang
for key, value := range goku {
  fmt.Println(key, value)
}
```

Q: What method allows you to take the square root of a number?
A: `math.Sqrt`

Q: Create a "person" struct with name (string) and age (int) fields.
```golang
type person struct {
  name string
  age int
}
```

Given the "person" struct, initialize Naruto at age 22.
```golang
type person struct {
  name string
  age int
}
```

```golang
naruto := person{name: "Naruto", age: 22}
fmt.Println(naruto)
```

Q: If I give you a variable `x := 7`, how do you find its memory address?
A: `&x`

  
### Structures

<!-- Anki placeholder -->

Q: GO is not an object-oriented language like C++ or Java.

Q: Define a `Saiyan` structure with a name (string) and power (int).

A:
```golang
type Saiyan struct {
    name string
    power int
}
```

Q: Initialize a `Saiyan`, "Goku", with a power of 9001.

```golang
type Saiyan struct {
    name string
    power int
}
```

A:
```golang
goku := Saiyan{
    name: "Goku",
    power: 9001,
}
```


Q:

```golang
type Saiyan struct {
    name string
    power int
}
```

Is it valid to write the following?
```golang
goku := Saiyan{}
// or
goku := Saiyan{name: "Goku"}
```

A: Yes, structures can have unassigned fields just like variables can have unassigned values.

Cl: Structures can have unassigned fields just like variables can have unassigned values.

Cl: Go passes arguments to a function as copies.

Q: What does the following print?
```golang
package main

import "fmt"

type Saiyan struct {
  name  string
  power int
}

func main() {
  goku := Saiyan{"Goku", 9000}
  Super(goku)
  fmt.Println(goku.power)
}

func Super(s Saiyan) {
  s.power *= 2
}
```

A: Still 9000 because only the copy of `goku` became super, not the original variable. Changes made in `Super` weren't reflected in the caller.

Q: 

```golang
type Saiyan struct {
  name  string
  power int
}

func main() {
  goku := Saiyan{"Goku", 9000}
  Super(goku)
  fmt.Println(goku.power)
}

func Super(s Saiyan) {
  s.power *= 2
}
```

Q: If you have an interface, `Spec`, and want to verify that the type, `MyType`, implements `spec`, how can you check this at compile time?

```go
var _ Spec = (*MyType)(nil)
```

This will error at compile time: 
```
prog.go:23: cannot use (*MyType)(nil) (type *MyType) as type Spec in assignment:
    *MyType does not implement Spec (missing Method method)
 [process exited with non-zero status]
```

Q:  `*MyType` means pointer to `MyType`.


## Bytes in Go

## Debugging

```shell
go mod tidy
```

Opens permissions for the go directories that were unable to see the staandard library dependencies.

```shell
chown -R realu:realu $GOPATH
```


```shell
go clean -modcache
```


## Testing

#### Testify assert vs. require

In the [stretch/testify](github.com/stretchr/testify) package, the two packages "assert" and "require" can both be used to give a flavor of assert statements. 

```golang
import (
  "github.com/stretchr/testify/assert"
  "github.com/stretchr/testify/require"
)
```

Q: When is it better to use require versus assert?

It depends on the behavior you need. You get a log entry for each assertion with `assert`. However with `require`, the first failed requirement interrups and fails the complete test. This means that any requirements after the first failed one won't be evaluated; they'll be skipped.


Q: Test all go files visible from the current path.
```sh
go test ./...
```

To test with code coverage:
```sh
go test ./... -cover
```

