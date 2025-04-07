## Headings

- ```markdown
  # Heading 1

  ## Heading 2

  ### Heading 3

  #### Heading 4

  ##### Heading 5

  ###### Heading 6
  ```

<br/>
<br/>
<br>

## Italic text

- ```markdown
  _This is italic text_
  ```

- _This is italic text_

<br/>
<br/>
<br>

## Bold text

- ```
  **This is bold text**
  ```
- **This is bold text**

<br/>
<br/>
<br>

## Hardbreak

- ```
  This is a a paragraph showing how to use hardbreak and softbreak.

  This right here is a hardbreak as I have left an entire line of space.
  ```

- This is a a paragraph showing how to use hardbreak and softbreak.

  This right here is a hardbreak as I have left an entire line of space.

<br/>
<br/>
<br>

## Softbreak

- ```
  However, if we leave exactly 2 spaces after a sentence it'll be a softbreak. You can see here  |
  I left 2 space's before ther vertical line (Don't use the verticle line, it's just for illustration)
  ```
- However, if we leave exactly 2 spaces after a sentence it'll be a softbreak. You can see here  
  before ther vertical line (Don't use the verticle line, it's just for illustration)

<br/>
<br/>
<br>

## Indentation

- Use softbreak and then `&emsp;`
  ```markdown
  This right here  
  &emsp; is how you indent  
  &emsp; &emsp; Gotta use softbreak(i.e. atleast a space is left at the end of previous line.)!
  ```
- This right here  
  &emsp; is how you indent  
  &emsp; &emsp; Gotta use softbreak(i.e. atleast a space is left at the end of previous line.)!

<br/>
<br/>
<br>

## Adding links

- Standard url
  ```
  [description here](url)
  ```

<br/>
<br/>
<br>

## Embedding Images

```syntax
![description](path)
```

<br/>
<br/>
<br>

## Unordered lists

- ```markdown
  - First
  - Second
    - sub first
      - sub sub first
  ```

- - First
    _ Second
    _ sub first \* sub sub first

<br/>
<br/>
<br>

## Ordered lists

- ```
  1. first item
  1. second item
  1. third item
      1. sub item
          1. sub sub item
  ```
- 1. first item
  1. second item
  1. third item
     1. sub item
        1. sub sub item

<br/>
<br/>
<br>

## Checkboxes

- This will show as checkboxes in github

- [x] get this item
- [] do this chore

<br/>
<br/>
<br>

## Code blocks

Enclose multine code in '```'.

<br/>
<br/>
<br>

## Tables

- ```markdown
  | Column 1   | Column 2   |
  | ---------- | ---------- |
  | some thing | some value |
  ```

- | Column 1   | Column 2   |
  | ---------- | ---------- |
  | some thing | some value |

<br/>
<br/>
<br>

## Quotations

Use '>' for quotes.

<br/>
<br/>
<br>

## LaTeX within Markdown

- Add the following at the top of the md file.

  ```md
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
  ```

* Use `$ $` or `$$ $$` to render the LaTeX.

<br>
<br>
<br>

## Math equations

- Writing equation that has an if and else condition

$$T(i,j) = \begin{cases} 1 + T(i-1,j-1) & \text{if } \text{text1}[i] == \text{text2}[j], \\ \max(T(i-1,j), T(i,j-1)) & \text{otherwise}. \end{cases}$$
