# The Basics

- NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers.
- In NumPy **_dimensions are called axes_**.

* The following array has one axis with 3 elements in it.
  ```
  [1,2,3]
  ```
* This one has two axes, the first axis has length of 2 and the second one has length of 3.

  ```
  [[1., 0., 0.],
  [0., 1., 2.]]
  ```

* NumPy’s array class is called `ndarray`. It is also known by the alias `array`.

<br>
<br>

## ndarray.ndim

- The number of axes (dimensions) of the array.

<br>
<br>

## ndarray.shape

- The dimensions of the array.
- This is a tuple of integers indicating the size of the array in each dimension.
- For a matrix with n rows and m columns, shape will be (n,m).
- The length of the shape tuple is therefore the number of axes, ndim.

<br>
<br>

## ndarray.size

- The total number of elements of the array. This is equal to the product of the elements of shape.

<br>
<br>

<br>
<br>
<br>

# Creating Arrays

## From a Python List

```py
import numpy as np
python_list = [1,2,3]
numpy_array = np.array(python_list)
```
