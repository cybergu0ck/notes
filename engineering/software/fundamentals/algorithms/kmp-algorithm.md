# The Problem

- We are trying to find if the given string (we call haystack) is made up of repeating substring (we call needle).
- 'xabxab' is a haystack with needle 'xab'.
- 'xabyab' has 'ab' repeating but this is not our problem as we are dealing with patterns which when repeated forms the entire string.

<br>
<br>
<br>

# Brute Force Method

The brute force method to search a pattern in a string.

```py
def strStr(haystack: str, needle: str) -> bool:
    if needle == "" : return 0
    for i,c in enumerate(haystack):
        is_needle = haystack[i: i+ len(needle)]
        if is_needle == needle:
            return True
    return False
```

- Here the for loop runs 'n' times and accessing a range of values from the string is O(m). Hence O(m\*n).

<br>
<br>
<br>

# KMP Algorithm

The Knuth-Morris-Pratt (KMP) algorithm is a string-searching algorithm that efficiently finds occurrences of a pattern (we call needle) string within a longer text string (we call haystack).

<br>

## 1. Preprocessing (Computing LPS)

Construct the lps (Longest Prefix Suffix) array/ prefix table/ partial match table.

- LPS stands for largest Preffix Suffix.
- It is an array
- I personally use the term lps value to refer to each value in the lps array that is calculated untill every index based on the length of pattern repeatition.
  - lps value of 0 means there the pattern is not repeating. ex: ab
  - lps value of 1 means we have pattern of len 1 that is repeating. ex: aa [(a)(a)]
  - lps value of 2 means we have a pattern of len 2 that is repeating. ex: abab [(ab)(ab)] or aaaa [(aa)(aa)]
  - So on and so forth.

### Illustration

- For abcab, the lps = [0, 0, 0, 1, 2]
- For aaabc, the lps = [0, 1, 2]
- For abaaba, the lps = [0, 0, 1, 1, 2, 3]

<br>

## 2. Searching

Compare the characters and use the lps array.

```py
def get_lps( needle):
    lps = [0]* len(needle)
    p = lps[0]  #The value of p is always 0 for every case
    i = 1       #We always start with the first index
    while(i < len(needle)):
        if needle[i] == needle[p]:
            #We found a better lps value; increment
            lps[i] = p + 1
            p += 1
            i += 1
        else:
            if p == 0:
                #We found the least lps value; increment
                lps[i] = 0
                i += 1
            else:
                #Try to keep the current lps value we have got
                p = lps[p-1] #crucial
    return lps

def kmp_algo(haystack, needle):
    lps = get_lps(needle)  #preprocessing

    #searching
    i = 0  # ptr for haystack
    j = 0  # ptr for needle
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]  #crucial
        if j == len(needle):
            #return i - len(needle) #return index
            return True
    return False
```

<br>
<br>
<br>

# Time complexity

- If 'n' is the length of the haystack.
- If 'm' is the length of the needle.

<br>

1. Big O of Brute Force is O(n\*m).
1. Big O of KMP is O(n+m).

<br>
<br>
<br>

# Usefullness of KMP

In the brute force method the move back in haystack if a character in it doesn't match the needle's character. But in KMP algorithm we never do this computation. See Neetcode's video from the reference section.

<br>
<br>
<br>

# Reference

- Watch this [video](https://youtu.be/V5-7GzOfADQ) to understand how to compute lps array.
- Watch [neetcode's video](https://youtu.be/Gjkhm1gYIMw) to understand the algorithm.
