# Open CV

<br>
<br>

## Basic Open CV Operations

<br>

### Reading an image

- Syntax :

  ```
  cv2.imread(filename[, flags])
  ```

  flags (Optional):

  1. `cv2.IMREAD_COLOR` (or -1) : loads color image, excludes transparency channel if present.
  2. `cv2.IMREAD_GRAYSCALE` (or 0) : loads image in grayscale mode
  3. `cv2.IMREAD_UNCHANGED` (1): loads original image with transparency (alpha value)

<br>

### Displaying the image

- Syntax :

  ```python
  cv2.imshow(window_name,array)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  - window_name is the title of the window that displays the image.
  - array is the image read as numpy array.

<br>

### Writing the image

- Syntax :
  ```python
  cv2.imwrite(path, array)
  ```

<br>
<br>

## Basic Image Operations

<br>

### Resizing the image

- Syntax

  ```
  cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
  ```

  - src: Input image (numpy array).
  - dsize: Size of the output image (width, height). If it's a scaling factor, it should be (0, 0).
  - dst: (Optional) Output image. If not specified, a new image is created.
  - fx: (Optional) Scale factor along the horizontal axis. Default is 1.0.
  - fy: (Optional) Scale factor along the vertical axis. Default is 1.0.
  - interpolation: (Optional) Interpolation method used for resizing. Default is cv2.INTER_LINEAR.

- Resizing the image to a desired output size.

  ```python
  image = cv2.resize(image, (400,360))
  ```

- Resizing the image using scaling factor. Here, the size of the image is decreased by 50% in both dimensions.

  ```python
  image = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)
  ```

<br>

### Rotating the image

```python
image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
```

This will rotate the image clockwise by 90 degrees.

<br>

### Getting the shape of an image

```python
dimensions = image.shape  # Not image.shape()
```

This gives a tuple with 3 items,

1. first item is image height
2. second is image width
3. number of channels
