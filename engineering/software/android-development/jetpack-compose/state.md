# State

State refers to any data that can change and affect the UI.

<br>
<br>
<br>

## Composition

The Composition is a description of the UI built by Compose when it executes composables.

- Compose apps call composable functions to transform data into UI.

<br>
<br>
<br>

## Recomposition

Recomposition is a process where upon a state change Compose re-executes the affected composable functions and updates the UI.

- The only way to modify the Composition is through recomposition.
- To achieve this Compose needs to know the states to be tracked so that it can schedule the recomposition when it receives an upate. The trackable state is known as [Observable state](#observable-state).

<br>
<br>
<br>

## Observable state

Observable state is a state that is tracked by Compose.

- Observable state can be immutable (read only).
- Observable state can be mutable, Example : `mutableStateOf()`, t receives an initial value as a parameter that is wrapped in a State object, which then makes its value observable.

<br>
<br>
<br>

## State hoisting

State hoisting is a pattern of moving state to its caller to make a component stateless.

- When a state needs to be shared by composables to be used in them, The state must be hoisted higher in the hierarchy.
- In Compose, data flows down (from parent to child) and events flow up (from child to parent).

![image](./_resources/images/state-hoisting-animated.gif)

<br>

When applied to composables, this often means introducing two parameters to the composable:

1. A value: `T` parameter, which is the current value to display.
1. An onValueChange: `(T) -> Unit` – callback lambda, which is triggered when the value changes so that the state can be updated elsewhere, such as when a user enters some text in the text box.

<br>
<br>

### Illustration

Here, the tip is dynamically updated when the user inputs the data.

- `TipCalculator` acts as a parent, holding a Column which stacks the `UserInput` and `TipCalculated` vertically.
- The value entered by the user in the UserInput component is needed in the TipCalculated component, hence the state `amountInput` must be hoisted.

```kt
package com.example.notes

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.safeDrawingPadding
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.notes.ui.theme.NotesTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            NotesTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    TipCalculator(
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }
}
@Composable
fun TipCalculator(modifier: Modifier = Modifier) {
    // 1. STATE IS HOISTED HERE (The Parent)
    var amountInput by remember { mutableStateOf("") }

    Column(modifier = modifier.fillMaxSize().padding(16.dp)) {
        // 2. Pass the state DOWN and the event UP
        UserInput(
            value = amountInput,
            onValueChange = { amountInput = it }
        )

        // 3. Pass the state DOWN to the consumer
        TipCalculated(tip = amountInput)
    }
}

@Composable
fun UserInput(
    value: String,                    // State flows down
    onValueChange: (String) -> Unit,  // Event flows up
    modifier: Modifier = Modifier
) {
    TextField(
        value = value,
        onValueChange = onValueChange,
        label = { Text("Enter bill amount") },
        modifier = modifier.fillMaxWidth(),
        keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
        singleLine = true
    )
}

@Composable
fun TipCalculated(tip: String, modifier: Modifier = Modifier) {
    val amount = tip.toFloatOrNull() ?: 0f
    val calculatedTip = amount * 0.25

    Text(
        text = "Tip (25%): $${String.format("%.2f", calculatedTip)}",
        style = MaterialTheme.typography.headlineSmall
    )
}

@Preview(showBackground = true)
@Composable
fun TipCalculatorPreview() {
    NotesTheme {
        TipCalculator()
    }
}
```
