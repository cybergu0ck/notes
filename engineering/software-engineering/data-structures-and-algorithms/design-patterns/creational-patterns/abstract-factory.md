# Abstract Factory Pattern

**_The Abstract Factory design pattern is a creational pattern that helps creation of families of related objects without specifying their concrete classes._**

<br>

![img](./_assets/abstract-factory-uml.png)

### Components

1. **Products** are designed using abstract classes for interface and concrete classes for implementation.

2. **Families** of products are created using Factories. Abstract factory serves as an interface and each concrete factory _"makes"_ products for the specific family it represents.

3. **Client** uses a concrete factory via the abstract factory.

<br>

### Applicability

1. This pattern is helpful to design _"families of related products that are to work together"_.
2. This pattern is helpful in usecases where client is independent of how its products are created, composed, and represented.

<br>

### Benefits

Beyond its applicability to the above outlined use cases, the pattern offers:

1. Encapsulation of implementations of the products.
2. Flexibility to modify existing implementation.
3. Flexibility to add a new families without breaking existing code. (_Given the new family also contains equal number of products as before_)

<br>

### Consequences

1. Decreases code readability due to added complexity.
1. Although there is flexibility to add new families, However there is no flexibilty to add new products as it breaks existing code.

<br>
<br>

## Illustration

![img](./_assets/abstract-factory-illus.png)

```cpp
#include <iostream>

//Abstract Products
class I_Label {
public:
    virtual void setText(std::string text) = 0;
};

class I_Button {
public:
    virtual void setSize(int size) = 0;
};

class I_UI {
public:
    virtual void addLabel(I_Label* label) = 0;
    virtual void addButton(I_Button* btn) = 0;
};

//Concrete Products
class LoginLabel : public I_Label {
public:
    void setText(std::string text) override {
        //Implemention for setting the text for the label
    }
};

class LoginButton : public I_Button {
public:
    void setSize(int size) override {
        //Implementation for event handler for the button click
    }
};

class LoginUI : public I_UI {
public:
    LoginUI() :login_button{ nullptr }, login_label{ nullptr } {}
    ~LoginUI() {
        delete login_label;
        delete login_button;
    }
    void addLabel(I_Label* label) override {
        login_label = label;
    }
    void addButton(I_Button* btn) override {
        login_button = btn;
    }
protected:
    I_Label* login_label;
    I_Button* login_button;
};

//Abstract Factory
class I_UIFactory {
public:
    virtual I_UI* makeUI() = 0;
    virtual I_Label* makeLabel() = 0;
    virtual I_Button* makeButton() = 0;
};

//Concrete Factory
class LoginUIFactory : public I_UIFactory {
public:
    LoginUI* makeUI() {
        return new LoginUI();
    }
    LoginLabel* makeLabel() {
        LoginLabel* label = new LoginLabel();
        label->setText("Existing User?");
        return label;
    }
    I_Button* makeButton() {
        LoginButton* btn = new LoginButton();
        btn->setSize(5);
        return btn;
    }
};

//Client
class App {
public:
    App() {
        createLoginUI();
    }
    ~App() {
        delete login_ui;
        delete login_factory;
    }
protected:
    I_UI* login_ui;
    LoginUIFactory* login_factory;
    I_UI* createUI(I_UIFactory* factory) {
        I_UI* ui = factory->makeUI();
        I_Label* label = factory->makeLabel();
        I_Button* button = factory->makeButton();
        ui->addLabel(label);
        ui->addButton(button);
        return ui;
    }

    void createLoginUI() {
        login_factory = new LoginUIFactory();
        login_ui = createUI(login_factory);     //Use of the factory!
    }
};

int main() {
    App my_app = App();
}
```

<br>

### Classes

1. label, button and ui are products.

   - `I_Label`, `I_Button` and `I_UI` are abstract classes of the products that serves an interface for the concrete implementations.
   - `LoginLabel`, `LoginButton` and `LoginUI` are the concrete products of a same family i.e. "Login". They have public methods which may be used in the implementations of methods in the concrete factory.

2. LoginFactory makes the products for the "Login" family.

   - `I_UIFactory` is an abstract factory that serves as an interface for the concrete implementation of the factories. All the methods in this class are mostly pure virtual functions. Generally, they donot take any parameters aswell.
   - `LoginUIFactory` is a concrete factory. The methods "make" each product as required. (Uses the public metods of the products)

3. App is the client
   - `App` is a client class. It has a method to create different UI's by using appropriate factory.

- Note that classes containing pointers as members most likely has constructors and destructors to initialise and clean up.

<br>

### Applicability

1. This pattern is helpful to design a _"families of related products that are to work together"_.

   - In this illlustration, the products are UI, Label and Button and the family is "Login".

2. This pattern is helpful in usecases where client is independent of how its products are created, composed, and represented. (Another way of saying this: Client is isolated from the type of porducts created)
   - Client code doesn't contain any references to concrete classes (other than instantiation of the concrete factory), it contains the abstract classes in the type definitions and just calls the _"make"_ methods of the factory object. Hence doesn't know how the product is created, composed or represented.

<br>

### Benefits

1. Encapsulation of implementations of the products.

2. Flexibility to modify existing implementation.

   - Each product has an abstract base class serving as an interface.
   - Product's implementations are encapsulted as products are exposed only via interfaces.

3. Flexibility to add a new families without breaking existing code. (_Given the new family also contains equal number of products as before_)
   - Adding a new family is as easy as creating the concrete classes for all the products and creating a concrete factory class. The client code has only interface definitions, hence passing this new factory would work in the exiting code.

<br>

### Consequences

1. Decreases code readability due to added complexity.

   - Lot of classes are created.

1. Although there is flexibility to add new families, However there is no flexibilty to add new products as it breaks existing code.

   - Addition of new product means modification of the abstract base factory class `I_UIFactory`, in our case.

     - If we make the creation of new product as pure virtual function, then the already existing concrete factory class `LoginUIFactory`, in our case will break.
     - We cannot make the creation of the new product as empty virtual function because we need to write implementation to satisfy the return type and we cannot do that.

   ```cpp
   //say we created Ipopup and LogoutPopup
   class I_UIFactory {
   public:
       virtual ILabel* createLabel() = 0;
       virtual IButton* createButton() = 0;
       virtual IPopup* createPopUp(){} // We cannot provide implementation here as we cannot return the IPopup*.
   };
   ```
