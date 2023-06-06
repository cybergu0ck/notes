> <br> C++ is a general-purpose programming language that supports procedural, object-oriented, and generic programming. <br> > <br>

<br>
<br>

# Procedural Programming

- procedural programming is basically a collection of functions, where data (usually declared seperately) are manipulated.
- limitations:
  - functions need to know the structure of data, if structure of the data is changed, then the function must also change for it to work.
  - as programs get large, it is difficult to understand, maintain, reuse, debug, extend.

<br>
<br>

# Object Oriented Programming

- Object-oriented programming (OOP) is a programming paradigm that uses "objects" – data structures consisting of data fields and methods together with their interactions – to design applications and computer programs.
- OOP in C++ is based on the concept of classes. A class is a blueprint for an object. It defines the data that an object will hold and the methods that an object will have.
- When you create an object, you are creating an instance of a class. The object will have its own copy of the data that is defined in the class, and it will be able to call the methods that are defined in the class.

- Advantages
  _ Abstraction : Abstraction is a process of hiding the implementation details of a system from the user, and only the functional details will be available to the user end.
  _ Encapsulation: Encapsulation is a method of wrapping up the data and code acting on the data into a single unit.
  _ Inheritence : Creating new classes by using the code present in already defined classes, extending the data.
  _ Polymorpism : Polymorphism is the ability to use the same code to operate on different types of objects. This makes the code more flexible.
  <br>

- Limitations:
  - OOP is not a panacea, it will bad code even worse XD
  - complicated design
  - slower and larger in size

<br>
<br>

# Classes and Objects

- Classes are user defined datatypes that act as a blueprints from which objects are created.
- Classes have attributes (data) and methods(functions).

<br>

- Objects are specific instance of a class, which has it's own identity.
- Objects have the attributes and can make use of the methods defined in the class.

<br>
<br>

# Class Declaration

- The syntax for declaring classes (Note the semi colon at the end).

  ```cpp
  class ClassName{
      //declaration(s)
  };
  ```

  ```cpp
  class Player {
  public:     //by default it'll be private!
      //attributes
      string name;
      int health;
      int xp;

      //methods
      void talk(string greeting_text) {
          cout << name << " says " << greeting_text << endl;
      }
      bool is_dead() {
          bool is_dead;
          if (health <= 0) {
              is_dead = true;
          }
          else {
              is_dead = false;
          }
      }
  };

  int main()
  {
      //class object
      Player frank;
      Player random_dude;

      //pointer to a class object
      Player* bad_guy = new Player();
      delete bad_guy;

      //array of class object
      Player players_arr[]{ frank, random_dude };

      //vector of class object
      vector<Player> players_vec{ frank};
      players_vec.push_back(random_dude);
  }
  ```

<br>
<br>

# Accessing Class Members

- An object can use the dot operator (.) to access the members of it's class.

  ```cpp
  int main()
  {
      Player jack;
      jack.name = "jack";
      jack.talk("Hello");

  }
  //jack saya Hello
  ```

- When using pointer to a class object, we can access the class members in two ways:

  1. Dereference the pointer and then use the dot operator.

     ```cpp
     int main()
     {
         Player* player = new Player();
         /*
         here player is not a Player object!
         it is a pointer pointing to a Player object dynamically allocated in heap memory.
         It is better to name this variable appropriately like player_ptr!
         It is named "player" for the purpose of explanation.
         */

         (*player).name = "Arrie";
         (*player).talk("Hey there");
     }

     //Arrie says Hey there
     ```

  2. Use the _member of pointer operator_ (arrow operator)

     ```cpp

     int main()
     {
         Player* player = new Player();
         /*
         here player is not a Player object!
         it is a pointer pointing to a Player object dynamically allocated in heap memory.
         It is better to name this variable appropriately like player_ptr!
         It is named "player" for the purpose of explanation.
         */

         player->name = "Arrie";
         player->talk("Hey there");
     }

     //Arrie says Hey there
     ```

<br>
<br>

# Class members acess modifiers

- C++ provides three kinds:

  1. public : accessible anywhere
  2. private : accessible only by members or friends of the class.
  3. protected : accessible by members of the class and members of derived class.(not accesible by objects of base and derived classes!)

<br>

- The syntax is:

  ```cpp
  class Class_Name{
      acess_modifier:  //public, private or protected
          //declarations
  };
  ```

- If no access modifier is specified, then the members are considered as private.
- The memeber methods in the class declaration always has access to to the member attributes!

