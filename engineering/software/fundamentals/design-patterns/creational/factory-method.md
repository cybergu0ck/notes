# Factory Method

<br>
<br>

## Theory

Factory method is a creational pattern that defines an interface for creating an object, but hands over the responsibility of instantiation to one of the subclasses.

<br>

![img](./_assets/)

<br>

### Components

1. Product : The component created by the factory.

   - Implemented via an interface.

1. Factory : The component that creates a family of related products.

   - Implemented via an interface.
   - Concrete factorties "make" products for the specific family it represents.

1. Client : client is uses with the factory. The relationship could be [association](../../object-oriented-programming/object-relationships.md#association), [aggregation](../../object-oriented-programming/object-relationships.md#aggregation) or [composition](../../object-oriented-programming/object-relationships.md#composition).

<br>

### Applicability

2. This pattern is helpful in usecases where client is independent of how its products are created, composed, and represented.

<br>

### Advantages

1. Abstraction of implementation of products.

1. Adheres to [open-close principle](../../object-oriented-programming/principles.md#open-close-principle) in the context of addition of a new family, containing the same kind and number of products.

<br>

### Disadvantages

<br>
<br>

## Application

![img](./_assets)

<br>

```cpp
#include<iostream>
#include <memory>

//interface of product
class IDocument{
public:
    virtual ~IDocument() = default;
    virtual void open() = 0;
    virtual void save() = 0;

};


//concrete product
class PDFDocument : public IDocument{
public:
    ~PDFDocument(){}
    void open() override{
        std::cout << "opening pdf document" << '\n';
    }
    void save() override{
        std::cout << "saving pdf document" << '\n';
    }
};


//interface of factory
class IDocumentFactory{
public:
    virtual ~IDocumentFactory() = default;
    virtual std::shared_ptr<IDocument> make_document() = 0;
};


//concrete factory
class PDFDocumentFactory : public IDocumentFactory{
public:
    ~PDFDocumentFactory(){}
    std::shared_ptr<IDocument> make_document() override{
        return std::make_shared<PDFDocument>();
    }
};


//client
int main(){
    std::unique_ptr<IDocumentFactory> factory = std::make_unique<PDFDocumentFactory>();
    std::shared_ptr<IDocument> doc = factory->make_document();
    doc->open();
    doc->save();
}

//opening pdf document
//saving pdf document
```

<br>

### Components

1. Product : The component created by the factory.

   - Implemented via an interface.

1. Factory : The component that creates a family of related products.

   - Implemented via an interface.
   - Concrete factorties "make" products for the specific family it represents.

1. Client : client is uses with the factory. The relationship could be [association](../../object-oriented-programming/object-relationships.md#association), [aggregation](../../object-oriented-programming/object-relationships.md#aggregation) or [composition](../../object-oriented-programming/object-relationships.md#composition).

<br>

### Applicability

2. This pattern is helpful in usecases where client is independent of how its products are created, composed, and represented.

<br>

### Advantages

1. Abstraction of implementation of products.

1. Adheres to [open-close principle](../../object-oriented-programming/principles.md#open-close-principle) in the context of addition of a new family, containing the same kind and number of products.

<br>

### Disadvantages

<br>
<br>
