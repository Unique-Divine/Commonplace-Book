
### Building binaries

```bash
cargo build --release --out-dir . -Z unstable-options 
```

```toml
[[bin]]
# name of the output binary
name  = "run_sh" 
# path to the rust code that defines the binary.
# Execution logic is defined by `pub fn main`.
path = "src/run_sh.rs" 
```

### Testing

```rust

```

### ...

For viewing prints in a test run:

```rust
assert!(false, "Failed Successfully");
```

## Formatting Strings

Use the `format!` function to format strings directly.
Certain functions like `println!` also implement the format pattern.

```rust
let my_string = "Hello, World!";
println!("{}", my_string); // prints: Hello, World!
println!("{:?}", my_string); // prints: "Hello, World!"
```

Q: What's the difference between using `{}` and `{:?}` in format strings?

Use `{}` when you want the default user-friendly output, and `{:?}` when you want a more detailed output for debugging or development purposes.

- `{}`: This is for default formatting, typically used for user-facing output. It invokes the `std::fmt::Display` trait which formats the types in a way that is intended to be readable. Most standard library types implement this trait, but for user-defined types, you would need to manually implement `std::fmt::Display`.

- `{:?}`: This is for debug formatting and invokes the `std::fmt::Debug` trait. It's intended for debugging and development, providing a more detailed (and often multiline) representation of the value. All standard library types and most user-defined types implement this trait automatically when you derive it, but you can also manually implement it for more control over the output.

## Self, &self, and self

Q: What's the difference between these versions of "self", and when should you use
each one? 

On `self`:
- Refers to the instance of the type (analagous to `this` in TypeScript or
  Python's `self`).
- When defining functions for an `impl` block, you can use `&self`, `&mut self`,
  or just `self`.
  - If you're only reading from the object (the most common case), use `&self`, a
    "reference to self".
  - If you're modifying the object, use `&mut self`, a "mutable reference to
    `self`".
  - If you're consuming or transforming the object in such a way that the
    original object won't not be used afterward, use `self`, an "owned `self`".

On `Self`:
- Refers to the type itself rather than an instance of the type, especially in
  the context of trait and type definitions.
- `Self` is particularly useful in trait definitions where you don't know the
  implementing type yet. When a type implements the trait, `Self` will resolve to
  the implementing type.
