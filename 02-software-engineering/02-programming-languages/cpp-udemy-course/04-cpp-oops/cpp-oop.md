> <br> C++ is a general-purpose programming language that supports procedural, object-oriented, and generic programming. 


<br>
<br>

# Procedural Programming

* procedural programming is basically a collection of functions, where data (usually declared seperately) are manipulated.
* limitations: 
    * functions need to know the structure of data, if structure of the data is changed, then the function must also change for it to work.
    * as programs get large, it is difficult to understand, maintain, reuse, debug, extend.

<br>
<br>

# Object Oriented Programming 

* Object-oriented programming (OOP) is a programming paradigm that uses "objects" – data structures consisting of data fields and methods together with their interactions – to design applications and computer programs.
* OOP in C++ is based on the concept of classes. A class is a blueprint for an object. It defines the data that an object will hold and the methods that an object will have.
* When you create an object, you are creating an instance of a class. The object will have its own copy of the data that is defined in the class, and it will be able to call the methods that are defined in the class.

* Advantages
    * Abstraction : Abstraction is a process of hiding the implementation details of a system from the user, and only the functional details will be available to the user end. 
    * Encapsulation: Encapsulation is a method of wrapping up the data and code acting on the data into a single unit.
    * Inheritence : Creating new classes by using the code present in already defined classes, extending the data.
    * Polymorpism : Polymorphism is the ability to use the same code to operate on different types of objects. This makes the code more flexible.
<br>

* Limitations:
    * OOP is not a panacea, it will bad code even worse XD
    * complicated design
    * slower and larger in size

<br>
<br>

# Classes and Objects

* Classes are user defined datatypes that act as a blueprints from which objects are created.
* Classes have attributes (data) and methods(functions).

<br>

* Objects are specific instance of a class, which has it's own identity.
* Objects have the attributes and can make use of the methods defined in the class.

<br>
<br>

# Class Declaration

* The syntax for declaring classes (Note the semi colon at the end).
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

* An object can use the dot operator (.) to access the members of it's class.

    ```cpp
    int main()
    { 
        Player jack;
        jack.name = "jack";
        jack.talk("Hello");

    }
    //jack saya Hello
    ```

* When using pointer to a class object, we can access the class members in two ways:

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

    2. Use the *member of pointer operator* (arrow operator)

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

* C++ provides three kinds:

    1. public : accessible anywhere
    2. private : accessible only by members or friends of the class.
    3. protected : accessible by members of the class and members of derived class. 

<br>

* The syntax is:

    ```cpp
    class Class_Name{
        acess_modifier:  //public, private or protected
            //declarations
    };
    ```

* If no access modifier is specified, then the members are considered as private.
* The memeber methods in the class declaration always has access to to the member attributes! 

<br>
<br>

# Implementing member method

* member methods can be implemented in two ways:
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

* We can seperate the class specification (declaration) from the implementation using header files
    * .h file for class declaration
    * .cpp file for the class implementation

<br>

* Consider the following header file that contains the declaration

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

* the following source file contains the implementation

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

* without include guards, the compiler will see the declaration everytime the header file is included in a file. (this is an error)
* there are two kinds:

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

* constructor is a special member function that is invoked during object creation and hence we can use it for initialization.
* constructors must have the same name as the class.
* no return type is specified for constructors. 
* constructors can be overloaded.

    ```cpp
    #include <iostream>

    using namespace std;

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

        int get_health();
        void set_health(int);
    };

    void Player::set_health(int value) {
        health = value;
    }

    int Player::get_health() {
        return health;
    }

    int main()
    { 
        Player superman{ "Kent Clark" };
        superman.set_health(1000);
        cout << superman.get_health();
    }

    //constructor with name parameter is called for Kent Clark
    //1000
    ```

<br>
<br>

# Destructors

* Destructors are also special kind of member function that is invoked automatically when the object is destroyed.
* Destructors have the same name as the class preceded by a tilde symbol (~)
* Destructors have no return type and no parameters.
* There can be only 1 destructor for a class hence it cannot be overloaded unlike constructors.
* They are used to release memory and stuff