Classes are blueprints or templates for creating objects in object-oriented programming.

<br>

The following is an example for Kotlin `Car` class.

```kt
class Car(
    val brand: String,
    val model: String,
    var fuel: Double,
){
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
}

```

<br>
<br>
<br>
<br>

# Properties

Properties are variables that belong to a class and store data/state for objects.

- `brand`, `model` and `fuel` are properties.

<br>
<br>
<br>
<br>

# Methods

Methods are functions that belong to a class and define behaviors/actions objects can perform.

- `showFuel` and `addFuel` are methods.

<br>
<br>
<br>
<br>

# Constructor

Constructor defines the parameters needed to create an object. It's the signature for object creation.

```kt
class Car(
    val brand: String,    // Constructor parameters
    val model: String,
    var fuel: Double
) {
    // Constructor just receives and assigns values
}

val car = Car("Toyota", "Camry", 50.0)  // Calling constructor
```

<br>
<br>
<br>
<br>

# Init

init is a special block that runs automatically when an object is created. It executes initialization logic right after the constructor.

```kt
class Car(
    val brand: String,
    var fuel: Double
) {
    init {
        // Runs AFTER constructor assigns brand and fuel
        println("$brand created with $fuel liters")

        // Can add validation
        if (fuel < 0) {
            fuel = 0.0
        }
    }
}
```

- `init` is not a method, it is a an initializer block in Kotlin.

* The execution order is as follows :

  1. Primary constructor parameters are assigned
  1. Property initializations
  1. init blocks run (in order if multiple)
  1. Object is ready to use

<br>
<br>
<br>
<br>

# Instantiation

```kt
fun main() {
    var myCar : Car = Car("Tata", "Siera", 0.0)
    myCar.addFuel(100.0)
    println(myCar.showFuel())
}

//Tata Siera is being manufactured.
//100.0
```

<br>
<br>
<br>
<br>