<br>
<br>

# Implementing member method

- member methods can be implemented in two ways:

  1. can be implemented inside the class declaration. (implicitely inline)

     ```cpp
     class Account {
     private:
         double balance;	//this is not accessible anywhere outside this class
     public:
         double get_balance() {
             return balance;			//balance is acessible here even though it is private!
         }
         void set_balance(double bal) {
             balance = bal;			//same comment
         }
     };
     ```

  2. can be implemented outside the class declaration. (using scope resolution operator (::))

     ```cpp
     class Account {
     private:
         double balance;
     public:
         double get_balance();       //prototype
         void set_balance(double);   //prototype
     };


     void Account::set_balance(double bal) {
         balance = bal;
     }

     double Account::get_balance() {
         return balance;
     }
     ```

<br>
<br>

# Seperating Specification from Implementation

- We can seperate the class specification (declaration) from the implementation using header files
  - .h file for class declaration
  - .cpp file for the class implementation

<br>

- Consider the following header file that contains the declaration

  ```h
  //account.h

  #pragma once

  class Account {
  private:
      double balance;
  public:
      double get_balance();
      void set_balance(double);
  };
  ```

- the following source file contains the implementation

  ```cpp
  //account.cpp

  #include <iostream>
  #include "account.h"   //include the header!
  using namespace std;


  void Account::set_balance(double bal) {
      balance = bal;
  }

  double Account::get_balance() {
      return balance;
  }


  int main()
  {
      Account mine;
      mine.set_balance(100);
      cout << mine.get_balance() << endl;
  }
  ```

<br>

## Include Guards

- without include guards, the compiler will see the declaration everytime the header file is included in a file. (this is an error)
- there are two kinds:

  1. using `ifndef` directive preprocessor

     ```h
     #ifndef _ACCOUNT_H_  //this can be any unique name
     #define _ACCOUNT_H_

     //account class declaration

     #endif
     ```

  1. using `pragma` directive preprocessor

     ```h
     #pragma once

     //account class declaration
     ```

<br>
<br>

# Constructors

- constructor is a special member function that is invoked during object creation and hence we can use it for initialization.
- constructors must have the same name as the class.
- no return type is specified for constructors.
- constructors can be overloaded.

  ```cpp
  #include <iostream>

  class Player {
  private:
      int health{ 100 };
      int xp{ 0 };

  public:
      std::string name;

      //overloaded constructors
      Player() {
          std::cout << "constructor without any parameters is called for " << name << std::endl;
      }

      Player(std::string name) {
          std::cout << "constructor with name parameter is called for " << name << std::endl;
      }
  };


  int main()
  {
      Player superman{ "Kent Clark" };
      Player* player_ptr = new Player("Shaktiman");  //constructor for the Player object will be called
  }

  //constructor with name parameter is called for Kent Clark
  //constructor with name parameter is called for Shaktiman
  ```

<br>
<br>

# Destructors

- Destructors are also special kind of member function that is invoked automatically when the object is destroyed.
- Destructors have the same name as the class preceded by a tilde symbol (~)
- Destructors have no return type and no parameters.
- There can be only 1 destructor for a class hence it cannot be overloaded unlike constructors.
- They are used to release memory and stuff.

  ```cpp
  class Player {
  private:
      int health{ 100 };
      int xp{ 0 };

  public:
      std::string name;

      //overloaded constructors
      Player() {
      }

      Player(std::string arg) {
          name = arg;
      }

      //Destructor
      ~Player() {
          std::cout << "Desctructor called for " << name << std::endl;
      }
  };

  int main()
  {
      {
          Player first_player{ "batman" };
      }
      //desctructor will be called for batman as soon as the block scope ends i.e. here!

      {
          Player second_player{ "superman" };
          Player third_player{ "ironman" };
          Player fourth_player{ "cap america" };
      }
      //Notice the order of destrctor called!

      Player* player_ptr = new Player("Shaktiman");
    delete player_ptr;			//destructor for the player object is called
  }

  //Desctructor called for batman
  //Desctructor called for cap america
  //Desctructor called for ironman
  //Desctructor called for superman
  //Desctructor called for Shaktiman
  ```

<br>
<br>

# Default constructor

- If we donot specify any constructors ourselves, a no args default constructor will be created by compiler itself.

  ```cpp
  class Player {
  private:
      int health{ 100 };
      int xp{ 0 };

  public:
      std::string name;

      //no constructor is defined, hence no args default constructor will be created.
  };

  int main()
  {
      Player hero;
      hero.name = "Stuart";
      cout << hero.name << endl;
  }
  //Stuart
  ```

