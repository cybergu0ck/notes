# Grid

- Similarities between flexbox and grid:

  - Both use parent containers with child items.
  - They have similar property names for alignment and positioning.

- Differences between flexbox and grid:

  - Checkout this concise [article](https://css-tricks.com/quick-whats-the-difference-between-flexbox-and-grid/) which higlights some key differences.

<br>

> In fact, not only do each of these modules have their own use cases, but you will also find it helpful to pair Flex and Grid together.

<br>

# Grid Container

- In CSS, an element is turned into a grid container with the property `display: grid` or `display: inline-grid`.
- Each of the **direct** child elements below it automatically become grid items. If we had another element as a child under one of these child elements it would **not** be a grid item.
- Like flexbox, grid items can be grid containers.

* What’s easy about CSS Grid is that you don’t have to assign each child element a property.

* `display:grid` property would stretch to take up space the way a block level box would.

> See image

- `display: inline-grid` would not

> See image

<br>
<br>

# Columns and Rows

- **Tracks** are nothing but columns or rows, technically they are what is present between the grid lines.
- Grid with 2 equal tracks across columns and 2 equal tracks along the rows:

  ```css
  #container {
    display: grid;
    grid-template-columns: 100px 100px;
    grid-template-rows: 50px 50px;
  }
  ```

  > Add Image

- Grid with 2 equal columns and only 1 row
  ````css
  #container {
  display: grid;
  grid-template-columns: 100px 100px;
  grid-template-rows: 50px;
  }```
  > Add Image
  ````
  > add Image

* Using shorthand `grid-template`:

  ```css
  #container {
    display: grid;
    grid-template: 50px / 100px 100px;
  }
  ```

> add image

<br>
<br>

# Implicit and Explicit Grid

- When we use the `grid-template-columns` and `grid-template-rows` properties, we are **_explicitly_** defining grid tracks to lay out our grid items.
- But when the grid needs more tracks for extra content, it will **_implicitly_** define new grid tracks. Additionally, the size values established from our grid-template-columns or grid-template-rows properties are not carried over into these implicit grid tracks. But we can define values for the implicit grid tracks.

* We can set the implicit grid track sizes using the `grid-auto-rows` and `grid-auto-columns` properties. In this way we can ensure any new tracks the implicit grid makes for extra content are set at values that we defined.

<br>

## Illustration

- Consider we have elements more than what could be accomodated explicitely by `grid-template`,

  ```css
  #container {
    display: grid;
    grid-template: 50px / 100px 100px;
  }
  ```

> add more grid items in html and then add Image

- It is more common to add elements further down the grid vertically, this can be done using `grid-auto-rows`

  ```css
  #container {
    display: grid;
    grid-template: 50px / 100px 100px;
    grid-auto-rows: 50px;
  }
  ```

> Add Image

- In case, we want to add elements horizontally, we must use `grid-auto-flow:column` and then `grid-auto-columns`

<br>
<br>

# Gap

- we can set gap between rows and gap between columns seperately using `row-gap` and `column-gap` properties:

  ```css
  #container {
    display: grid;
    grid-template: 50px / 100px 100px;
    row-gap: 10px;
    column-gap: 20px;
  }
  ```

> Keep 4 grid items in the image

- The shorthand `gap` will set the same value for both rows and columns.

  ```css
  #container {
    display: grid;
    grid-template: 50px / 100px 100px;
    gap: 10px;
  }
  ```

<br>
<br>

# Positioning

<br>

## Tracks

- Tracks are nothing but group of cells, present between the grid lines. (tracks are analogous to column and row)

<br>

## Lines

- Whenever we create grid tracks, grid lines are created implicitly. This is important. Grid lines are only created after our grid tracks have been defined. We can not explicitly create grid lines.
- Every track has a start line and an end line.
- The lines are numbered from _left to right_ and _top to bottom_ _starting at 1_.

* **Grid lines are what we use to position grid items.**

<br>

## Cells

- The space in a grid shared by a single row track and a single column track is called a grid cell.
- By default, each child element of a grid container will occupy one cell.

<br>

- As an illustraion, we are positioning different rooms on the floorplan

  ```css
  #floor-plan {
    display: inline-grid;
    grid-template: 50px 50px 50px 50px 50px/ 50px 50px 50px 50px 50px;
    background-color: antiquewhite;
  }

  .living-room {
    grid-column-start: 1;
    grid-column-end: 6;
    grid-row-start: 1;
    grid-row-end: 3;
  }

  .kitchen {
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 3;
    grid-row-end: 6;
  }
  .bed-room {
    grid-column-start: 3;
    grid-column-end: 5;
    grid-row-start: 3;
    grid-row-end: 6;
  }
  .bath-room {
    grid-column-start: 5;
    grid-column-end: 6;
    grid-row-start: 3;
    grid-row-end: 6;
  }
  ```

> Add image (output from pc)

> Add image (hand drawn explanation)

<br>

- The `grid-area` is a shorthand for `grid-row-start` / `grid-column-start` / `grid-row-end` / `grid-column-end`

  ```css
  #floor-plan {
    display: inline-grid;
    grid-template: 50px 50px 50px 50px 50px/ 50px 50px 50px 50px 50px;
    background-color: antiquewhite;
  }

  .living-room {
    grid-area: 1 / 1 / 3 / 6;
  }

  .kitchen {
    grid-area: 3 / 1 / 6 / 3;
  }

  .bed-room {
    grid-area: 3 / 3 / 6 / 5;
  }

  .bath-room {
    grid-area: 3 / 5 / 6 / 6;
  }
  ```

- Yet Another way is to use a `grid-template-areas` consisting of names (layouted properly) and using those names as values for `grid-area` property

  ```css
  #floor-plan {
    display: inline-grid;
    grid-template: 50px 50px 50px 50px 50px/ 50px 50px 50px 50px 50px;
    background-color: antiquewhite;
    grid-template-areas:
      "living living living living living"
      "living living living living living"
      "kitchen kitchen bedroom bedroom bathroom"
      "kitchen kitchen bedroom bedroom bathroom"
      "kitchen kitchen bedroom bedroom bathroom";
  }

  .living-room {
    grid-area: living;
  }

  .kitchen {
    grid-area: kitchen;
  }

  .bed-room {
    grid-area: bedroom;
  }

  .bath-room {
    grid-area: bathroom;
  }
  ```
