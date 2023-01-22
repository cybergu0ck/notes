def decoratorFunction(originalFunction):        #1. Takes a function as argument

    def wrapperFunction():
        print('The wrapper executed before {}'.format(originalFunction.__name__))  #2. Modification done to display function without changing it!
        originalFunction()

    return wrapperFunction   #3. returns the wrapper function ready to be executed!

@decoratorFunction
def display():
    print('The display function ran')

@decoratorFunction
def anotherDisplay():
    print('The Another display function ran')


display() 
anotherDisplay()
