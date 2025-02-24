```cpp
#include <iostream>

template<typename T>
class Sharedptr {

public:
	T* resource;
	int* ref_count;

	void increment_ref()
	{
		if (ref_count)
		{
			(*ref_count)++;
			std::cout << "Incremented ref_count to " << *ref_count << std::endl;
		}
	}

	void decrement_ref()
	{
		if (ref_count)
		{
			(*ref_count)--;
			std::cout << "Decremented ref_count to " << *ref_count << std::endl;

			if (*(ref_count) == 0)
			{
				if (resource)
				{
					delete resource;
					std::cout << "Deleted resource" << std::endl;
				}
				if (ref_count)
				{
					delete ref_count;
					std::cout << "Deleted ref_count" << std::endl;
				}
			}
		}
	}

	Sharedptr():resource{nullptr}, ref_count{new int(1)}
	{
		std::cout << "Default constructor called, ref_count = " << *ref_count << std::endl;
	}
	Sharedptr(T* data):resource{data}, ref_count{new int(1)}
	{
		std::cout << "Parameterized constructor called, ref_count = " << *ref_count << std::endl;
	}

	Sharedptr(const Sharedptr<T>& rhs): resource{rhs.resource}, ref_count{rhs.ref_count}
	{
		this->increment_ref();
		std::cout << "Copy constructor called" << std::endl;
	}

	Sharedptr& operator=(const Sharedptr<T>& rhs)
	{
		if (this != &rhs)
		{
			this->decrement_ref();
			resource = rhs.resource;
			ref_count = rhs.ref_count;
			this->increment_ref();
		}
		std::cout << "Assignment operator called" << std::endl;
		return *this;
	}

	~Sharedptr()
	{
		this->decrement_ref();
		std::cout << "Destructor called" << std::endl;
	}

	//move constructor and move assignment operator is missing
};

class Test {
public:
	Test() {
		std::cout << "Test object created" << std::endl;
	}
	~Test() {
		std::cout << "Test object destroyed" << std::endl;
	}
};

int main() {
	{
		std::cout << "Creating sp1 with default constructor" << std::endl;
		Sharedptr<Test> sp1;

		std::cout << "\nCreating sp2 with parameterized constructor" << std::endl;
		Sharedptr<Test> sp2(new Test);

		std::cout << "\nCreating sp3 with copy constructor from sp2" << std::endl;
		Sharedptr<Test> sp3 = sp2;

		std::cout << "\nAssigning sp1 to sp2" << std::endl;
		sp1 = sp2;

		std::cout << "\nCreating sp4 with copy constructor from sp1" << std::endl;
		Sharedptr<Test> sp4(sp1);
	}
	std::cout << "\nEnd of main, all Sharedptr instances should be destroyed" << std::endl;

	return 0;
}
```
