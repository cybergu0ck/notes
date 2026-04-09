# Contents

- [Recursion](#recursion)
  - [Recurrance Relations](#recurrance-relations)
  - [Tail recursion](#tail-recursion)

<br>
<br>
<br>




# Recursion

- Theoretically, there is no problem that can only be solved with recursion. According to the "Church-Turing" Thesis, recursion and iteration are computationally equivalent; any recursive algorithm can be converted into an iterative one by manually managing a stack.
  - However, some problems are "inherently recursive," meaning an iterative version would be significantly more complex, less readable, or would simply "manualize" the recursion by using an explicit stack

<br>
<br>
<br>

## Recurrance Relations

$T(n) = T(n-1) + n = O(n^2)$

$$ T(n) = T(n-1) + n $$
$$ T(n) = T(n-2) + (n-1) + n $$
$$ T(n) = T(n-3) + (n-2) + (n-1) + n $$
$$ \text{Hence, } T(n) = T(n-k) + (n-k+1) + (n-k+2) +...+ (n-1) + n $$

$$ \text{T(1) = 1, Therefore n-k = 1, Substituting this in the above equation,}$$

$$ T(n) = 1 + 2 + 3 + ... + n-1 + n $$
$$ T(n) = \frac{n(1+n)}{2} $$
$$ O(n^2)$$

<br>
<br>
<br>

## Tail recursion

Tail recursion is a specialized form of recursion where the recursive call is the final operation performed by a function.

- Regular recursion

  ```py
  function factorial(n) {
  if (n === 0) return 1;
  return n * factorial(n - 1);
  }
  ```

- Tail recursion

  ```py
  function factorial(n, acc = 1) {
  if (n === 0) return acc;
  return factorial(n - 1, acc * n);
  }
  ```

- Checkout this [video](https://www.youtube.com/watch?v=mfkOjhZmkRk) to understand the concept with an illustration.
