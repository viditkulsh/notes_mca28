# Java — Question Bank

Theory questions and programs on polymorphism, the `this` / `super` / `final` / `static` keywords, casting, abstract classes, strings and wrapper classes, access modifiers, packages, interfaces, adapter classes and exception handling.

> Student-transcribed. Verify against the copy given in class before relying on it for an exam.

Structured answers to all of these: [Question_Bank_Ans.md](Question_Bank_Ans.md). Unit 1 (Fundamentals of Java) has its own bank: [JAVA_UNIT1_Question_Bank.md](JAVA_UNIT1_Question_Bank.md).

## Contents

- [Theory Questions](#theory-questions)
- [Programs](#programs)

---

## Theory Questions

1. Explain method overloading and method overriding in Java. Compare them based on definition, inheritance, parameters, return type, binding, and polymorphism with suitable examples.
2. Explain the `this`, `super`, and `final` keywords in Java. Discuss their different uses with suitable code examples and explain why a `final` method cannot be overridden.
3. Explain upcasting, downcasting, and dynamic method dispatch in Java. Describe how runtime polymorphism is achieved and discuss the possible risks of incorrect downcasting with examples.
4. Explain abstract classes and abstract methods in Java. Compare an abstract class with a normal class and discuss how subclasses implement abstract methods. Give a suitable real-world example.
5. Explain `String`, String array, String methods, `StringBuffer`, and wrapper classes in Java. Compare `String` and `StringBuffer` with respect to mutability and memory behavior, and explain the need for wrapper classes with suitable examples.
6. State the purpose of the keywords `this` and `super`.
7. State the purpose of the keywords `static` and `final`.
8. Explain the different access modifiers in Java: default, `public`, `private`, and `protected`.
9. What is a user-defined package in Java? Explain the steps for creating and importing a user-defined package.
10. Explain interfaces in Java. What are the advantages of using interfaces?
11. Differentiate between an abstract class and an interface in Java.
12. What is an adapter class? Explain its purpose and advantages with a suitable example.
13. Explain the different types of exceptions in Java with suitable examples.
14. Explain the purpose and difference between the `throw` and `throws` keywords in Java.
15. Explain the use of `try`, `catch`, and `finally` blocks in exception handling.
16. What are nested `try` blocks and multiple `catch` statements? Explain with suitable examples.
17. What are user-defined exceptions? Explain the procedure for creating and using a user-defined exception in Java.

## Programs

1. Create an interface `Manager` with a method `showDetails()`. Implement the interface in the `HRManager` class and call the method from the main class.
2. Create a `Product` class with `productId`, `productName`, `quantity`, and `price`. Accept 10 products and display the top two products according to highest price.
3. Create `Student` and `Marks` classes using inheritance. Calculate total Java marks using theory and practical marks and display the result.
4. Accept an email address and throw a user-defined `InvalidEmailException` if it starts with a digit or does not contain `@`.
5. Create a `Bank` class with customer name, account number, and balance. Implement constructors, deposit, and withdraw methods and display the updated balance.
6. Create a `Staff` class with name, birth-date, designation, and salary. Create five objects and display the name of the staff member having the highest salary.
7. Create an abstract `Order` class with subclasses `PurchaseOrder` and `SalesOrder`. Create five objects of each subclass and accept and display their details.
8. Implement a user-defined `InSufficientFundException` for a bank withdrawal and display the additional amount required when the balance is insufficient.
9. Create an abstract class `Shape` with an abstract method `area()`. Create `Circle`, `Rectangle`, and `Triangle` subclasses and demonstrate dynamic method dispatch.
10. Create a superclass `Employee` and subclasses `Manager` and `Developer`. Demonstrate method overriding, upcasting, downcasting, and the `super` keyword.
11. Create a user-defined package `mypackage` containing a `Student` class and import it into another class to display student details.
12. Create an interface `Vehicle` with methods `start()` and `stop()`. Implement it using a `Car` class.
13. Create two interfaces `Printable` and `Showable` and implement both interfaces in a single `Document` class.
14. Create an interface `StudentActivity` with multiple methods and use an adapter class to implement only the required method in the `Student` class.
15. Create a superclass `Employee` with `private`, `protected`, and `public` members. Create a subclass in another package and demonstrate which members can be accessed.
16. Write a Java program using `try`, `catch`, and `finally` to handle an arithmetic exception.
17. Write a Java program using multiple `catch` statements to handle different types of exceptions.
18. Write a Java program using nested `try` blocks to handle exceptions at different levels.
19. Write a Java program to create and use a user-defined `InvalidEmailException` when an invalid email address is entered.
20. Write a Java program to create an `InSufficientFundException` and throw it when the withdrawal amount is greater than the available balance.
