# Array Sorting Algorithms

| Algorithm      | Big Omega           | Big Theta           | Big O          | Big O, Space Complexity |
| -------------- | ------------------- | ------------------- | -------------- | ----------------------- |
| Insertion Sort | $\Omega(n)$         | $\theta(n^2)$       | $O(n^2)$       | $O(1)$                  |
| Merge Sort     | $\Omega(n \log(n))$ | $\theta(n \log(n))$ | $O(n \log(n))$ | $O(n)$                  |

<br>
<br>

## Insertion Sort

```py
def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp
    return nums
```

<br>
<br>

## Merge Sort

```py
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # Append remaining elements from left, if any
        if i < len(left):
            nums[k:] = left[i:]

        # Append remaining elements from right, if any
        if j < len(right):
            nums[k:] = right[j:]


def apply_merge_sort(nums):
    merge_sort(nums)
    return nums


nums = [38, 27, 43, 3, 9, 82, 10]
print(apply_merge_sort(nums))
# [3, 9, 10, 27, 38, 43, 82]
```
