# QGridLayouts

Facilates the positioning of widgets in terms of rows and columns.

<br>
<br>

## Spacing in QGridLayout

- Use `setColumnMinimumWidth` and `setRowMinimumHeight` for row and column spacing.

  ```cpp
  void QGridLayout::setColumnMinimumWidth(int column, int minSize);
  ```

  ![image](./_assets/qgrid-2.png)

<br>
<br>

## Instances where not to prefer QGridLayout

- If any column contains a small and a large widget then spaing issues will surface. In the following image, column 0 has a QLabel and 2 QCheckBox, there is spacing in rows 1 and 2 towards the right of the QCheckbox.

  ![image](./_assets/qgrid-1.png)
