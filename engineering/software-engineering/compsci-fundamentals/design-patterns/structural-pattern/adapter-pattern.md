# Adapter Pattern

_The Adapter design pattern is a structural pattern that allows objects with incompatible interfaces to work together._

<br>
<br>

## About The Adapter Pattern

<br>

### Components

<br>

### Applicability

<br>

### Benefits

<br>

### Consequences

<br>
<br>

## Illustration

```cpp
#include <iostream>

class I_LegacyDatabase {
public:
	virtual void establishConnection(const std::string connection_id="") = 0;
};

class LegacyDB : public I_LegacyDatabase {
public:
	void establishConnection(const std::string connection_id) override {
		std::cout << "simulating connection mechanism for legacy db" << "\n";
	}
};

class ModernDB {
public:
	void connect(int port) {
		std::cout << "simulating connection mechanism for modern db" << "\n";
	}
};

class DatabaseAdapter : public I_LegacyDatabase {
private:
	ModernDB* modern_db;
public:
	void establishConnection(const std::string connection_id) override {
		int port = getPort();
		modern_db->connect(port);
	}
	int getPort() {
		//implement the API
		return 123;
	}
};

int main() {
	I_LegacyDatabase* db1 = new LegacyDB();
	db1->establishConnection("uniquestring"); //simulating connection mechanism for legacy db

	I_LegacyDatabase* db2 = new DatabaseAdapter();
	db2->establishConnection();	//simulating connection mechanism for modern db
}
```
