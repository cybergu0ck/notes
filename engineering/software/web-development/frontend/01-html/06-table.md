# HTML Table

All the contents of the table must be enclosed within `<table>` tags.

<br>
<br>

## Headers, Rows and Columns

- Headers are enclosed in `<th>`. (th stands for table header)
- Rows are enclosed in `<tr>`. (tr stands for table row)
- Column entries are enclosed in `<td>`. (td stands for table data)

* This illustration shows a table generated using the following html and css code.

  ```html
  <table>
    <tr>
      <th>Subject</th>
      <th>Fav Ranking</th>
    </tr>
    <tr>
      <td>Physics</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Engineering</td>
      <td>1</td>
    </tr>
    <tr>
      <td>History</td>
      <td>3</td>
    </tr>
  </table>
  ```

  ```css
  html {
    font-family: sans-serif;
  }

  table {
    border-collapse: collapse;
    border: 2px solid rgb(200, 200, 200);
    letter-spacing: 1px;
    font-size: 0.8rem;
  }

  td,
  th {
    border: 1px solid rgb(190, 190, 190);
    padding: 10px 20px;
  }

  th {
    background-color: rgb(235, 235, 235);
  }

  td {
    text-align: center;
  }

  tr:nth-child(even) td {
    background-color: rgb(250, 250, 250);
  }

  tr:nth-child(odd) td {
    background-color: rgb(245, 245, 245);
  }

  caption {
    padding: 10px;
  }
  ```

  ![table](./_assets/table1.png)

<br>
<br>
