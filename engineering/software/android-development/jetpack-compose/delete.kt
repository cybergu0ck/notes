
@Composable
fun BillDetailsScreen(modifier: Modifier) {
    val billOptions = listOf("Quotation", "Invoice")
    var selectedBillOption by remember { mutableStateOf(billOptions[0]) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(start = 40.dp, top = 80.dp, end = 40.dp, bottom = 40.dp)
            .verticalScroll(rememberScrollState()), // Allows scrolling if keyboard covers fields
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        Text(text = "Select Document Type:", style = MaterialTheme.typography.labelLarge)
        Row(verticalAlignment = Alignment.CenterVertically) {
            billOptions.forEach { text ->
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    modifier = Modifier.padding(end = 16.dp)
                ) {
                    RadioButton(
                        selected = (text == selectedBillOption),    //state hoisting to be done here
                        onClick = { selectedBillOption = it }       //state hoisting to be done here
                    )
                    Text(text = text, modifier = Modifier.padding(start = 4.dp))
                }
            }
        }
    }
}
