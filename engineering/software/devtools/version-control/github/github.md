
# Linking in github markdown files


## Same-file anchors

* For backlinks (on same file) to work on github, Refer [official github doc](https://gist.github.com/TobiasPalludan/5948533e97d260a04ea47e44ea7cc6b0), else see below:

    ```
    [text](#<syntaxed_heading>)
    ```

* syntaxed_heading is the heading with these conversion rules applied

    - punctuation marks will be dropped from the heading.
    - leading white spaces will be dropped from the heading.
    - upper case will be converted to lower in the heading.
    - spaces between letters in the heading will be converted to '-'

    ```
    ## Title

    ### Place 1

    Hello, this is some text to fill in this, [here](#place-2), is a link to the second place.

    ### Place 2

    Place one has the fun times of linking here, but I can also link back [here](#place-1).

    ### Place's 3: other example

    Place one has the fun times of linking here, but I can also link back [here](#places-3-other-example).
    ```

* For more reference [check this stackoverflow thread](https://stackoverflow.com/questions/27981247/github-markdown-same-page-link#:~:text=Note%20how%20in%20the%20example,here%5D(%23place%2D2)%20.&text=If%20you%20have%202%20or,be%20place%2D2%2D1%20.)

* Illustration: To backlink the top most heading of this file [the top most heading](#same-file-anchors)

<br/>
<br/>


## Cross-file anchors  

* See [official-docs](https://gist.github.com/TobiasPalludan/5948533e97d260a04ea47e44ea7cc6b0) else see below:

    - Add filename.md in font of the header link. (i.e. `[text](filename.md#header)`)
    - Use linux's `cd` command if files are present in other directory (i.e. `[text](../prev-folder/filename.md#header)`)



