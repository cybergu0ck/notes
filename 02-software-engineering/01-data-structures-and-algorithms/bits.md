
# Range of values that can be represented using bytes

- Byte can hold 8 bits.
- The range of values a byte can hold is -128 to 127 in case of signed bits and 0-255 in case of unsigned bit notation.

***Concept Clarity:***
> every `bit` can be 0 or 1. hence the formula for number of values a N bit binary number = 2 ^ N.

- a 2 bit binary number can hold 2 ^2 = 4 values
- a 3 bit binary number can hold 2 ^3 = 8 values
- a 8 bit binary number (A `byte`) can hold 2 ^8 = 256 values.

<br/>

Consider a byte,

## Unsigned Bit Notation:

- If a byte can hold 256 values then values 1 to 255 will contain 255 values. zero should be included as 00000000 (binary) is 0 (decimal). Hence, the range of values will be 0-255 (has 256 values)

<br/>

## Signed Bit Notation:

> ***In a signed bit MSB is used to represent the sign. ***
- hence there are 7 bits remaining for values. Using the formula 2 ^7 = 128 values can be represented. note that totally 128 positive values (MSB is 0) and 128 negative values can be included (by making the MSB as 1). From 1-127 has 127 values, adding 0 (0:127) we have 128 values. Now -1:-127 we have 127 values we have to include -128 (i.e -11111111) 
- The overall range of values would be -128:127 (256 values)
