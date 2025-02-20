# Strategy Pattern

<br>
<br>

## Theory

The strategy patterm encapsulates a family of interchangable startegies(algorithms) and facilitates the client to select one at runtime.

<br>

![image](./_assets/strategy1.png)

<br>

### Components

1. Context : The component that holds the reference to the selected strategy and logic to execute it.

1. Strategy : The component containing specific algorithm.

   - Implemented via an interface.
   - Generally present as a family.

1. Client : The component that chooses the specific concrete strategy and uses the context to execute it.

<br>

### Applicability

1. Choosing a strategy from a family of strategies at runtime.

<br>

### Advantages

1. Flexibilty to chose a particular strategy at runtime.
1. Adheres to [open-close principle](../../object-oriented-programming/principles.md#open-close-principle)
1. Isolation of implementation of strategy.
1. Loose coupling of client and strategy code. see [coupling](../../object-oriented-programming/principles.md#coupling)

<br>

### Disadvantages

1. Client and strategies are not completely decoupled, as the client needs to be aware of the different strategies available to choose the appropriate one.

<br>

## Application

<br>

![image](./_assets/strategy2.png)

<br>

```cpp
#include <iostream>
#include <memory>

// interface for strategy
class IPaymentSystem
{
public:
    virtual ~IPaymentSystem() = default;
    virtual void pay() = 0;
};

// concrete strategy
class NetBankSystem : public IPaymentSystem
{
public:
    NetBankSystem() {}
    ~NetBankSystem() override {}
    void pay() override
    {
        std::cout << "simulate payment done using netbank" << '\n';
    }
};

// concrete strategy
class CreditCardSystem : public IPaymentSystem
{
public:
    CreditCardSystem() {}
    ~CreditCardSystem() override {}
    void pay() override
    {
        std::cout << "simulate payment done using credit card" << '\n';
    }
};

// context
class ShoppingCart
{
private:
    std::shared_ptr<IPaymentSystem> payment_processor;

public:
    enum PAYMENT_MODE
    {
        CREDIT_CARD,
        NETBANK
    };
    ShoppingCart()
    {
    }
    ~ShoppingCart() {}
    void set_payment_system(std::shared_ptr<IPaymentSystem> service)
    {
        this->payment_processor = service;
    }
    void execute_payment()
    {
        this->payment_processor->pay();
    }
};

// client, assume this to be an app which "owns a" shoping cart object
int main()
{
    ShoppingCart cart;
    std::cout << "Type 0 for credit card and 1 for netbank" << "\n";
    int mode{};
    std::cin >> mode;
    std::shared_ptr<IPaymentSystem> processor;
    if (ShoppingCart::CREDIT_CARD == mode)
    {
        processor = std::make_shared<CreditCardSystem>();
    }
    else if (ShoppingCart::NETBANK == mode)
    {
        processor = std::make_shared<NetBankSystem>();
    }
    processor->pay();
}
```

<br>

### Components

The family of strategies represents the family of payment systems.

1. Strategy : `NetBankSystem` and `CreditCardSystem`, components containing specific algorithm.

   - `IPaymentSystem`is the interface for the family of payment systems.

1. Context : `ShoppingCart` class has a the `payment_processor`, a referance to a payment system via the `IPaymentSystem` interface and `execute_payment` to execute the payment system's `pay` method.

1. Client : `main` function selects the appropriate concrete strategy and uses `ShoppingCart` to `execute_payment`.

<br>

### Applicability

1. choosing a strategy from a family of strategies at runtime.

<br>

### Advantages

1.  Flexibilty to chose a particular strategy at runtime.

    - The payment system can be chosen by the user at run time.

1.  Adheres to [open-close principle](../../object-oriented-programming/principles.md#open-close-principle).

    - A new payment system can be added to the system without modifying the existing code.

1.  Isolation of implementation of strategy.

    - Neither the context nor the client knows about the implementation details of the strategies.

1.  Decoupling of client and strategy code. see [decoupling](../../object-oriented-programming/principles.md#decoupling)

    - Client is independant from the implementation of the strategies and interacts with it using the interface's `pay` method via context's `execute_payment` method.
    - Client and strategies are not completely decoupled. see [below](#disadvantages-1)

<br>

### Disadvantages

1. Client needs to be aware of the different strategies available and about choosing the appropriate one.

   - In this particular implementation of the system, it is appropriate for `ShoppingCart` to have an instance of `IPaymentSystem` and hence it contains the enum `PAYMENT_MODE`.
   - Nevertheless, client is dependant on the information regarding the number of available payment systems.

<br>
<br>
