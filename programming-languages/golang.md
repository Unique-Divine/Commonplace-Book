<!-- go.md -->
# Golang <!-- omit in toc -->

### Installation

On linux: 
```bash
sudo apt-get upgrade
sudo apt-get update
sudo apt-get install golang-go
```

After resetting the terminal window, run `go version` to verify that this worked properly.


Ref: https://sal.as/post/install-golan-on-wsl/


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
  return point
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

What's another way to write this that will work?
```golang
var facts = make(map[int]string)
```

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

Print the values 0 through 4 going incrementing by 1.
```golang
func main() {
  for i := 0; i < 4; i++ {
    fmt.Println(i)
  }
}
```

Initalize a slice, `letters`, containing the letters "a", "b", "c" 
```golang
arr := []string{"a", "b", "c"}
// var arr = []string{"a", "b", "c"}
```

Given that `arr := []string{"a", "b", "c"}`, iterate through the slice printing the indices and values.
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

