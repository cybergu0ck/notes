# Decorator pattern

The Decorator design pattern is a structural pattern that dynamically adds new behaviors to an object by wrapping it, without altering its original class or affecting other instances.

<br>
<br>
<br>

## Components

1. Component : Defines the common interface for both the basic objects and the decorators so they can be used interchangeably.

1. Concrete component : The original, basic class that provides the core functionality before any extra "decorations".

1. Base decorator : An abstract class that implements the "Component" interface and contains a reference to a wrapped "Component" object ([aggregation](../../object-oriented-programming/object-relationships.md#aggregation)).

1. Concrete decorator : The specific classes that override the component methods to add extra behaviours to the wrapped object.

<br>

- The component diagram is as follows:

<!-- TODO Add the drawio image here -->

<br>

- The component diagram showing a real world example is as follows:

<!-- TODO Add the drawio image here -->

<br>
<br>
<br>

## Implementation

<br>
<br>
<br>

## Applicability

<br>
<br>

### Avoid class explosion

- Class explosion is a software design anti-pattern where an excessive number of classes are created to handle every variation of an object, leading to complex, hard-to-maintain code.
  - This commmonly results from over-using inheritance.

- Use Decorator pattern to "flatten" the hierarchy into individual, stackable components.

* Illustration : There is no need to create "EncryptedFile", "CompressedFile" or "EncryptedCompressedFile" classes inheriting from `File` class. Behaviour can be stacked.

  ```cpp
  #include <iostream>
  #include <string>
  #include <memory>

  class IFile{
  public:
      virtual ~IFile() = default;
      virtual void writeData(std::string data) = 0;
      virtual std::string getFileName() = 0;
  };

  class File: public IFile{
  public:
      std::string filename;
      File(std::string name) : filename(name){}
      void writeData(std::string data) override {
          std::cout << "Writing " << data << " to " << filename << "\n";
      }
      std::string getFileName() override {
          return filename;
      }
  };

  class IFileDecorator: public IFile{
  protected:
      std::unique_ptr<IFile> wrapedFile;
  public:
      IFileDecorator(std::unique_ptr<IFile> object) : wrapedFile(std::move(object)){}
      std::string getFileName() override {
          return wrapedFile->getFileName();
      }
  };


  class EncryptionDecorator: public IFileDecorator{
  public:
      EncryptionDecorator(std::unique_ptr<IFile> object) : IFileDecorator(std::move(object)){};
      void writeData(std::string data) override {
          wrapedFile->writeData(data);
          std::cout << "Encrypting " << wrapedFile->getFileName() << "\n";
      }
  };

  class CompressionDecorator : public IFileDecorator
  {
  public:
      CompressionDecorator(std::unique_ptr<IFile> object) : IFileDecorator(std::move(object)){}
      void writeData(std::string data) override {
          wrapedFile->writeData(data);
          std::cout << "Compressing " << wrapedFile->getFileName() << "\n";
      }
  };

  int main() {
      std::unique_ptr<IFile> myFile = std::make_unique<File>("password.txt");
      myFile = std::make_unique<EncryptionDecorator>(std::move(myFile));
      myFile = std::make_unique<CompressionDecorator>(std::move(myFile));
      myFile->writeData("super secret password");
      return 0;
  }

  //Writing super secret password to password.txt
  //Encrypting password.txt
  //Compressing password.txt
  ```

- Object Specific requirement : Use this when a specific objects needs special behaviour out of lot of instances.
  - A game object who picks up a "Power Shield" needs the `ShieldDecorator`. Every other player remains a `BasicPlayer`.

* Temporary behaviour : When an object needs a feature for a short time and then needs to go back to being "plain".
  - This is done by wrapping it for the process and then discard the decorator when the process finishes.
  - Examples :
    - An object needs to "searchable", "syncable" only during a specific background process.
    - A game object equips a momentary boost and becomes "Indestructable" only for a short duration.

<br>
<br>
<br>

## Advantages

<br>
<br>
<br>

## Disadvantages
