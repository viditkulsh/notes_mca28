# Java — Theory Notes

Concept notes from Java theory lectures. Each entry keeps the definition as given in class, with a short example added where it makes the idea concrete.

## Contents

- [20 Aug 2026 — OOP Fundamentals](#20-aug-2026--oop-fundamentals)
  - [What is a class?](#what-is-a-class)
  - [What is abstraction?](#what-is-abstraction)
  - [What is encapsulation?](#what-is-encapsulation)
  - [What is polymorphism?](#what-is-polymorphism)
  - [What is inheritance?](#what-is-inheritance)
  - [What is a function?](#what-is-a-function)
- [Quick Reference](#quick-reference)

---

## 20 Aug 2026 — OOP Fundamentals

### What is a class?

A class is a blueprint or template for creating objects in object-oriented programming. It defines the properties (attributes) and behaviours (methods) that the objects created from the class will have. A class encapsulates data for the object and the methods to manipulate that data, allowing for modular and reusable code.

```java
class Student {
    String name;   // attribute
    int marks;     // attribute

    void display() {              // behaviour
        System.out.println(name + ": " + marks);
    }
}
```

### What is abstraction?

Abstraction is a fundamental concept in object-oriented programming (OOP) that focuses on hiding the complex implementation details of a system and exposing only the essential features or functionalities to the user. It allows developers to create simplified models of real-world entities, making it easier to manage complexity and improve code maintainability.

In Java, abstraction is achieved through **abstract classes** and **interfaces**, which let you declare methods without providing their complete implementation. Subclasses, or classes that implement the interface, supply that implementation.

### What is encapsulation?

Encapsulation is a core principle of OOP that involves bundling the data (attributes) and the methods (functions) that operate on that data into a single unit called a class. It achieves data hiding and protects the internal state of an object from being accessed or modified directly from outside the class.

In practice this means keeping fields `private` and exposing them through public getters and setters.

### What is polymorphism?

Polymorphism is a fundamental concept in OOP that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). This gives code flexibility and extensibility, as the same method name can behave differently depending on the object that invokes it.

Two forms:

| Form | Achieved by | Resolved at |
| --- | --- | --- |
| Compile-time polymorphism | Method overloading | Compile time |
| Runtime polymorphism | Method overriding | Runtime |

### What is inheritance?

Inheritance is a key feature of OOP that allows a new class (subclass or derived class) to inherit properties and behaviours (attributes and methods) from an existing class (superclass or base class). This promotes code reusability, as the subclass can use the existing functionality of the superclass while also adding its own features or overriding existing ones.

Inheritance establishes an **"is-a"** relationship between classes, enabling hierarchical classification and organisation of code.

### What is a function?

A function is a block of code that performs a specific task or operation and can be called or invoked from other parts of a program. Functions break complex problems into smaller, manageable pieces, promoting code reusability and modularity.

In languages like Java, functions are referred to as **methods** when they are defined within a class — which, in Java, is always.

---

## Quick Reference

| Term | Meaning |
| --- | --- |
| Function | Same thing as a method in Java |
| Method | A function defined inside a class |
| Primitive type | Pre-defined by the language — `int`, `char`, `boolean`, `double`, `float`, `long`, `short`, `byte` |
| Non-primitive type | User-defined or library types — classes, interfaces, arrays, `String` |

## Related code

- [arrays/Array.java](arrays/Array.java) — declaring, assigning, and iterating over arrays
- [arrays/ArrayDemo.java](arrays/ArrayDemo.java) — using a class from another package
- [loops/Loop.java](loops/Loop.java) — `for`, `while`, and `do-while` loops
- [util/Stats.java](util/Stats.java) — `public` access across packages