- If we create our own constructor(s), that will be called instead.

<br>
<br>

# Constructor initialiser list

- In the following code, we are actuallu assigning the values to the data members inside the constructor and not technically initialising.

  ```cpp
  class Player {
  private:
      int health;     //initialisation is done here
      int xp;

  public:
      std::string name;

      Player(string name_value, int health_value, int xp_value) {
          name = name_value;
          health = health_value;      //assignment
          xp = xp_value;
      }
  };

  int main()
  {
      Player hero{ "batman", 100, 100 };
  }
  ```

- To initialise the datamembers using constructors (see the constructor definition below). The order in which the parameters are initilaised is the order in which they are written in the class and not the paramter initialisation list in the constructor definition.

  ```cpp
  class Player {
  private:
      int health;
      int xp;

  public:
      std::string name;

      Player(string name_value, int health_value, int xp_value)
          : name{ name_value }, health{ health_value }, xp{ xp_value } {
              //we can write any code here and that will be executed
      }
  };

  int main()
  {
      Player hero{ "batman", 100, 100 };
  }
  ```

<br>
<br>

# Delegated constructors

Delegated constructors in C++ are a feature introduced in C++11 that allow a constructor to call another constructor of the same class. This can be useful for reducing code duplication and improving readability.

- Consider constructor initialisation list for overloaded constructors, this is lot if repeated code

  ```cpp
  class Player {
  private:
      int health;
      int xp;

  public:
      std::string name;

      //overloaded constructors

      Player()
          : name{ "None" }, health{ 100 }, xp{ 0 } {
      }

      Player(string name_value)
          : name{ name_value }, health{ 100 }, xp{ 0 }  {

      }

      Player(string name_value, int health_value, int xp_value)
          : name{ name_value }, health{ health_value }, xp{ xp_value } {
      }
  };
  ```

- We can reuse the code by using delegated constructors

  ```cpp
  class Player {
  private:
      int health;
      int xp;

  public:
      std::string name;

      //overloaded constructors
      Player(string name_value, int health_value, int xp_value)
          : name{ name_value }, health{ health_value }, xp{ xp_value } {
      }

      Player()
          : Player{"None",100,0} {
      }

      Player(string name_value)
          : Player{name_value, 100,0} {
      }
  };
  ```

<br>
<br>

# Copy Constructors

- A copy constructor in C++ is a special constructor that is used to create a new object that is an exact copy of an existing object. The copy constructor is called implicitly whenever a new object is created from an existing object of the same type.
- copy constructors are called when objects are passed into functions as parameters, because pass by value is default in C++.
- If we donot specify the copy constructor, the compiler calls a default copy constructor.
- It is good practice :
  - To define copy constructor when our class has raw pointer members.
  - provide the copy constructor with a const reference parameter.
  - avoid using raw pointer members as much as possible.

<br>

- The copy constructor is declared as follows:

  ```
  type::type (const type &source)
  ```

- Illustration of a copy constructor for the Player class

  ```cpp
  #include <iostream>
  using namespace std;

  class Player {
  private:
      int health;
      int xp;

  public:
      std::string name;

      //constructor prototype (notice we have used default values)
      Player(string name_value = "None", int health_value = 100, int xp_value = 0);

      //copy constructor prototype
      Player(const Player& source);
  };

  //constructor definition
  Player::Player(string name_value, int health_value, int xp_value) : name{ name_value }, health{ health_value }, xp{ xp_value }
  {
  }

  //copy constructor definition
  Player::Player(const Player& source) : name{ source.name }, health{ source.health }, xp{ source.xp }
  {
      cout << "copy constructor is called for : " << source.name << endl;
  }


  void foo(Player obj) {
      //just accepts the Player obj as a parameter
  }

  int main()
  {
      Player hero;
      foo(hero);  //copy constructor is called for : None
  }
  ```

- We can write the copy constructor using delegated constructor like:

  ```cpp
  Player::Player(const Player& source) : Player{ source.name, source.health, source.xp }
  {
      cout << "copy constructor is called for : " << source.name << endl;
  }
  ```

> <br> Add an image

<br>
<br>

# Shallow Copy with copy constructor

