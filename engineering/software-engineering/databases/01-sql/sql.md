# Comments in SQL

- single line comments using `-- comment`
- multiline comments using `/* comment */`

<br>
<br>

# Creating Database

```sql
create  database record_company;
```

<br>
<br>

# Delete Database

```sql
drop database record_company;
```

<br>
<br>

# Using the Databse

```sql
use record_company;
```

<br>
<br>

# Create Tables

```
create table <name>(
    <col name> <data type>,
    <col name> <data type>,
    <col name> <data type>,...
);
```

```sql
create table toys (
  toy_name varchar(100),
  colour   varchar(10),
  price    int
);
```

<br>
<br>

# Inserting values into a table

```
insert into <table> values (<colum value>, <colum value>,... )
```

```sql
insert into toys values ( 'Sir Stripypants', 'red', 0.01 );
insert into toys values ( 'Miss Smelly_bottom', 'blue', 6.00 );
insert into toys values ( 'Cuteasaurus', 'blue', 17.22 );
insert into toys values ( 'Mr Bunnykins', 'red', 14.22 );
insert into toys values ( 'Baby Turtle', 'green', null );
```

<br>
<br>

# Selecting Rows

- To get all rows for specified columns.

  ```
  select <needed> from <table>
  ```

  ```sql
  select * from toys  -- select all colums
  select colour, price from toys --select only colour and price colums
  ```

* Filtering rows to get specific rows

  ```
  select <column> from <table> where <criteria>
  ```

  ```sql
  select * from toys where toy_name='Sir Stripypants';  --gets all columns for rows with the given criteria
  ```

* `and` and `or` can be used to combine the criteria

  ```sql
  select * from toys where toy_name='Sir Stripypants' or colour = 'green';
  ```

  > <br>
  > Order of Precedence:  <br>
  > AND has higher priority than OR. So if you include both in a where clause, the order you place them affects the results. <br>
  > <br>

  ```sql
  select * from toys
  where  toy_name = 'Mr Bunnykins' or toy_name = 'Baby Turtle'
  and    colour = 'green';

  -- toy_name = 'Mr Bunnykins' or (toy_name = 'Baby Turtle' and    colour = 'green')
  ```

  ```sql
  select * from toys
  where  colour = 'green'
  and    toy_name = 'Mr Bunnykins' or toy_name = 'Baby Turtle';

  -- (colour = 'green' and    toy_name = 'Mr Bunnykins') or toy_name = 'Baby Turtle'
  ```

* To avoid confusion in queries combining AND with OR, use parentheses. The database processes conditions inside the brackets first.
