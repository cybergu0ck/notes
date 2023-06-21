# Files, Streams and IO

- list of header files

  | Header File | Description                                                              |
  | ----------- | ------------------------------------------------------------------------ |
  | iostream    | Provides definitions for formatted input and output from/to streams      |
  | fstream     | Provides definitions for formatted input and output from/to file streams |
  | iomanip     | Provides definiton for manipulators used to format stream I/O            |

* classes

  | class        | Description                                                                                                   |
  | ------------ | ------------------------------------------------------------------------------------------------------------- |
  | ios          | Provides Basic support for formatted and unformatted I/O operations. Base class most other classes.           |
  | ifstream     | Provides for High level input operations on file based streams.                                               |
  | ofstream     | Provides for high level output operations on file based streams.                                              |
  | fstream      | Provides for high level I/O operations on file based streams. (Derived from ifstream and ofstream)            |
  | stringstream | Provides for high level I/O operations on memory based strings (Derived from istringstream and ostringstream) |

* global stream objects

  | Object | Description                                                                              |
  | ------ | ---------------------------------------------------------------------------------------- |
  | cin    | standard input stream, connected to keyboard by default                                  |
  | cout   | standard output stream, connected to console by default                                  |
  | cerr   | standard error stream, connected to console by default (instance of ostream, unbuffered) |
  | clog   | standard log stream, connected to console by default (instance of ostream, unbuffered)   |

<br>
<br>
<br>

# Manipulating Booleans

- Once the manipulator is set, it is done for all the subsequent lines too.

* The following code will make the booleans to be strings (true and false)

  ```cpp
  std::cout << std::boolalpha;
  std::cout.setf(std::ios::boolalpha);
  ```

* The following code will make the booleans to be integers (1 and 0)

  ```cpp
  std::cout << std::noboolalpha;
  std::cout << std::resetiosflags(std::ios::boolalpha);
  ```

* Check out this illustration

  ```cpp
  #include <iostream>
  #include <iomanip>

  int main()
  {
      std::cout << (10 == 10) << std::endl;	//1
      std::cout << std::boolalpha;
      std::cout << (10 == 20) << std::endl;	//false
      std::cout << (100 == 100) << std::endl; //true
      std::cout << std::noboolalpha;
      std::cout << (100 == 20) << std::endl;  //0
  }
  ```

  <br>
  <br>
  <br>

# Manipulating integers

- Note that we are manipulating how the data is displayed in the console and not the values stored in the variables!
- `#include <iostream>` and `#include <iomanip>` must be included for the following illustrations.

- base is decimal by default.

  ```cpp
  int num{ 255 };
  std::cout << std::dec  << num << std::endl; //255, this is default!
  ```

* we can modify the base with which it is displayed

  ```cpp
  int num{ 255 };
  std::cout << std::hex << num << std::endl; //ff
  std::cout << std::oct << num << std::endl; //377
  ```

* we can show the base in which the number is displayed.
  ```cpp
  int num{ 255 };
  std::cout << std::showbase;  //to not show base use std::noshowbase
  std::cout << std::dec << num << std::endl; //255
  std::cout << std::hex << num << std::endl; //0xff
  std::cout << std::oct << num << std::endl; //0377
  ```
* we can show the sign when displaying

  ```cpp
  int num{ 255 };
  std::cout << std::showpos;   //to not show sign use std::noshowpos
  std::cout << std::dec << num << std::endl; //+255
  std::cout << std::hex << num << std::endl; //ff
  std::cout << std::oct << num << std::endl; //377
  ```

<br>
<br>
<br>

# Manipulating floating point numbers

- By default the console displays floats upto 6 digits (precesion is 6 by default) and rounding always occurs.

  ```cpp
  float num{ 123.2688 };
  std::cout << num << std::endl;	//123.269, precesion is 6 by default
  ```

  ```cpp
  double num{ 1234444.2688 };
  std::cout << num << std::endl;	//1.23444e+06, precesion is still 6 using scientific notation!
  ```

