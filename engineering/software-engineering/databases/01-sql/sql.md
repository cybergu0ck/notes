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
