



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

`sudo apt install npm`


#### References - Node JS

- Introduction to JavaScript Runtime Environments. [[codecademy]](https://www.codecademy.com/article/introduction-to-javascript-runtime-environments)
- kaizer1v. 2018. [[StackOverflow]](https://stackoverflow.com/questions/30838412/what-is-javascript-runtime#:~:text=Javascript%20runtime%20refers%20to%20where,on%20node%2C%20again%20its%20v8.)
- About npm. [[docs.npmjs]](https://docs.npmjs.com/about-npm)


### tsconfig.json

The tsconfig.json file allows you to specify the root level files and the compiler options that requires to compile a TypeScript project.

Compiler options

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



### AssemblyScript

Installation: 
```
npm install --save @assemblyscript/loader
npm install --save-dev assemblyscript
```

Graph TS
```
yarn add --dev @graphprotocol/graph-ts
npm install --save-dev @graphprotocol/graph-ts
```

Graph CLI
```
npm install -g @graphprotocol/graph-cli
yarn global add @graphprotocol/graph-cli
```
Enables `graph` commands 

Instructions here: [AssemblyScript API](https://thegraph.com/docs/en/developer/assemblyscript-api/)
1. Run `graph codegen`: This generates AssemblyScript types for a subgraph.

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

