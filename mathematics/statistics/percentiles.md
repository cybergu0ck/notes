<style TYPE="text/css">
code.has-jax {font: inherit; font-size: 100%; background: inherit; border: inherit;}
</style>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [['$','$'], ['\\(','\\)']],
        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'] // removed 'code' entry
    }
});
MathJax.Hub.Queue(function() {
    var all = MathJax.Hub.getAllJax(), i;
    for(i = 0; i < all.length; i += 1) {
        all[i].SourceElement().parentNode.className += ' has-jax';
    }
});
</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS_HTML-full"></script>

# Percentiles

**_A percentile is a measure that indicates the value below which a given percentage of observations in a group of observations falls._**

- For example, the 50th percentile (also known as the median) is the value below which 50% of the data falls. 17th percentile is the value below which 17% of the data falls.
- Therefore, if someone scored at the 90th percentile on a standardized test, it means they scored as well as or better than 90% of the test takers.

<br>
<br>

## Calculation

To calculate a percentile,

1. arrange the data in ascending order from smallest to largest.
2. determine the position of the desired percentile within the dataset based on its percentage.
3. The value correspondin to that position is the value for the percentile.

<br>
<br>

## Illustration

For example, consider the scores in a standardized test as 98, 60, 91, 29, 75, 86, 53, 10.

### Calculating the 25th percentile

1. Arranging the data in ascending order: 10, 29, 53, 60, 75, 86, 91, 98.
2. Determining the position of the 25th percentile.

   $$ position = \frac{25}{100} \times {8} = 2$$

3. The value corresponding to $2 ^{nd}$ position is the value of the 25th percentile. This means that 25% of the data points in the dataset are less than or equal to 29.
   $$25^{\text{th}} \text{ percentile} = 29$$

<br>

### What percentile does the score of 91 fall

1. Arranging the data in ascending order: 10, 29, 53, 60, 75, 86, 91, 98.
2. We know the position of the score 91 i.e $7 ^ {th}$. Using the formula

   $$ 7 = \frac{x}{100} \times {8}$$

   $$ x = 87.5$$

3. So, the value 91 falls at the 87.5th percentile in the given dataset. This means that approximately 87.5% of the values in the dataset are less than or equal to 91.

<br>
<br>

## Quartiles

Quartiles are common percentiles that divides the data into 4 parts.

| Percentile                     | Meaning                                          |
| ------------------------------ | ------------------------------------------------ |
| 25th percentile (Q1)           | One-fourth of the data falls below this value.   |
| 50th percentile (Q2 or median) | Half of the data falls below this value.         |
| 75th percentile (Q3)           | Three-fourth of the data falls below this value. |
