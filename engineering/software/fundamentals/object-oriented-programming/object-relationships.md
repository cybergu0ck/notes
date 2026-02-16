# Object relationships

<br>
<br>
<br>

## Association

A relationship where objects are connected but exist independently.

<br>
<br>
<br>

## Aggregation

A "has-a" relationship where one object contains references to other independent objects.

<br>
<br>
<br>

## Composition

A strong "owns-a" relationship where contained objects cannot exist without the container

<br>
<br>
<br>

## Differences

| feature               | association   | aggregation                                               | composition                                             |
| --------------------- | ------------- | --------------------------------------------------------- | ------------------------------------------------------- |
| lifetime dependancy   | no dependancy | container and contained object have independant lifetimes | contained object is destroyed when the container ceases |
| relationship strength | weakest       | medium                                                    | strongest                                               |
| relationship type     | "knows about" | "has a"                                                   | "owns a"                                                |
| uml notation          | simple line   | line with hollow diamond                                  | line with filled diamond                                |

<br>
<br>
<br>

## UML

- uml for illustrating relationshis

  ![uml](./_resources/images/uml-lines.png)

- The arrows point from bottom to top i.e. from child to parent.

  ![uml](./_resources/images/uml-direction.png)
