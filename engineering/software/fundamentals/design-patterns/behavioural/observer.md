# Observer Design Pattern

_Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically._

- Also known as dependants, Publish-Subscribe.

<br>

### Components

1. **Subject** is the object being observed. It maintains a list of observers and notifies them of state changes.
1. **Observers** are the objects that listen for updates from the subject. When the subject changes, observers are notified and updated accordingly.
   - There can be any number of observers.

<br>

### Applicability

1. When an abstraction has two aspects, one dependent on the other.
1. Change in one object needs to trigger change in unknown number of objects.
1. Notifying changes to different objects without tight coupling.

<br>

### Benefits

1. Vary the subjects and observers independently, facilitates the addition of observers without modifing the subject or other observers.
1. Abstract coupling between subject and observer. The subject doesn't know about the concrete classes of any observer, hence abstract coupling (loosely coupled).
1. Support for broadcast communication.

<br>

### Consequences

1. Unexpected updates.Observers have no knowledge of each other, hence they are blind to the cost of changing the subject (if they do).

<br>
<br>

## Illustration
