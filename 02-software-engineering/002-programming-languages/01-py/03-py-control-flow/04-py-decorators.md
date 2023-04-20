# Decorators

In Python, a decorator is a function that takes another function as input and extends or modifies its behavior without explicitly changing its source code.

- Illustration for the concept of decorators.

    ```python
    def move():
        print("Robot moved!")   #simulates robot movement

    def make_sophesticated(func):   #takes the function as a parameter
        def recalibrate():
            func()                  #calls that funciton
            print("Recalibrating postion sensors now...")       #Adds extra behaviour

        return recalibrate              #Returns the modified function

    make_sophesticated(move)()          #Note that it needs to be called as fucntion object was returned

    #>Robot moved!
    #>Recalibrating postion sensors now...
    ```

- With the help of decorators we can simply call the original funciton and expect the modified behaviour!

    ```python
    def make_sophesticated(func):
        def recalibrate():
            func()
            print("Recalibrating postion sensors now...")

        return recalibrate

    @make_sophesticated     #syntax
    def move():
        print("Robot moved!")

    move()

    #>Robot moved!
    #>Recalibrating postion sensors now...
    ```