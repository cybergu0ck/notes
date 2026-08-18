# Nodejs

**_Node.js is an asynchronous event-driven JavaScript runtime environment._**

- Node.js runs the V8 JavaScript engine, Google Chrome’s core, outside the browser.
- A Node.js app runs in a single process, without creating a new thread for every request.
- It is open source and cross-platform.

<br>
<br>

## Differences between Node.js and the Browser

- Browser and Node.js are Javascript runtime environments.

  | Aspect             | Browser                                                                                                                 | Node                                                                       |
  | ------------------ | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
  | Context of use     | Used fot client-side web development                                                                                    | Used for server side javascript and building applications outside browser. |
  | Environment        | Runs in the browser on the client-side.                                                                                 | Runs on the server or locally on your computer.                            |
  | DOM Manipulation   | Can manipulate the DOM                                                                                                  | Lacks a DOM                                                                |
  | Concurrency Model  | It is synchronous (Blocking) by nature but supports asynchronous operations through callbacks, promises and async/await | It is asynchronous (Non- Blocking) in nature                               |
  | Modules            | Supports ES Modules                                                                                                     | Supports both the CommonJS and ES module systems                           |
  | File System Access | Limited file system access for security reasons                                                                         | Full file system access                                                    |
  | Networking         | Can make HTTP requests and interact with external servers                                                               | Used for creating web servers and handling network requests                |

<br>
<br>