* We can set the precesion

  ```cpp
  float num{ 123.2688 };
  std::cout << std::setprecision(4);
  std::cout << num << std::endl;	//123.3, precesion is set to 4
  ```

* we can set the precesion to the right of the decimal point.

  ```cpp
  float num{ 123.2688 };
  std::cout << std::fixed;
  std::cout << num << std::endl;	//123.268799, it maintains the precesion (default 6 here) to the right of decimal point.

  std::cout << std::setprecision(2);
  std::cout << num << std::endl;	//123.27, precesion (2 here) to the right of the decimal point.
  ```

* We can force scientific notation

  ```cpp
  float num{ 124.268 };
  std::cout << std::setprecision(2) << std::scientific;
  std::cout << num << std::endl;	//1.243e+02
  ```

* To unset these flags, check online or docs.

<br>
<br>
<br>

# Modifying allignment

- We can set the field width which will apply an allignment(space on left by default) only for the consecutive element (not all the subsequent elements)

<br>
<br>
<br>

# Reading from text file

- It will read characters until whitespace.

  ```cpp
  #include <iostream>
  #include <fstream>

  int main()
  {
    std::ifstream in_file{ "myfile.txt" };  //std::ios::in is not necessary as ifstream is inherintly for input!
    //std::ifstream in_file{ "myfile.txt", std::ios::in };
    std::string file_content;
    in_file >> file_content;
    std::cout << file_content << std::endl;		//larry
    in_file.close();
  }
  ```

- To read a full line from a file, we use getline(), note we must include string library for this

  ```cpp
  #include <iostream>
  #include <fstream>
  #include <string>

  int main()
  {
    std::ifstream my_file{ "myfile.txt" };
    std::string line;
    std::getline(my_file, line);
    std::cout << line << std::endl; //larry is first among them
    my_file.close();
  }
  ```

<br>
<br>

> When we create an ifstream (or fstream or ofstream) objects with the filename in it's initialization, then it'll be opened then itself. Else we can create the object without the initialization and then after having gotten the filename we can use the open function to open the file.

<br>
<br>
<br>

# Writing to files

- output files will be created if they are not present, if present they'll be overwritten/truncated (if not explicitely mentioned)
- Can be opened in text and binary modes.
- Can be opened so that new content is appended.

<br>

- `std::ios::out` (this was refered as a flag) must be used when using fstream

  ```cpp
  std::fstream outfile1{ "myfile.txt", std::ios::out };		//text mode (default)
  std::fstream outfile2{ "myfile.txt", std::ios::out | std::ios::binary };	//binary mode
  ```

- `std::ios::out` is optional when using ofstream

  ```cpp
  std::ofstream outfile3{ "myfile.txt" }; //std::ios::out is optional here
  std::ofstream outfile4{ "myfile.txt", std::ios::binary };
  ```

- We can choose to overwrite or append

  ```cpp
  std::ofstream outfile5{ "myfile.txt", std::ios::trunc }; //truncate or overwrite when writing
  std::ofstream outfile6{ "myfile.txt", std::ios::app }; //append on each write
  std::ofstream outfile7{ "myfile.txt", std::ios::ate }; //seek to the end of stream when opening
  ```

* We can open a file later on using open() and the filename as argument. In the following illustration, we create an ofstream object without any initialisation, we get the filename from the console and then we can open the file

  ```cpp
  #include <iostream>
  #include <fstream>
  #include <string>

  int main()
  {
    std::ofstream outfile;
    std::string filename;
    std::cin >> filename;

    outfile.open(filename);  //outfile.open(filename, std::ios::binary) for binary mode
  }
  ```

<br>

### Making sure the file is opened correctly

- This can be done using is_open()

  ```cpp
  if (file.is_open())
  {
    //do something
  }
  else
  {
   //do something
  }
  ```

* We can use the file object itself

  ```cpp
  if(file)
  {
    //do something
  }
  else
  {
    //do something
  }
  ```

<br>

### Always close the file

- Don't forget to close the file

  ```cpp
  file.close()
  ```
