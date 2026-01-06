Polymorphism is the ability to use the same code to operate on different types of objects. This makes the code more flexible.

<br>
<br>
<br>
<br>

# Function overloading

Function overloading means having multiple functions with the same name but different function signatures.

- The following constitute a function signature.
  - Function name
  - Number of parameters
  - Type of parameters
  - Order of paramters
- Return type is not a part of function signature. Therefore two functions with same name but different return type is not allowed.

<br>
<br>
<br>
<br>

# Constructors

The following class has multiple constructors with different paramters and they use the primary constructor.

```kt
class Car(
    val brand: String,
    val model: String,
    var fuel: Double,
) : Vehicle("Car"){

    constructor(brand: String) : this(brand, "generic", 0.0) //constructor delegation
    constructor(brand: String, model: String) : this(brand, model, 0.0) //constructor delegation

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
```
