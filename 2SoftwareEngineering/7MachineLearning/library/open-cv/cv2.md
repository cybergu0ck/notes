
## Reading an image using `imread()`
---
```python
image = cv2.imread('E:\\2Media\\1Pictures\\6Screenshots\\test.png',cv2.IMREAD_COLOR)
```

flag: 
1. `cv2.IMREAD_COLOR` (or -1) : loads color image, excludes transparency channel if present.
2. `cv2.IMREAD_GRAYSCALE` (or 0) : loads image in grayscale mode
3. `cv2.IMREAD_UNCHANGED` (1): loads original image with transparency (alpha value)


## Showing the image using `imshow()`
---
```python
cv2.imshow('this is the test image',image)
cv2.waitKey(0)
```


## Resize the image using `cv2.resize()`
---
```python
image = cv2.resize(image, (400,360))
```
This will resize the image to 400 * 360 size.


```python
image = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)
```
This will resize according to the original size, the above will decrease the size by 50% vertically and horizontally.


## Rotating the image using `cv2.rotate()`
---
```python
image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
```
This will rotate the image clockwise by 90 degrees.


## Writing the image using `imwrite() `
---
```python
cv2.imwrite(path + '\\small-car.png', image)
```
This will write the image to the specified path