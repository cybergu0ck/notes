# Python Namespaces

**_A namespace is a mapping from names to objects._**

- Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way (except for performance), and it may change in the future.
- Examples of namespaces are:
  - the set of built-in names (containing functions such as abs(), and built-in exception names);
  - the global names in a module;
  - In a sense the set of attributes of an object also form a namespace.
- The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits.

> The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; for instance, two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name.

The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called **main**, so they have their own global namespace. (The built-in names actually also live in a module; this is called builtins.)

<br/>
<br/>
<br/>
