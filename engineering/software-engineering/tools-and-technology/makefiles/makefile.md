# Makefile

makefile is a script used to automate the build process of a software project.

<br>
<br>

## Alternatives

- Alternatives for C/C++ build systems are SCons, CMake, Bazel and Ninja.
- Microsoft Visual Studio has its own build tool.
- Java has Ant, Maven and Gradle.
- Interpreted languages like Python, Ruby, Javascript do not need to be recompiled.

<br>
<br>

## Makefile Syntax

A Makefile consists of a set of rules.

<br>

### Rule

A rule specifies how to build a target from its prerequisites and may include one or more commands to execute.

```
targets: prerequisites
    command
    command
    command
```

<br>

### Command

- A command in a makefile rule is a series of shell commands that are executed to update the target.
- These commands must be indented with a TAB (NOT space!) and are executed in the order they are listed in the makefile.

<br>

### Target

A target is a file or a concept that the make utility is supposed to update.

- It represents the result of a build process.
- Targets can be executables, object files, libraries, or any other files

<br>

### Prerequisites

Prerequisites are dependencies for a target. They are files or other targets that must exist before the target can be built.

- "Prerequisites" are also called as "Dependencies".

- If a prerequisite doesn't exist then make will search for explicit rule to build that prerequisite (a target with the name of that prerequisite), If such a rule is present in the Makefile it will build it first and then execute the original target.

  ```makefile
  final.txt: starter.txt
      cat starter.txt >> final.txt

  starter.txt: content.txt
      touch starter.txt
      cat content.txt >> starter.txt

  content.txt:
      touch content.txt
      echo "Simulating some addition of content." >> content.txt
  ```

  - The order of execution in terms of targets will be content.txt, starter.txt and then final.txt as seen in the output.

        ```
        touch content.txt
        echo "Simulating some addition of content." >> content.txt
        touch starter.txt
        cat content.txt >> starter.txt
        cat starter.txt >> final.txt
        ```

- make might use a default implict rule in some instances where there the prerequsite and any explicit rule for it doesn't exist.

  ```makefile
  blah: blah.o
      g++ -o blah.exe blah.o
  ```

  - Consider the above Makefile with only blah.cpp in the filesystem, make will not throw an error even though blah.o doesn't exist and nor does any rule for building blah.o . It will use default implicit rule for compiling and linking cpp files and then execute the command for target blah.

<br>
<br>

## Working Principle of make

1. make compares the timestamps of the target and its prerequisites. If a prerequsisite has been modifed more recently than the target or if the target doesnt exist, make considers the target to be out-of-date.

2. If the target is out-of-date, make executes the commands associated with the rule to update the target.

<br>

### Illustartion

```cpp
//blah.cpp
#include <iostream>

int main(){
    std::cout << "blu bla blah" << "\n";
    return 0;
}
```

- Consider this Makefile with 1 target having no dependency.

  ```makefile
  blah:
      g++ -Wall -std=c++14 blah.cpp -o blah
  ```

  - When we run `make`, it creates a the "target" named "blah".
  - If we run `make` again, it doesn't run the commands as the "target" already exists.
  - The cpp file will NOT be recompiled (the command for the target in the Makefile will execute) even if changes are made to the cpp file as the **target blah** has NO dependency in the Makefile.

- Consider the following Makefile with the target having the dependency.

  ```makefile
  blah: blah.cpp
      g++ -Wall -std=c++14 blah.cpp -o blah
  ```

  - The cpp file will be recompiled (the command for the target in the Makefile will execute) every time it is modified (Technically, whenever the timestamp is changed.) as the **target blah** has a **dependency blah.cpp**.

<br>
<br>

## Make Clean

clean is often used as a target to remove the output of other targets.

```makefile
blah.exe: blah.o
	g++ -o blah.exe blah.o

blah.o: blah.cpp
	g++ -c blah.o blah.cpp

clean:
	rm -f blah.exe blah.o
```

<br>
<br>

## Variables

Variables in Makefile can only be strings.

```makefile
files := blah.o #files will be set to blah.o

blah.exe: ${files}
	g++ -o blah.exe ${files}

blah.o: blah.cpp
	g++ -c blah.o blah.cpp

clean:
	rm -f blah.exe blah.o
```

- Variables are set using `:=` or `=`.
- Variables are referenced using `${}` ir `$()`.
- Single or Double quotes have no meaning to Make.

  ```makefile
  files := 'blah.o' #Bad Practice; files will be set to "'blah.o'"
  ```

<br>
<br>

## Wildcard

### `*` Wildcard

- `*` may be used in the target, prerequisites or in the wildcard function.

- When `*` matches no files, it is left as it is, unless run in the wildcard function. 

  ```makefile
  #Without wildcard function, it'll throw an error for zero matches
  print: *.py 
    ls -la $?
  ```

  ```
  make: *** No rule to make target '*.py', needed by 'print'.  Stop.
  ```
- Hence it is a good practice to use the wildcard function.

  ```makefile
  print: ${wildcard *.py}
    ls -la $?
  ```
  ```
  ls -la 
  total 0
  ```

<br>

### `%` wildcard

`%` has variety of usecases.

- When used in "matching" mode, it matches one or more characters in a string. This match is called the stem.
- When used in "replacing" mode, it takes the stem that was matched and replaces that in a string.