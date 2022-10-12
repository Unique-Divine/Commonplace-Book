# Typescript                <!-- omit in toc -->

#### Table of Contents
- [JavaScript](#javascript)
  - [Custom Errors](#custom-errors)
- [Types](#types)
- [Typescript Syntax](#typescript-syntax)
  - [JSON](#json)
- [Style](#style)
- [Tooling](#tooling)
  - [Node and npm](#node-and-npm)
  - [yarn](#yarn)
  - [tsconfig.json](#tsconfigjson)
  - [TypeScript Basics](#typescript-basics)
  - [Eslint and Prettier with TypeScript and React](#eslint-and-prettier-with-typescript-and-react)
  - [Apollo for GraphQL](#apollo-for-graphql)
  - [AssemblyScript](#assemblyscript)
  - [`depcheck` to track and remove unnecessary dependencies](#depcheck-to-track-and-remove-unnecessary-dependencies)
- [References](#references)

## JavaScript

If the `return` statement has no return value specified, `undefined` is returned instead. 


### Custom Errors

To write a custom error, a class should inherit from the built-in `Error` class.

```js
// The "pseudocode" for the built-in Error class defined by JavaScript itself
class Error {
  constructor(message) {
    this.message = message;
    this.name = "Error"; // (different names for different built-in error classes)
    this.stack = <call stack>; // non-standard, but most environments support it
  }
}
```

```js
class CustomError extends Error {
  constructor(message) {
    super(message); // (1)
    this.name = "CustomError"; // (2)
  }
}

function test() {
  throw new CustomError("Whoops!");
}

try {
  test();
} catch(err) {
  alert(err.message); // Whoops!
  alert(err.name); // CustomError
  alert(err.stack); // a list of nested calls with line numbers for each
}
```

1. JS requires calling the `super` fn in the child's `constructor`.
2. The parent constructor (for `Error`) sets the `name` property to "Error", so it has to be reset to the custom name manually.

Finally, a catch block that handles `CustomError` could look something like this:

```js
try {
  // ...
} catch (err) {
  if (err instanceof CustomError) {
    alert(err.message);
  } else {
    throw err; // unknown error, re-throw
  }
}
```

JOT more info here: https://javascript.info/custom-errors

## Types

#### Union type

A union type can be any one of some set of options.
```ts
type Response = "yes" | "no" | undefined
```

#### Intersection type

Intersecting types lets you define a type with both attributes. 

```ts
type Point = {x: number} & {y: number}
// equivalent to 
type Point = {x: number, y: number}
```
- [ ] TODO mine https://www.typescriptlang.org/cheatsheets
  - [ ] TODO mine control flow - https://www.typescriptlang.org/static/TypeScript%20Control%20Flow%20Analysis-8a549253ad8470850b77c4c5c351d457.png
  - [ ] TODO mine types - https://www.typescriptlang.org/static/TypeScript%20Types-4cbf7b9d45dc0ec8d18c6c7a0c516114.png
  - [ ] TODO mine interfaces - https://www.typescriptlang.org/static/TypeScript%20Interfaces-34f1ad12132fb463bd1dfe5b85c5b2e6.png
  - [ ] TODO mine classes - https://www.typescriptlang.org/static/TypeScript%20Classes-83cc6f8e42ba2002d5e2c04221fa78f9.png

## Typescript Syntax

Interfaces

Interfaces are like structures, or structs, in Go or abstract classes in Python (sort of). Anything that has the properties of the interface is compliant and considered an instance of it.

```ts
interface Point {
  x: number;
  y: number;
}

function move(pt: Point, dx: number, dy: number): Point {
  return {
    x: pt.x + dx, 
    y: pt.y + dy,
  }
};
```

TODO mine reference: https://stackoverflow.com/a/41915551

### JSON 

```ts
var pojo: Object 
JSON.stringify(pojo) // returns the JSON string compactly
JSON.stringify(pojo, null, 2) // JSON string with 2-space pretty formatting
```


## Style 

[Google Style Guide - JS](https://google.github.io/styleguide/jsguide.html#jsdoc)


JSDocs use Markdown syntax and special "tags" the begin with `@` such as `@param` and `@returns`. For example, 

```ts
/**
 * @fileoverview High-level description of the file.
 *
 * Heading for a bulleted list:
 * - item 0
 * - item 1
 */
```

[Top/file-level comments](https://google.github.io/styleguide/jsguide.html#jsdoc-top-file-level-comments)



## Tooling

### Node and npm


Q: What is Node.js?

An asynchronous event-driven JavaScript runtime. 

Q: What is a javascript runtime?

Javascript runtime refers to where your javascript code is executed when you run it. 

A JS runtime environment is where programs are executed. It determines what global objects a program can access and can impact how it runs. 

Q: Where can JS runtime environments execute code?

Two places: a browser's runtime env or the Node runtime env

Q: What is npm?

npm is the world's largest software registry. "npm" was originally short for Node package manager, and it's the default package manager for the JavaScript runtime environment, Node.js. npm, Inc. is the company behind the Node package manager, the npm Registry, and the npm CLI.  
- The npm registry is a large public database of JS software.

Installation

It is recommended to use a version manager for Node JS such as `nvm` [[github.com/nvm-sh/nvm]](https://github.com/nvm-sh/nvm). To install nvm, use cURL or Wget:
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```

```
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```

#### Install npm

On Ubuntu:  
`sudo apt install npm`


### yarn 

Install yarn with npm.
```sh
npm install -g yarn
```

#### References - Node JS

- Introduction to JavaScript Runtime Environments. [[codecademy]](https://www.codecademy.com/article/introduction-to-javascript-runtime-environments)
- kaizer1v. 2018. [[StackOverflow]](https://stackoverflow.com/questions/30838412/what-is-javascript-runtime#:~:text=Javascript%20runtime%20refers%20to%20where,on%20node%2C%20again%20its%20v8.)
- About npm. [[docs.npmjs]](https://docs.npmjs.com/about-npm)


### tsconfig.json

The tsconfig.json file allows you to specify the root level files and the compiler options that requires to compile a TypeScript project.

Compiler options

Q: What happens when you set `"type": "module"` in the `package.json`?

When you set `"type": "module"` in the `package.json` file, it specifies the project as an ES module. Omitting this from the `package.json` has the same effect as setting it to `"type": "commonjs"`, where JS files are treated as CommonJS.

Q: What is an ES module? And what is CommonJS?

The default behavior for Node.js is to treat JS code as CommonJS modules. Common JS modules are characterized by the `require()` statement for module imports and `module.exports` for module exports.

Example exports for a CommonJS module
```js
// util.js
module.exports.add = function(a, b) {
  return a + b;
} 
```

```js
const {add} = require('./util')

console.log(add(5, 5)) // 10
```


Q: When should one use CommonJS versus an ES module for a project?  





### TypeScript Basics

Q: Write a "hello, World!" program in Typescript.
```ts
let message: string = 'Hello, World!';
console.log(message)
```

Q: Compile and then run `code.ts`. 
```bash
tsc code.ts
node code.js
```
Alternatively, you can use `ts-node` if you installed it with `npm`.
```
ts-node code.js
```

Q: `tsc` stands for TypeScript Compiler.

### Eslint and Prettier with TypeScript and React

ESLint is a tool for identifying and reporting on patterns found in EMCAScript/JavaScript code with the goal ofmaking code more consistent and avoiding bugs. It is similar to JSLint in many ways.

[ESLint - Getting Started with ESLint](https://eslint.org/docs/latest/user-guide/getting-started)

### AssemblyScript

#### Install AssemblyScript 
```
npm install --save @assemblyscript/loader
npm install --save-dev assemblyscript
```

#### Install Graph TS
```
npm install --save-dev @graphprotocol/graph-ts
yarn add --dev @graphprotocol/graph-ts
```

#### Install Graph CLI
```
npm install -g @graphprotocol/graph-cli
yarn global add @graphprotocol/graph-cli
```
With `graph-cli` installed, you should be able to use `graph` commands after restarting the shell.

Instructions here: [AssemblyScript API](https://thegraph.com/docs/en/developer/assemblyscript-api/)
1. Run `graph codegen`: This generates AssemblyScript types for a subgraph. You can run this command in the same directory as the "subgraph.yaml" or specify the path manually using `graph codegen path/to/subgraph.yaml`.
  - Successful completion 

Q: What are the types `u8` and `u32`?  
These are `number` types corresponding to the common, unsigned integer types (8-bit unsigned integer) in WebAssembly. In `node_modules/assemblyscript/std/assembly`, they're defined like follows:
```ts
/** A 32-bit unsigned integer. */
declare type u32 = number;
```

Q: What is `usize` in AssemblyScript?  
A: A 32-bit unsigned ineger when targeting 32-bit Wasm or a uint64 when targeting 64-bit Wasm.

There's a common function used, "changetype" with the following syntax:

```ts
/* Changes the type of `usize` kind variable 'value' to another one of  `usize` 
  kind. Useful for casting class instances to their pointer values and 
  vice-versa. Beware that this is unsafe.
 */
declare function changetype<T>(value: any): T;
```

I saw this in contexts like the following: 
```ts
function changetype<Address>(value: any): Address
```



---

### `depcheck` to track and remove unnecessary dependencies

```sh
yarn global add depcheck # install
depcheck                 # usage
```

Ref: https://www.pluralsight.com/guides/how-to-remove-unused-dependencies-in-react


## References 

- [The `return` statement. MDN Web docs.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
