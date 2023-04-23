
# What are commands exactly?

A command can be one of four different things:

1. __An executable program__ like all those files we saw in /usr/bin. Within this category, programs can be compiled binaries such as programs written in C and C++, or programs written in scripting languages such as the shell, perl, python, ruby, etc.
2. __A command built into the shell itself__. bash supports a number of commands internally called shell builtins. The cd command, for example, is a shell builtin.
3. __A shell function__. These are miniature shell scripts incorporated into the environment. We will cover configuring the environment and writing shell functions in later chapters, but for now, just be aware that they exist.
4. __An alias__. Commands that we can define ourselves, built from other commands.

<br/>
<br/>

# Display a command's type using `type`

```bash
type <command>
```

* Some Examples: 

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

# Display an executable's location using `which`

```bash
which <executable>
```

* Some Examples: 
	```bash
	which ls
	```

	```
	/usr/bin/ls
	```

- `which` only works with executables


<br/>
<br/>

# Getting a command's documentation 

<br/>

## Getting help for shell builtins using `help`

```bash
help <shell_builtin>
```

