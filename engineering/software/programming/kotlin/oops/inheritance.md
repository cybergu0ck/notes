Inheritance is when a class (child/subclass) acquires properties and methods from another class (parent/superclass).

<br>

# Super class

Superclass is the class that is being inherited from. It contains common properties and methods shared by its subclasses.

```kt
open class Vehicle(
    val type: String,
) {
    init {
        println("A $type type of vehicle is being manufactured.")
    }

    open fun printType(){
        println("Vehicle type : $type")
    }
}

class Car(
    val brand: String,
    val model: String,
    var fuel: Double,
) : Vehicle("Car"){
    init {
        //automatically executed when an object of this class is instantiated
        println("$brand $model is being manufactured.")
    }

    fun showFuel(): Double {
        return fuel
    }

    fun addFuel(fuel : Double){
        this.fuel += fuel
    }

    override fun printType() {
        println("Vehicle type : $type, brand: $brand, model: $model, fuel: $fuel")
    }
}

fun main() {
    var myCar : Car = Car("Tata", "Siera", 0.0)
    myCar.addFuel(100.0)
    myCar.printDetails()
}

//A Car type of vehicle is being manufactured.
//Tata Siera is being manufactured.
//Vehicle type : Car, brand: Tata, model: Siera, fuel: 100.0
```

- Kotlin classes are `final` by default. To enable a class to be super class it must be made `open`.
- Subclasses must initialise superclass constructor.

* Superclass methods are `final` by default, they must be made `open` to be overriden by subclasses.
* `override` keyword must be used for subclass methods to override their superclass methods.

<br>
<br>
<br>
<br>

# Visibility Modifiers

The accessibility of properties and methods can be controlled using the visibility modifiers.

| Modifier  | Accessibility                   |
| --------- | ------------------------------- |
| public    | Everywhere (default)            |
| private   | Within the class                |
| protected | Within the class and subclasses |
| internal  | Within the module               |

- The following method for the `Car` means that this method can be called only within the class and not outside of it.

  ```kt
  private fun openEngineCase()
  {
      println("Simulate opening the engine case")
  }
  ```

<br>
<br>
<br>
<br>

# Abstract class

Abstract class is a class that cannot be instantiated directly and serves as a blueprint for other classes.

```kt
abstract class Vehicle(
    val type: String,
) {
    init {
        println("A $type type of vehicle is being manufactured.")
    }

    abstract fun getDetails() : String //Abstract method has no implementation and must be overridden
}

class Car(
    val brand: String,
    val model: String,
    var fuel: Double,
) : Vehicle("Car"){
    init {
        //automatically executed when an object of this class is instantiated
        println("$brand $model is being manufactured.")
    }

    fun showFuel(): Double {
        return fuel
    }

    fun addFuel(fuel : Double){
        this.fuel += fuel
    }

    private fun openEngineCase()
    {
        println("Simulate opening the engine case")
    }

    override fun getDetails() : String{
        return "Type : $type, Brand: $brand, Model: $model, fuel: $fuel"
    }
}

fun main() {
    var myCar : Car = Car("Tata", "Siera", 0.0)
    myCar.addFuel(100.0)
    println(myCar.showFuel())
    println(myCar.getDetails())
}

//A Car type of vehicle is being manufactured.
//Tata Siera is being manufactured.
//100.0
//Type : Car, Brand: Tata, Model: Siera, fuel: 100.0
```

- Abstract classes in Kotlin can have

  1. Abstract members : Incomplete members that needs to be overridden by subclasses.
  1. Concrete members : Complete members that have initial value or implementation.
