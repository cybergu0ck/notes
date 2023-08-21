# Filtering Data

- Assuming the table to be

  | toy_name             | colour  | price |
  | -------------------- | ------- | ----- |
  | 'Sir Stripypants'    | 'red'   | 0.01  |
  | 'Miss Smelly_bottom' | 'blue'  | 6.00  |
  | 'Cuteasaurus'        | 'blue'  | 17.22 |
  | 'Mr Bunnykins'       | 'red'   | 14.22 |
  | 'Baby Turtle'        | 'green' | null  |

<br>
<br>

## Selecting Columns

- Selecting all columns (we are not filtering rows at the moment)

  ```
  select * from <table>
  ```

  ```sql
  select * from toys  -- select all colums
  ```

- Selecting only specific columns.

* To get all rows for specified columns. (we are not filtering rows at the moment)

  ```
  select <column,...> from <table>
  ```

  ```sql
  select colour, price from toys --select only colour and price colums
  ```

<br>
<br>

## Selecting Rows

- All rows are selected by default.
- Rows are filtered using `WHERE` clause.

* Filtering rows to get specific rows

  ```
  select * from <table> where <criteria>
  ```

  ```sql
  select * from toys where toy_name='Sir Stripypants';  --gets all columns for rows with the given criteria
  ```

<br>

### AND and OR

- `AND` and `OR` can be used to combine the criteria

  ```sql
  select * from toys where toy_name='Sir Stripypants' or colour = 'green';
  ```

  - ORDER OF PRECEDENCE: AND has higher priority than OR. So if you include both in a where clause, the order you place them affects the results.
  - To avoid confusion in queries combining AND with OR, use parentheses. The database processes conditions inside the brackets first.

    ```sql
    select * from toys
    where  toy_name = 'Mr Bunnykins' or toy_name = 'Baby Turtle' and    colour = 'green';
    -- toy_name = 'Mr Bunnykins' or (toy_name = 'Baby Turtle' and    colour = 'green')
    ```

    ```sql
    select * from toys
    where  colour = 'green'
    and    toy_name = 'Mr Bunnykins' or toy_name = 'Baby Turtle';

    -- (colour = 'green' and    toy_name = 'Mr Bunnykins') or toy_name = 'Baby Turtle'
    ```

<br>

### LIKE

- When searching strings, you can find rows matching a pattern using `LIKE`.
- The two wildcard characters are
  - Underscore ( \_ ) that matches exactly one character.
  - Percent ( % ) that matches zero or more characters.

```sql
select * from toys where toy_name like '%e' -- selects rows where toy_name ends with the letter e.
select * from toys where toy_name like 'm%' -- selects rows where toy_name starts with the letter m.
select * from toys where toy_name like '___________' -- selects rows where toy_name is exactly 11 letters.
select * from toys where colour like '_e_' -- any colour with exactly one character either side of e (red).
select * from toys where colour like '%e%' -- any colour that contains e anywhere in the string (red, blue, green)
```

<br>

### IS NULL

- The result of compraing a value to null is unknown. WHERE classes only return rows where the tests are true. Hence `is null` is used to filter data with null in it.

  ```sql
  select toy_name from toys where price is null
  ```

<br>

### NOT

- We can use `NOT` to return the opposite of most conditions.

  ```sql
  select toy_name from toys where color not blue
  select toy_name from toys where color != blue  -- same as above
  select toy_name from toys where color <> blue  -- same as above
  ```

- One exception to this is null. Searching for rows that are NOT equal to null still returns nothing. Instead use `is not null`
