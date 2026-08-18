# Count Color

Use case is to count the number of cells based on color (fill).

<br>
<br>

## Enable Developer Tab in the Ribbon

1. In the **Home** Tab, hover over the empty space in the ribbon and **Right Click**.
2. Select **Customise the Ribbon**.
3. Change the dropdown from **Popular Commands** to **All Tabs**.
4. Find **Developer** Section and Click **Add >>**.
5. Click Ok and the Developer tab must be present in the ribbon.

<br>
<br>

## Enter VBA mode

- Go to **Developer** Tab
- Click **Visual Basic** Option

<br>
<br>

## Add the functions in VB

- After opening VBA mode
- Click **Insert** and select _Module_.
- Add the following code and exit back to the spreadsheet.

  ```vb
  Function CountCellsByColor(data_range As Range, cell_color As Range) As Long
  Dim indRefColor As Long
  Dim cellCurrent As Range
  Dim cntRes As Long

  Application.Volatile
  cntRes = 0
  indRefColor = cell_color.Cells(1, 1).Interior.Color
  For Each cellCurrent In data_range
      If indRefColor = cellCurrent.Interior.Color Then
      cntRes = cntRes + 1
      End If
  Next cellCurrent

  CountCellsByColor = cntRes
  End Function

  Function CountCellsByFontColor(data_range As Range, font_color As Range) As Long
  Dim indRefColor As Long
  Dim cellCurrent As Range
  Dim cntRes As Long

  Application.Volatile
  cntRes = 0
  indRefColor = font_color.Cells(1, 1).Font.Color
  For Each cellCurrent In data_range
      If indRefColor = cellCurrent.Font.Color Then
      cntRes = cntRes + 1
      End If
  Next cellCurrent

  CountCellsByFontColor = cntRes
  End Function
  ```

<br>
<br>

## Using the function

- The first argument is the area of the cells where we need to count colors, second is the cell whose color will be used for calculation

  ```
  =CountCellsByColor(A:A,D2)
  ```

- use `Alt + F9` to run (and hence update the values) the formulas in the workbook.

<br>
<br>

## References

- Watch [this](https://www.youtube.com/watch?v=fwSIIDm08fo&t=210s&ab_channel=JopaExcel) video for the entire preocess, especially launching VBA mode
- [This](https://www.ablebits.com/office-addins-blog/count-sum-by-color-excel/) page has to the code for the functions.
