# Open CV

<br>
<br>

## Basic Open CV Operations

<br>

### Reading an image

```
cv2.imread(filename[, flags])
```

flags (Optional):

1. `cv2.IMREAD_COLOR` (or -1) : loads color image, excludes transparency channel if present.
2. `cv2.IMREAD_GRAYSCALE` (or 0) : loads image in grayscale mode
3. `cv2.IMREAD_UNCHANGED` (1): loads original image with transparency (alpha value)

<br>

### Displaying the image

```python
cv2.imshow(window_name,array)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

- window_name is the title of the window that displays the image.
- array is the image read as numpy array.

<br>

### Writing the image

This will write the image to the specified path.

```python
cv2.imwrite(path, array)
```

<br>
<br>

## Basic Image Operations

<br>

### Resizing the image

```python
image = cv2.resize(image, (400,360))
```

This will resize the image to 400 \* 360 size.

```python
image = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)
```

This will resize according to the original size, the above will decrease the size by 50% vertically and horizontally.

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
