# Creating Database

```sql
CREATE  DATABASE record_company;
```

<br>
<br>

# Delete Database

```sql
DROP DATABASE record_company;
```

<br>
<br>

# Using the Databse

```sql
USE record_company;
```

<br>
<br>

# Create Tables

```sql
CREATE TABLE bands(
    column1 INT
    column2 VARCHAR
);
```

```sql
create  database record_company;
use record_company;

create table bands(
 id int not null auto_increment,
 name varchar(255) not null,
 primary key (id)
);

create table albums(
	id int not null auto_increment,
    name varchar(255) not null,
    release_year int,
    band_id int not null,
    primary key (id),
    foreign key (band_id) references bands(id)
);

insert into bands (name)
values ('iron maiden');

insert into bands (name)
values ('deuce'),('avenged sevenfold'), ('ankor');

select * from bands;  	-- selects every column and every row from bands

select name from bands;	-- queries the name column and all the rows

select id as 'ID', name as 'Band Name' from bands;	-- queries the required but modifies the titles temporarily

select * from bands order by name;		-- orders in ascending order by name column values
select * from bands order by name desc;	-- orders in descending order by name column values



insert into albums(name, release_year, band_id)
values ('The Number of the beasts', 1985, 1),
		('Power slave', 2018, 1 ),
        ('Nightmare', 2018, 2),
        ('Nightmare', 2010, 3),
        ('test album', NULL,3);

insert into albums(name, release_year, band_id)
values ("delete", NULL, 1);

select id from albums where name = "delete";

delete from albums where id = 11;

select * from albums;

select distinct name from albums;

update albums
set release_year = 1982 where id =6;

select * from albums where release_year < 2000;

select * from albums where name like '%er%';




```
