# Casting Operators

# reinterpret_cast

- This casting operator is the most powerful, but also the most dangerous, as it performs low-level reinterpretation of the bits of an object from one type to another.
- It allows you to convert between unrelated types, such as between pointers and integers, but it should be used sparingly and with a deep understanding of the implications.
- It is also called as C style cast or forced cast.

<br>
<br>

# static_cast

- This casting operator is used for performing conversions that are known at compile-time and can be checked for safety.
- It is primarily used for implicit conversions between compatible types, such as converting from one arithmetic type to another or from a pointer to a base class to a pointer to a derived class.
- It supports both upcasting and down casting.
- It is also called safe cast or compile time cast.

<br>
<br>

# dynamic_cast

- It supports only down casting.
- Also called as safe cast or run time cast.

<br>
<br>

# const_cast

-
