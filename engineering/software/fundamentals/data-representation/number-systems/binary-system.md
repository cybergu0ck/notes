# Bit

The term "bit" is short for "binary digit" and represents a single binary value, either 0 or 1.

<br>
<br>
<br>
<br>

# Binary Numbers

The binary system is a base-2 positional number system, using only [bits](./binary-system.md#bit).

- Each position in a binary number represents a power of 2.
- A 8 bit binary number is called a "byte".
- MSB (Most Significant Bit) is the bit in a binary number that has the highest weight, usuall the leftmost bit.
- LSB (Least Significant Bit) is the bit in a binary number that has the lowest weight, usually the rightmost bit.

<br>
<br>
<br>

## Types of binary numbers

Binary numbers can be unsigned or signed.

<br>
<br>

### Unsigned binary numbers

Unsigned binary numbers represent only non-negative values (zero and positive integers).

- These numbers do not have a sign bit; all bits contribute to the magnitude.
- For an 'n' bit unsigned binary number, the range is from 0 to $2^n - 1$.

<br/>
<br/>

### Signed binary numbers

Signed binary numbers can represent both positive and negative values by using a sign bit.

There are several methods to represent signed numbers:

<br>

#### Sign-Magnitude

[MSB](./binary-system.md#binary-numbers) is sign, rest bits represent magnitude; however, zero has two representations (+0 and -0).

<br>

#### One’s Complement

Negative numbers are bitwise inverted; still has two zeros.

<br>

#### Two’s Complement

Negative numbers are represented by inverting bits and adding one; only one zero representation.

- This is most commonly used to represent signed binary numbers.

<br>
<br>
<br>

## The total number of unique values represented by n bit binary number.

The total number of unique values represented by 'n' bit binary number is $2^n$.

- a 2 bit binary number can represent $2 ^2 = 4$ values.
- a 3 bit binary number can represent $2 ^3 = 8$ values.
- a 8 bit binary number (A byte) can represent $2 ^8 = 256$ values.

<br>
<br>

## The range of numbers represented by n bit binary number.

The range of numbers that can be represented by an 'n' bit binary number depends on whether the representation is [signed or unsigned](./binary-system.md#types-of-binary-numbers).

- The range of numbers that can be represented by a 'n' bit unsigned binary number is 0 to $2^n - 1$.

  - A [byte](./binary-system.md#binary-numbers) can represent 0 to 255 in case of unsigned binary numbers.

- The range of numbers that can be represented by a 'n' bit singed binary number using two's complement system is $ -2^{n-1} \space \text{to} \space 2^{n-1}-1$.

  - A [byte](./binary-system.md#binary-numbers) can represent -128 to 127 in case of signed binary numbers.

<br>
<br>

## The number of bits required to represent an integer

The number of bits required to represent an integer 'i' is roughly of order $\log_{2}(i)$

- Considering unsigned binary numbers, The range of numbers that can be represented by an n-bit unsigned binary number is [0 to $2^n - 1$](./binary-system.md#the-range-of-numbers-represented-by-n-bit-binary-number).
- To represent integer 'i' in binary, enough bits are needed such that largest number represented using the bits is at least as big as 'i'.

$$
2^n - 1 \geq i
$$

$$
2^n \geq i
$$

$$
nlog_2(2) \geq log_2(i)
$$

$$
n  \geq log_2(i)
$$

<br>
<br>
<br>

## Each additional bit doubles the range of distinct values that can be represented

- Considering unsigned binary numbers, The total number of unique values represented by 'n' bit binary number is [$2^n$](./binary-system.md#the-total-number-of-unique-values-represented-by-n-bit-binary-number).

- Increasing by 1 bit, the total unique values that can be represented will be

$$ 2^{n+1} $$
$$ 2^1 \times 2^n $$

<br>
<br>
<br>

## Binary Arithmetic

#TODO - Add notes when required, include Overflow and Underflow topic.

<br>
<br>
<br>

## Bitwise Operations

#TODO - Add notes when required.

<br>
<br>
<br>

## Endianness

#TODO - The concept of byte order: Big-endian vs. Little-endian.

<br>
<br>
<br>

## Floating Point Representation

#TODO - Seems like an advanced topic, also not sure if it comes under binary numbers.

<br>
<br>
<br>

## Binary Coding Systems

#TODO - Seems like an advanced topic, encoding schemes like Gray code, BCD (Binary Coded Decimal).

<br>
<br>
<br>
