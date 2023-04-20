
## Random Remarks
---

- If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance:

    ```python
    class WareHouse:
        region = 'West'

    first_property = WareHouse()
    print(f'first_property is a {first_property.__class__.__name__} in {first_property.region}')

    second_propery = WareHouse()
    second_propery.region = 'North'
    print(f'second_propery is a {second_propery.__class__.__name__} in {second_propery.region}')

    ```

- Often, the first argument of a method is called self. ***This is nothing more than a convention: the name self has absolutely no special meaning to Python***. Note, however, that by not following the convention your code may be less readable to other Python programmers, and it is also conceivable that a class browser program might be written that relies upon such a convention.

- Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok. For example:

    ```python
    def written_outside_the_class():
    print("Printing something")

    class NewsAgency:
        printer = written_outside_the_class

        printer()
        
    fox_news = NewsAgency()

    #>Printing something
    ```

    * Note that this practice usually only serves to confuse the reader of a program.

* Methods may call other methods by using method attributes of the self argument:

    ```python
    class Elevator:
    """Simulates an 2 floor elevator."""

    def go_to_first_floor(self):
        print("Reached first floor.")

    def go_to_second_floor(self):
        self.go_to_first_floor()
        print("Reached second floor.")

    mitsubishi = Elevator()
    mitsubishi.go_to_second_floor()

    #>Reached first floor.
    #>Reached second floor.
    ```