- If the class doesn't have raw pointers then the default copyconstructor provided by the compiler (that performs memberwise shallow copy) is sufficient.
- In the following code, when display_shallow method is called it creates a new Shallow object (to copy the argument obj1, here the data attribute is a pointer so the new Shallow object will store the address that the argument is pointing and not the actual data ) and when the control flow exits the display_shadow function (i.e. it's block scope) the descructor for that copy object is called and it'll free the heap memory but now the original obj1 is now pointing to invalid memory and the program crashes.

  ```cpp
  #include <iostream>
  using namespace std;

  class Shallow
  {
  public:
      int* ptr_data;

      Shallow(int value);                 //constructor prototype
      Shallow(const Shallow& source);     //copy constructor prototype
      ~Shallow();                         //descructor prototype
      void display_shallow(Shallow s);
  };

  Shallow::Shallow(int value)
  {
      ptr_data = new int;
      *ptr_data = value;
  }

  //copy constructor using parameter initialisation
  Shallow::Shallow(const Shallow& source) : ptr_data{source.ptr_data}
  {
      cout << "Copy constructor for Shallow copy" << endl;
  }


  Shallow::~Shallow()
  {
      delete ptr_data;
      cout << "Destructor frees the heap memory" << endl;
  }

  void Shallow::display_shallow(Shallow s)
  {
      cout << *(s.ptr_data) << endl;
  }

  int main()
  {
      Shallow obj1{ 100 };
      obj1.display_shallow(obj1);   //crashes the program hopefully

  }

  /*
  Copy constructor for Shallow copy
  100
  Destructor frees the heap memory
  crashes
  */
  ```

- control flow for this program:
  - begins with `main`.
  - Shallow object named `obj1` is created, it has a raw pointer attribute `ptr_data` and points to a memory location that stores the value 100.
  - when `display_shallow` function is called and the Shallow object is passed as a parameter, the copy constructor is called because the object is passed by value (hence a seperate Shallow object is created with scope of that function)
  - the control is now at the copy constructor, the new Shallow object's (the shallow copy) `ptr_data` stores the obj1.ptr_data i.e. it stores the same address as that of obj1.ptr_data and now points to the same memory address.
  - the control is back at the `display_shallow` function, it prints out 100 in the console.
  - when the `display_shallow` block ends, the control is at the destructor to delete the new Shallow Object (the shallow copy), as it deletes it frees up the allocated heap memory and now that memory is invalid.
  - the control is back at `main`
  - when main ends, the destructor is called again to delete the `obj1` object but the compiler sees that it is trying to dealocate invalid memory and hopefully the program crashes.

<br>

- The above copy constructor can also be written without parameter initialistion like

  ```cpp
  Shallow::Shallow(const Shallow& source)
  {
      ptr_data = source.ptr_data;
      cout << "Copy constructor for Shallow copy" << endl;
  }
  ```

> <br> Add a picture illustration <br>  
> <br>

<br>
<br>

# Deep copy with copy constructor

- In the copy constructor below, we copy the actual data (the data pointed by the ptr_data pointer) and not the address unlike shallow copy, so the new Deep object (the deep copy) actually points to a new heap memory and is seperate from the original argument.

  ```cpp
  #include <iostream>
  using namespace std;

  class Deep
  {
  private:
      int* ptr_data; //pointer to int

  public:
      Deep(int value);			//constructor prototype
      Deep(const Deep& source);	//copy constructor (deep copy)
      ~Deep();					//destrcutor
      void display_deep(Deep d);
  };

  Deep::Deep(int value)
  {
      ptr_data = new int;  //new heap memory
      *ptr_data = value;
  }

  //copy constructor using delegated constructor!
  Deep::Deep(const Deep& source): Deep{ *source.ptr_data }
  {
      cout << "copy constructor, deep copy" << endl;
  }

  Deep::~Deep()
  {
      delete ptr_data;  //deallocate memory
      cout << "destructor called" << endl;
  }

  void Deep::display_deep(Deep d)
  {
      cout << *d.ptr_data << endl;
  }

  int main()
  {
      Deep obj1{ 100 };
      obj1.display_deep(obj1);

  }

  /*
  copy constructor, deep copy
  100
  destructor called
  destructor called
  */
  ```

- control flow for this program:
  - begins with `main`.
  - Deep object named `obj1` is created, it has a raw pointer attribute `ptr_data` and points to a memory location that stores the value 100.
  - when `display_deep` function is called and the Deep object is passed as a parameter, the copy constructor is called because the object is passed by value (hence a seperate Deep object is to be created with scope of that function)
  - the control is now at the copy constructor, here a new Deep object is created and it's `ptr_data` attribute now pointst to a new and seperate memory on the heap with the value of 100.
  - the control is back at the `display_deep` function, it prints out 100 in the console.
  - when the `display_deep` block ends, the control is at the destructor to delete the new Deep Object (the deep copy)
  - the control is back at `main`
  - when main ends, the destructor is called again to delete the `obj1` object.

<br>

- We can write the above copy constructor without using the delegated constuctor as follows:

  ```cpp
  Deep::Deep(const Deep& source)
  {
      ptr_data = new int;
      *ptr_data = *source.ptr_data
      cout << "copy constructor, deep copy" << endl;
  }
  ```

- To confirm if the copy constructor is actually performing deep copy, we must debug the program and see that the pointers have different memory addresses for the source and the deep copy object.

<br>

# Move constructors

> checkout the notes for l values, r values, l value references and r value references. <br>

<br>

- If we donot define a move constructor, the compiler will use the copy constructor instead! this results in lot of memory when dealing with large amounts if data.
- Move constructors moves an object instead of copying it. It copies the address of the resource from source to the current object and nulls out the pointer in the source pointer.
- This can be a significant performance improvement.
- Move constructors are called when an object is created from a temporary object (**r values**).

* The definition for move constructor is similar to that of copy construtor. `const` is removed becuase we have to null the source pointer and r value references are used in parameters instead of l value references.

  ```cpp
  type(const type &source);   //copy constructor definition
  type(type &&source);        //move constructor definiton
  ```

* The following code doesn't have a move constructor defined, hence the compiler will use the copy constructor instead when class objects are created to pass into functions. This is not memory efficient.

  ```cpp
  #include <iostream>
  #include <vector>
  using namespace std;

  class Player {

  public:
      std::string name;   //string
      int* xp;            //raw pointer
      Player(string name_value = "None", int xp_val =0); //constructor prototype (notice we have used default values)
      Player(const Player& source);           // copy constructor prototype

  };

  //constructor definition
  Player::Player(string name_value, int xp_val) : name{ name_value }
  {
      xp = new int;
      *xp = xp_val;
      //initialises the name  and xp attribute
  }

  //copy constructor definition (must perform deep copy as raw pointer is present in class)
  Player::Player(const Player& source) : Player{ source.name, *source.xp }
  {
      cout << "copy constructor is called for : " << source.name << endl;
  }


  int main()
  {
      vector <Player> vec;
      vec.push_back(Player{ "hero" });  //These Player objects are temporary objects i.e. r values
      vec.push_back(Player{ "bad_guy" });
  }

  /*
  copy constructor is called for : hero
  copy constructor is called for : bad_guy
  copy constructor is called for : hero

  here the hero copy constructor is called more than once because of vector behaviour
  */

  ```

<br>

- Since the objects being passed into functions are r value (temporary), we can make it efficient by defining a move constructor which will override the copy constructor.
- We must use `noexcept` in function prototype and definiton in visual studio, for unkown reason.

  ```cpp
  #include <iostream>
  #include <vector>
  using namespace std;

  class Player {

  public:
      std::string name;   //string
      int* xp;            //raw pointer
      Player(string name_value = "None", int xp_val =0); //constructor prototype (notice we have used default values)
      Player(const Player& source);           // copy constructor prototype
      Player(Player&& source)noexcept;                // move constructor prototype

  };

  //constructor definition
  Player::Player(string name_value, int xp_val) : name{ name_value }
  {
      xp = new int;
      *xp = xp_val;
      //initialises the name  and xp attribute
  }

  //copy constructor definition (must perform deep copy as raw pointer is present in class)
  Player::Player(const Player& source) : Player{ source.name, *source.xp }
  {
      cout << "copy constructor is called for : " << source.name << endl;
  }


  //move constructor definition (must null the source raw pointer as raw pointers is present in the class)
  Player::Player(Player&& source)noexcept : Player{ source.name, *source.xp }
  {
      source.xp = nullptr;
      cout << "move constructor is called for : " << source.name << endl;
  }


  int main()
  {
      vector <Player> vec;
      vec.push_back(Player{ "hero" });  //These Player objects are temporary objects i.e. r values
      vec.push_back(Player{ "bad_guy" });
  }

  /*
  move constructor is called for : hero
  move constructor is called for : bad_guy
  move constructor is called for : hero
  */
  ```

<br>
<br>

# `this` pointer

- `this` is a reserved keyword.
- It is a pointer to the object and hence contains the address of the object.
- It can be only used in the scope of the class.
- We can use it to access members and methods and much more.

```cpp
void Account::set_balance(double bal)
{
    balance = bal; //   this->balance = bal; behind the scenes!
}
```

<br>

### Use cases

- `this` can be used in the case where the name of the member attribute and the parameter name are the same.

  ```cpp
  void Account::set_balance(double balance)
  {
      balance = balance; //ambiguous and may result in wrong output
  }
  ```

  ```cpp
  void Account::set_balance(double balance)
  {
      this->balance = balance; //non-ambiguous
  }
  ```

- `this` is used to determine if two objects are the same

  ```cpp
  bool Player::compare_objects(const Player& other)
  {
      bool res;
      if (this == &other)
      {
          res = true;
      }
      else
      {
          res = false;
      }
      return res;
  }
  ```

<br>
<br>

# `const` with classes

- When we `const` qualify an object, we cannot modify it's member attributes and we cannot use any functions that is not `const` qualified.

  ```cpp
  #include <iostream>
  #include <vector>
  using namespace std;

  class Player {
  private:
      int health;
      int xp;
      int* level_ptr;

  public:
      std::string name;
      string get_name();
      void set_name(string name_value);
      Player(string name_value);
  };

  Player::Player(string name_value): name{name_value}
  {
      //constuctor
  }


  string Player::get_name()
  {
      return this->name;
  }

  void Player::set_name(string name_value)
  {
      this->name = name_value;
  }


  int main()
  {
      const Player hero{ "hero" };    //const object
      Player bad_guy{ "bane" };       //non const object
      cout << bad_guy.get_name() << endl;
      hero.set_name("batman");            //error
      cout << hero.get_name() << endl;    //error
  }
  ```

- Hence, we must const qualify the member methods as shown below

  ```cpp
  #include <iostream>
  #include <vector>
  using namespace std;

  class Player {
  private:
      int health;
      int xp;
      int* level_ptr;

  public:
      std::string name;
      string get_name() const;
      void set_name(string name_value);
      Player(string name_value);
  };

  Player::Player(string name_value): name{name_value}
  {
      //constuctor
  }


  string Player::get_name() const
  {
      return this->name;
  }

  void  Player::set_name(string name_value)
  {
      this->name = name_value;
  }


  int main()
  {
      const Player hero{ "hero" };    //const object
      Player bad_guy{ "bane" };       //non const object
      cout << bad_guy.get_name() << endl;
      cout << hero.get_name() << endl;    //not an error anymore
      hero.set_name("batman");            //error, can't use setter methods with const objects
  }
  ```

<br>
<br>

# Static class members

- In C++, a static member is a member of a class that is not associated with any particular object of the class. Static members are shared by all objects of the class.
- Static members can be variables, functions, or classes.
- Static variables are initialized once (usually in source file), when the class is first defined.
- Static functions can be called without creating an object of the class.
- Static classes are used to create objects that are not associated with any particular class.

  ```h
  //header file

  #pragma once

  #include <string>
  using namespace std;

  class Player {
  private:
      static int num_players;

  public:
      std::string name;
      Player(string name_value);
      ~Player();

      static int get_num_players();
  };
  ```

  ```cpp
  //source file

  #include <iostream>
  #include "practice.h"
  using namespace std;

  int Player::num_players{ 0 };       //static members can be initialised in source file only!

  Player::Player(string name_value) : name{ name_value }
  {
      ++num_players;
  }

  Player::~Player()
  {
      --num_players;
  }

  int Player::get_num_players()
  {
      cout << name << end;    //error; "static functions have access to static members only"
      return num_players;
  }

  int main()
  {
      Player first{ "superman" };
      Player second{ "batman" };
      cout << first.get_num_players() << endl;    //2
  }
  ```

<br>
<br>

# structs

- In C++, structs are a way to group together related data. They are similar to classes, but they have some key differences.
  - Structs are implicitly public. This means that the members of a struct are accessible to all code. Classes are not implicitly public, and their members must be explicitly declared as public or private.
  - Structs are value types, while classes are reference types. This means that when you create a struct variable, a copy of the struct data is created. When you create a class variable, a reference to the class data is created.
  - Structs cannot have virtual functions. Virtual functions are functions that can be overridden by derived classes. Structs cannot have virtual functions because they are value types, and value types cannot be overridden.

<br>
<br>

# friends

> <br> Fill Notes <br> > <br>

<br>
<br>
