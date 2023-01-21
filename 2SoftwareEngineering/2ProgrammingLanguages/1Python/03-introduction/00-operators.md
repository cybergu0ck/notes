

### Bitwise Operators 
---

| Symbol | Operator |
|---|---|
| & | bitwise AND |
| \| | bitwise OR |
| ~ | bitwise NOT |
| ^ | bitwise XOR |
| << | bitwise Left Shift |
| >> | bitwise Right Shift |

### Bitwise AND
---
Decimal 5 is Binary 0101. (5 is 0b0101)
Decimal 6 is Binary 0110. (6 is 0b0110)

5 & 6 should give 0b0100 which is 4 (Perform AND bit by bit)

```python
print(5 & 6)

>4
```

We can use the `bin()` to get binary of any decimal number.
```python
print(bin(5 & 6))

>0b100
```


### Bitwise OR
---
Exactly same like AND but instead performs OR.


### Bitwise NOT
---
Invert all the 1's to 0's and 0's to 1's.

Important points:

> ***Computers store negative numbers in 2's compliment form ([Twos complement: Negative numbers in binary - Ben Eater](https://www.youtube.com/watch?v=4qH4unVtJkE&ab_channel=BenEater))***
> 
> Hence, 
> 1. to find the decimal equivalent of a negative binary number (i.e. if MSB = 1), get the 2's compliment
> 2. To find the binary bits for a negative decimal number, also get the 2's compliment.

* It is crucial to know how many bits does the language (compiler or interpreter) use to represent numbers, As this will determine the position of the Most Significant Bit (MSB)
* MSB will determine if the number is positive (MSB = 0) or negative (MSB = 1)
* Python uses 32 bits to represent integers.

![image](../_assets/bitwise-not.jpg)

Explanation for how it is (-6) in Base 10 is as follows:

![image1](../_assets/negative-numbers.jpg)


> Shortcut to find bitwise OR
> 
> `~ N is equal to -(N+1)`
> 
> ~5 is -6

