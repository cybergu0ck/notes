# Recursion

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

Tail recursion is when a function's recursive call is the very last thing it does, No work happens after it returns.

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
