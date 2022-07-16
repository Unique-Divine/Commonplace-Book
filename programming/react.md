# React           <!-- omit in toc -->

- [React Introduction](#react-introduction)
  - [Scaffolding React Apps](#scaffolding-react-apps)
  - [Functional Components](#functional-components)
  - [Props](#props)
- [Event Handlers: onClick, onBlur, and onChange](#event-handlers-onclick-onblur-and-onchange)
- [Hooks: useState, useContext, useEffect, and useRef](#hooks-usestate-usecontext-useeffect-and-useref)
  - [`useState` hook](#usestate-hook)
  - [Sharing State](#sharing-state)
  - [`useRef` hook](#useref-hook)
  - [`useMemo` hook](#usememo-hook)
- [Context and the `useContext` hook](#context-and-the-usecontext-hook)
- [Resources](#resources)
- [Debugging](#debugging)

## React Introduction

Q: What is a React in one sentence?  
A: React is a declarative and flexible JS library for building user interfaces that lets you compose complex UIs from isolated pieces of code called "components".

In the statement,
```js
class ShoppingList extends React.Component {
  // ...
}
```
'ShoppingList' is a `React.Component` type. A `React.Component` takes in parameters called `props` (short for "properties").

**JSX**: React developers use a special syntax called "JSX" to make structures (e.g. `<div />` or `h1`) easier to write. Any JavaScript expression that is put within braces can be used in JSX, giving it the full power of JavaScript.

- JSX is likely short for JavaScript XML.

CLOZE: Each React element is a JavaScript object that you can store in a variable or pass around in your program.

Q: What's a functional component?

A funtional component is a function that takes a `props` object as an argument and returns valid JSX.

### Scaffolding React Apps

#### Scaffolding a fresh app

**Scaffolding a JavaScript template**: If you have NodeJS installed, you can scaffold a React App with the following command.
NOTE, a React application exists in a folder that has no capital letters and no spaces.
```sh
npx create-react-app app-name
```

Noteworthy App directories
- By pathing into `public` directory, you can and view the `index.html` file. This contains your scaffolded React App and a single `div` element called "root".
- The `src` folder contains all of your JS and CSS code.  
- `index.js` is where the application starts.


Add the following to the top of `index.js` in the `src/` directory.
```js
import React from 'react';
import ReactDOM from 'react-dom';
```

**Scaffolding a TypeScript template**:  To instead scaffold with a typescript template, use 
```sh
npx create-react-app --template typescript app-name
```

Current progress in React TS tutorial: https://youtu.be/jrKcJxF0lAU?t=1031

### Functional Components

Functional components are functions isolated in their own jsx or tsx files that return some HTML. 

Here's an example of a minimal functional component that returns a `div` JSX element. You need to import React at the tp of the application for the JSX to be recognized properly.
```ts
// Greeting.tsx
import React from 'react';

export const Greeting = () => {
  return <div>Hello, World!</div>;
};
```

Now, you can import this component in your App.tsx and use it. It has the look and feel of an HTML tag.
```ts
// App.tsx
import React from 'react';
import { Greeting } from './Greeting';

function App() {

  return (
    <div className="App">
      <Greeting />
    </div>
  );
}

export default App;
```

You could also import this component into other React files. Components are composable and can utilize other components. Splitting your app up with them can help you write more modular code.

You can see this minimal application display by running `yarn start`.

### Props

Props, short for properties, are basically what enables you to pass in arguments to a React.Component. 

If we wanted to pass a name to the `Greeting` component in the [Functional Components](#functional-components) section, we could pass a "name" property to the element in App.tsx, then create access the name via an attribute of the `props` object.
```ts
// inside the return block of App()
<Greeting name="Alice"/>
```

```ts
// Greeting.tsx
export const Greeting = (props) => {
  return <div>Hello, {props.name}!</div>;
}
```

Equivalently, we can use what is known as object deconstruction to grab attributes directly from the argument.
```ts
// Greeting.tsx
export const Greeting = ({name}) => {
  return <div>Hello, {name}!</div>;
}
```
Object deconstruction is the more common way to get this behavior. 

## Event Handlers: onClick, onBlur, and onChange

- ANKI React events begin with the prefix "on".

https://youtu.be/m_477l0Er9w?list=PLL5bKmA1evMlBbH9_yxsydTmyrtnerCn4&t=410


## Hooks: useState, useContext, useEffect, and useRef

Q: What are React hooks?

React Hooks are functions that manipulate state variables of functional components, instrumenting the lifecycle methods of classes.

- ANKI React hooks begin with the prefix "use".

### `useState` hook

Q: `useState` is a hook that allows you to have state variables in functional components. 

Q: Arguments of `useState`? 

receives an argument for the initial state of a variable.  

Q: What does `useState` return?

1. The equivalent of one field of a class component's `this.state` object. In other words, the current value of a state variable
2. A function to update the state variable. The equivalent of `this.setState`.

Q: When should you use the `useState` hook?

When using a state variable scoped to a single component.

#### State

Each piece of state holds a single value, which could be an object or any other type.

When you use the `useState` hook, it only updates a single piece of state, equivalent to one field of `this.state`. 

```ts
class Message extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      message: '',
      list: [],    
    };
  }
  // ... */
}
```

```ts
const Message= () => {
   const [msg, setMsg] = React.useState( '' );
   const listState = React.useState( [] );
}
```

Q: When should you pass a function as the initial value for the `useState` hook? 

When the computation of this initial value may be expensive. This way, the initial value will be executed and assigned only on the initial render. On subsequent renders (due to change of state in the parent of current component), the argument of the `useState` hook will be ignored because the current value will be retrieved.

```ts
const Message = () => {
   const [msg, setMsg] = useState( () => expensiveComputation() );
   /* ... */
}
```

Q: Should you use `React.useState` with class components?

No, it should only be used in React functions.

Q: Can `React.useState` be used in regular JS functions that aren't called in a functional component?

No, it'll raise an error.


### Sharing State

Q: Do two coponents using the same custom hook share state? 

No. Custom hooks are a mechanism to reuse stateful logic, but every time you use a hook, the state and effects inside of it are isolated. 

> "Each call to a hook gets isolated state." - React docs

```ts
export function useCounter() {
  const [count, setCount] = useState(0);
  const decrement = () => setCount(count - 1);
  const increment = () => setCount(count + 1);
  const invert = () => setCount(count * -1);
  const reset = () => setCount(0);
  return {
    count,
    decrement,
    increment,
    invert,
    reset
  };
}

function ComponentFoo() {
  const counter = useCounter();
  return (
    <div>{counter.count} 
       <button> onClick={counter.increment}</button>
     </div>
  );
}

function ComponentBar() {
  const counter = useCounter();
  // ...
  return (
    <div>{counter.count} 
       <button> onClick={counter.decrement}</button>
     </div>
  );
}
```

Here, the buttons of `ComponentFoo` and `ComponentBar` change different counters because each call of the `useCounter` hook creates a fresh copy of `count`.


### `useRef` hook

### `useMemo` hook


`useMemo` is a hook that returns a value that only recomputes when one of its dependencies has changed.
Q: dependencies?
Q: What recomputes?

> "side effects belong in `useEffect`, not `useMemo`"
Q: What does this mean? Why is it true?


## Context and the `useContext` hook

Typically react components pass data top-down from parent to child via props, but this way of passing data with props is cumbersome if the properties are required by many components. 
Context provides a way to pass data through the component tree without having to pass props down manually at every level. 

Q: When should you use `Context`?

Context is designed to share "global" variables for a tree of React components.

## Resources

- useRef: https://reactjs.org/docs/hooks-reference.html#useref
- useState: https://reactjs.org/docs/hooks-effect.html
- useEffect: https://reactjs.org/docs/hooks-reference.html#useeffect
- [useState in React: A complete guide](https://blog.logrocket.com/a-guide-to-usestate-in-react-ecb9952e406c)
- [The most important React concepts to learn first (as a beginner) - Web Dev Junkie](https://youtu.be/m_477l0Er9w?list=PLL5bKmA1evMlBbH9_yxsydTmyrtnerCn4)
- [Tutorial: Intro to React](https://reactjs.org/tutorial/tutorial.html) assumes no existing React knowledge.
- [A re-introduction to JavaScript (JS tutorial)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)
- [Learn React in 30 Minutes](https://youtu.be/hQAHSlTtcmY)
- [React Hooks Course - All React Hooks Explained](https://youtu.be/LlvBzyy-558)


## Debugging

If you see the error:
> Uncaught Invariant Violation: Invalid hook call. Hooks can only be called inside of the body of a function component. This could happen for one of the following reasons:
> 1. You might have mismatching versions of React and the renderer (such as React DOM)
> 2. You might be breaking the Rules of Hooks
> 3. You might have more than one copy of React in the same app
It could indicate that multiple versions of React are being used by different libraries in your application. To check if this is the case, use the list commands `npm ls` or `yarn list`.
I got this error from certain `@keplr-wallet` packages.

```sh
yarn list react
├─ @keplr-wallet/hooks@0.9.12-rc.3
│  └─ react@16.14.0
├─ @keplr-wallet/wc-qrcode-modal@0.9.12-rc.3
│  └─ react@16.14.0
└─ react@18.2.0
```

```sh
yarn list react-dom
├─ @keplr-wallet/wc-qrcode-modal@0.9.12-rc.3
│  └─ react-dom@16.14.0
└─ react-dom@18.2.0
```

