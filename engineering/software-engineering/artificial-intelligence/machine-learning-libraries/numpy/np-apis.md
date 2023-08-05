# `np.linspace`

- Return evenly spaced numbers over a specified interval.

  ```
  numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
  ```

* This code creates an array of 5 evenly spaced numbers with values ranging from 0 to 10 including the last number.

  ```py
  x = np.linspace(0,10,5)
  print(x)

  #>array([ 0. ,  2.5,  5. ,  7.5, 10. ])
  ```
