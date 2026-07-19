
# Navigation

The Navigation component has three main parts:

- **NavController:** Responsible for navigating between destinations.
- **NavGraph:** Maps composable destinations to navigate to.
- **NavHost:** Composable acting as a container for displaying the current destination of the NavGraph.

<br>
<br>
<br>

## Route

A route is a string that maps to a destination and serves as its unique identifier.
- A destination is typically a single Composable or group of Composables corresponding to what the user sees.
- Routes are defined using enums.

```kt
enum class AppScreen() {  
    First,  
    Second  
}
```
- In the above code, `First` and `Second` are routes.

<br>
<br>
<br>

## NavHost

A NavHost is a Composable that displays other composable destinations, based on a given route.

```kt
NavHost(
	navController,
	startDestination,
	modifier,
){
	content
}
```

- `navController`: An instance of the `NavHostController` class used to navigate between screens using it's `navigate()` method. 
- `startDestination`: A string route defining the destination shown by default when the app first displays the `NavHost`. 


<br>
<br>
<br>

## Sharing externally

<br>
<br>


### Intent

An intent is a request for the system to perform some action, commonly presenting a new activity.
- There are many different intents

<br>
<br>
<br>

## Illustration


The following implementation is required in the "build.gradle.kts" file inside the app directory.

```
implementation("androidx.navigation:navigation-compose:2.7.4")
```


The following is Screens.kt file in the "ui" directory containing the UI code.

```kt
package com.example.learn_nav.ui  
  
import androidx.compose.foundation.layout.Arrangement  
import androidx.compose.foundation.layout.Box  
import androidx.compose.foundation.layout.Column  
import androidx.compose.foundation.layout.Row  
import androidx.compose.foundation.layout.Spacer  
import androidx.compose.foundation.layout.fillMaxWidth  
import androidx.compose.foundation.layout.height  
import androidx.compose.foundation.layout.padding  
import androidx.compose.material3.Button  
import androidx.compose.material3.Card  
import androidx.compose.material3.MaterialTheme  
import androidx.compose.material3.OutlinedButton  
import androidx.compose.material3.Scaffold  
import androidx.compose.material3.Text  
import androidx.compose.runtime.Composable  
import androidx.compose.ui.Modifier  
import androidx.compose.ui.unit.dp  
  
  
  
@Composable  
fun TopCard(title: String, description: String) {  
    Card(  
        modifier = Modifier.fillMaxWidth().padding(16.dp)  
    ) {  
        Column(modifier = Modifier.padding(16.dp)) {  
            Text(title, style = MaterialTheme.typography.titleLarge)  
            Spacer(Modifier.height(8.dp))  
            Text(description, style = MaterialTheme.typography.bodyMedium)  
        }  
    }}  
  
@Composable  
fun FirstScreen(  
    onNextClick: () -> Unit) {  
    Scaffold(  
        bottomBar = {  
            Button(  
                onClick = onNextClick,  
                modifier = Modifier.fillMaxWidth().padding(16.dp)  
            ) {  
                Text("Continue")  
            }  
        }    ) { paddingValues ->  
        Box(modifier = Modifier.padding(paddingValues)) {  
            TopCard(  
                title = "Welcome to Screen One",  
                description = "This screen features a single, prominent call-to-action button anchored perfectly at the bottom."  
            )  
        }  
    }}  
  
@Composable  
fun SecondScreen(onBackClick: () -> Unit, onSubmitClick: () -> Unit) {  
    Scaffold(  
        bottomBar = {  
            Row(  
                modifier = Modifier.fillMaxWidth().padding(16.dp),  
                horizontalArrangement = Arrangement.spacedBy(16.dp)  
            ) {  
                OutlinedButton(onClick = onBackClick, modifier = Modifier.weight(1f)) {  
                    Text("Back")  
                }  
                Button(onClick = onSubmitClick, modifier = Modifier.weight(1f)) {  
                    Text("Submit")  
                }  
            }        }    ) { paddingValues ->  
        Box(modifier = Modifier.padding(paddingValues)) {  
            TopCard(  
                title = "Almost There: Screen Two",  
                description = "Here we use a Row with Modifier.weight(1f) to ensure both buttons split the bottom width evenly."  
            )  
        }  
    }}
```


The following is the main app, also contains the navigation code.
```kt
package com.example.learn_nav  
  
import android.content.Context  
import android.content.Intent  
import android.os.Bundle  
import androidx.activity.ComponentActivity  
import androidx.activity.compose.setContent  
import androidx.activity.enableEdgeToEdge  
import androidx.compose.foundation.layout.fillMaxSize  
import androidx.compose.foundation.layout.padding  
import androidx.compose.material3.Scaffold  
import androidx.compose.runtime.Composable  
import androidx.compose.ui.Modifier  
import androidx.compose.ui.platform.LocalContext  
import androidx.compose.ui.tooling.preview.Preview  
import com.example.learn_nav.ui.theme.LearnnavTheme  
import androidx.navigation.NavHostController  
import androidx.navigation.compose.NavHost  
import androidx.navigation.compose.rememberNavController  
import androidx.navigation.compose.composable  
import com.example.learn_nav.ui.FirstScreen  
import com.example.learn_nav.ui.SecondScreen  
  
enum class AppScreen() {  
    First,  
    Second  
}  
  
private fun onCancel(  
    navController: NavHostController  
) {  
    navController.popBackStack(AppScreen.First.name, inclusive = false)  
}  
  
private fun shareExternally(context: Context, subject: String, summary: String) {  
    val intent = Intent(Intent.ACTION_SEND).apply {  
        type = "text/plain"  
        putExtra(Intent.EXTRA_SUBJECT, subject)  
        putExtra(Intent.EXTRA_TEXT, summary)  
    }  
    context.startActivity(  
        Intent.createChooser(  
            intent,  
            "Dummy"  
        )  
    )  
}  
  
@Composable  
fun App(  
    navController: NavHostController = rememberNavController(),  
    modifier: Modifier = Modifier) {  
    val context = LocalContext.current  
    NavHost(  
        navController = navController,  
        startDestination = AppScreen.First.name,  
    ) {  
        composable(route = AppScreen.First.name) {  
            FirstScreen(onNextClick = {navController.navigate(AppScreen.Second.name)})  
        }  
        composable(route = AppScreen.Second.name) {  
            SecondScreen(  
                onBackClick = {onCancel(navController)},  
                onSubmitClick = {shareExternally(context, "Subject", "Summary")}  
            )  
        }  
    }}  
  
  
class MainActivity : ComponentActivity() {  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
        enableEdgeToEdge()  
        setContent {  
            LearnnavTheme {  
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->  
                    App(  
                        modifier = Modifier.padding(innerPadding)  
                    )  
                }  
            }        }    }  
}
```

- Note how `NavController` and `NavHost` are used in the `App` composable.