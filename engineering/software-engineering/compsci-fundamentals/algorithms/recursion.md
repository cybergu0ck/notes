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
