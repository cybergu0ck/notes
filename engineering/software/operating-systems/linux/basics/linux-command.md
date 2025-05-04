# Linux Command

A command can be one of four different things:

1. **An executable program** like all those files we saw in /usr/bin. Within this category, programs can be compiled binaries such as programs written in C and C++, or programs written in scripting languages such as the shell, perl, python, ruby, etc.
2. **A command built into the shell itself**. bash supports a number of commands internally called shell builtins. The cd command, for example, is a shell builtin.
3. **A shell function**. These are miniature shell scripts incorporated into the environment. We will cover configuring the environment and writing shell functions in later chapters, but for now, just be aware that they exist.
4. **An alias**. Commands that we can define ourselves, built from other commands.

<br/>
<br/>
<br/>

## Options and Arguments

- Commands are often followed by one or more options that modify their behavior and, further, by one or more arguments, the items upon which the command acts

  `command -options arguments`

- Many commmands also support long options with syntax:

  `command --longOptions arguments`

- Many commands allow multiple short options to be strung together. example:

  ```bash
  ls -la
  ```

<br/>

![image](./ImageRefs/lsOptions.png)

<br/>

## A Longer Look at Long Format

![image](./ImageRefs/ls-l.png)

- The meaning of each terms :

  ![image](./ImageRefs/ls-lMeaning.png)

<br/>
<br/>

<br>
<br>
<br>

## Type command

Display a command's type using `type`

```bash
type <command>
```

- Some Examples:

  ```bash
  type cd
  ```

  ```
  cd is a shell builtin
  ```

  ```bash
  type ls
  ```

  ```
  ls is aliased to `ls --color=auto'
  ```

<br/>
<br/>
<br/>

# Which command

Display an executable's location using `which`

```bash
which <executable>
```

- Some Examples:

  ```bash
  which ls
  ```

  ```
  /usr/bin/ls
  ```

* `which` only works with executables

<br/>
<br/>
<br/>

## Help commands

Getting help for shell builtins using `help`

```bash
help <shell_builtin>
```

<br>
<br>
<br

| Command   | Description                                        |
| --------- | -------------------------------------------------- |
|           |                                                    |
| `type`    | Indicate how a command name is interpreted.        |
| `which`   | Display which executable program will be executed. |
| `help`    | Get help for shell builtins                        |
| `apropos` | Display a list of appropriate commands             |
| `info`    | Display a command's info entry                     |
| `whatis`  | Display a very brief description of a command      |
| `alias`   | Create an alias for a command                      |
