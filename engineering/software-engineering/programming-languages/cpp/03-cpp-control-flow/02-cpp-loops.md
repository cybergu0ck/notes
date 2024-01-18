# Loops

## For Loop

```cpp
#include <iostream>

int main() {
	for (int i{ 0 }; i < 5; i++) {
		std::cout << i << "\t";
	}
}

//0       1      2       3       4
```

<br>
<br>

## Range Based For Loop

```cpp
#include <iostream>

int main() {
	int arr[5]{1,26,3,4,5 };
	for (auto item: arr) {
		std::cout << item << "\t";
	}
}

//1       26      3       4       5
```

<br>
<br>

## While Loop

```cpp
#include <iostream>

int main() {
	int current{ 0 };
	int max_limit{ 5 };
	while (current <= max_limit) {
		std::cout <<  current << " ";
		++current;
	}
}
// 0 1 2 3 4
```

<br>
<br>

## Do While Loop

```cpp
#include <iostream>

int main() {
    int userInput;
    do {
        std::cout << "Enter a positive integer: ";
        std::cin >> userInput;
        if (userInput <= 0) {
            std::cout << "Invalid input. Please enter a positive integer.\n";
        }
    } while (userInput <= 0);

    std::cout << "You entered: " << userInput << std::endl;
    return 0;
}
```
