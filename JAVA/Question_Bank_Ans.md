# Java — Answers to Question Bank

Structured, exam-oriented answers to every item in [Question_Bank.md](Question_Bank.md) (Unit 1 — Fundamentals of Java). Numbering matches the question bank exactly: **A1** answers question 1 of section A, **B7** answers question 7 of section B, **C3** answers question 3 of section C, and **P3** answers practical exercise 3.

Depth follows the marks. Section A answers are one to three sentences, section B answers are ~5-mark notes, and section C answers are full 8–10-mark answers in the shape **Definition → Explanation / Diagram → Program → Advantages & limitations → Summary**, sized to be written out in 12–15 minutes. Every complete program was compiled and run on JDK 25, and every **Sample output** block is the real output of that run. Apart from the one snippet marked *Java 14+*, all code also compiles with `javac --release 8`, so it works on older lab JDKs too.

> Student-written notes. The question bank is itself student-transcribed, so check each question against the copy given in class, and cross-check definitions with the class notes in [src/theory/notes.md](src/theory/notes.md) and the prescribed textbook before the exam.

## Contents

- [Unit 1 — Fundamentals of Java](#unit-1--fundamentals-of-java)
  - [A. Very Short Answer Questions](#a-very-short-answer-questions) (A1–A15)
  - [B. Short Answer Questions](#b-short-answer-questions)
    - [B1. Relationship between class and object](#b1-relationship-between-class-and-object)
    - [B2. Abstraction with an example](#b2-abstraction-with-an-example)
    - [B3. Encapsulation in Java](#b3-encapsulation-in-java)
    - [B4. Advantages of inheritance](#b4-advantages-of-inheritance)
    - [B5. Compile-time vs runtime polymorphism](#b5-compile-time-vs-runtime-polymorphism)
    - [B6. Rules for naming identifiers](#b6-rules-for-naming-identifiers)
    - [B7. Primitive data types](#b7-primitive-data-types)
    - [B8. Coding conventions and why they matter](#b8-coding-conventions-and-why-they-matter)
    - [B9. Arithmetic, relational and logical expressions](#b9-arithmetic-relational-and-logical-expressions)
    - [B10. Decision-making statements](#b10-decision-making-statements)
    - [B11. Arrays with an example](#b11-arrays-with-an-example)
    - [B12. Common methods of the Arrays class](#b12-common-methods-of-the-arrays-class)
    - [B13. Garbage collection](#b13-garbage-collection)
    - [B14. Why `System.gc()` does not guarantee collection](#b14-why-systemgc-does-not-guarantee-collection)
    - [B15. Current status of `finalize()`](#b15-current-status-of-finalize)
  - [C. Long Answer / Theory Questions](#c-long-answer--theory-questions)
    - [C1. Fundamental OOP concepts in Java](#c1-fundamental-oop-concepts-in-java)
    - [C2. Classes, objects, object creation and member access](#c2-classes-objects-object-creation-and-member-access)
    - [C3. Abstraction using an abstract class](#c3-abstraction-using-an-abstract-class)
    - [C4. Encapsulation and data hiding](#c4-encapsulation-and-data-hiding)
    - [C5. Inheritance and its types](#c5-inheritance-and-its-types)
    - [C6. Compile-time and runtime polymorphism](#c6-compile-time-and-runtime-polymorphism)
    - [C7. Identifiers, keywords and naming rules](#c7-identifiers-keywords-and-naming-rules)
    - [C8. Primitive and non-primitive data types](#c8-primitive-and-non-primitive-data-types)
    - [C9. Naming and formatting conventions](#c9-naming-and-formatting-conventions)
    - [C10. Expressions and operators](#c10-expressions-and-operators)
    - [C11. Decision-making statements with examples](#c11-decision-making-statements-with-examples)
    - [C12. Arrays and the Arrays class](#c12-arrays-and-the-arrays-class)
    - [C13. Garbage collection and automatic memory management](#c13-garbage-collection-and-automatic-memory-management)
    - [C14. `finalize()` and why it is not recommended](#c14-finalize-and-why-it-is-not-recommended)
  - [Multiple Choice Questions](#multiple-choice-questions)
  - [Practical Programming Exercises](#practical-programming-exercises)
    - [P1. Class and object with details](#p1-class-and-object-with-details)
    - [P2. Encapsulation with getters and setters](#p2-encapsulation-with-getters-and-setters)
    - [P3. Inheritance using `extends`](#p3-inheritance-using-extends)
    - [P4. Method overloading](#p4-method-overloading)
    - [P5. Method overriding](#p5-method-overriding)
    - [P6. Positive, negative or zero](#p6-positive-negative-or-zero)
    - [P7. Largest of three numbers](#p7-largest-of-three-numbers)
    - [P8. Grade using an else-if ladder](#p8-grade-using-an-else-if-ladder)
    - [P9. Menu using `switch`](#p9-menu-using-switch)
    - [P10. Store and display five integers](#p10-store-and-display-five-integers)
    - [P11. Largest element in an array](#p11-largest-element-in-an-array)
    - [P12. Sum and average of array elements](#p12-sum-and-average-of-array-elements)
    - [P13. Sorting with `Arrays.sort()`](#p13-sorting-with-arrayssort)
    - [P14. Comparing arrays with `Arrays.equals()`](#p14-comparing-arrays-with-arraysequals)
    - [P15. Object eligible for garbage collection](#p15-object-eligible-for-garbage-collection)
- [Quick revision sheet](#quick-revision-sheet)

---

## Unit 1 — Fundamentals of Java

### A. Very Short Answer Questions

**A1. What is Java?**

Java is a high-level, class-based, object-oriented programming language developed by James Gosling's team at Sun Microsystems (released in 1995, now owned by Oracle). Source code is compiled by `javac` into platform-independent **bytecode** (`.class` files) that runs on any **Java Virtual Machine (JVM)** — "Write Once, Run Anywhere".

**A2. What is a class?**

A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviours (methods) that every object created from it will have, bundling the data with the methods that manipulate it — e.g. `class Student { String name; void display() { … } }`.

**A3. What is an object?**

An object is an instance of a class, created at runtime with the `new` keyword (`Student s = new Student();`). It occupies memory on the heap and has **state** (its field values), **behaviour** (its methods) and **identity** (its own reference).

**A4. What is abstraction?**

Abstraction is hiding the complex implementation details of a system and exposing only its essential features to the user — showing *what* an object does, not *how*. In Java it is achieved through **abstract classes** and **interfaces**.

**A5. What is encapsulation?**

Encapsulation is bundling data (fields) and the methods that operate on that data into a single unit, the class, while protecting the internal state from direct outside access (data hiding). In practice: `private` fields exposed through `public` getters and setters.

**A6. What is inheritance?**

Inheritance is the mechanism by which a new class (subclass) acquires the attributes and methods of an existing class (superclass) using the `extends` keyword. It promotes code reuse and models an **"is-a"** relationship (e.g. `Car extends Vehicle`).

**A7. What is polymorphism?**

Polymorphism ("many forms") lets objects of different classes be treated as objects of a common superclass, so the same method name behaves differently depending on the object that invokes it. Java has **compile-time** polymorphism (method overloading) and **runtime** polymorphism (method overriding).

**A8. What is an identifier?**

An identifier is a name the programmer gives to a class, variable, method, package or other program element — e.g. `Student`, `totalMarks`, `calculateGrade`. It must follow Java's naming rules (see [B6](#b6-rules-for-naming-identifiers)).

**A9. What is a keyword?**

A keyword is a reserved word with a predefined meaning to the compiler, so it cannot be used as an identifier — e.g. `class`, `public`, `static`, `int`, `if`, `new`. All Java keywords are lowercase; `goto` and `const` are reserved but unused.

**A10. What is a data type?**

A data type specifies what kind of value a variable can hold, how much memory it takes and which operations are allowed on it. Java has 8 **primitive** types (`byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean`) and **non-primitive (reference)** types such as classes, interfaces, arrays and `String`.

**A11. What is an expression?**

An expression is a combination of operands (variables, literals, method calls) and operators that evaluates to a single value — e.g. `a + b * 2`, `marks >= 40`, `age > 18 && hasId`.

**A12. What is an array?**

An array is a fixed-size container object that stores multiple values of the **same type** under one name, accessed by an index starting at **0**; its size is given by the `length` field — e.g. `int[] marks = {78, 85, 91};`.

**A13. What is garbage collection?**

Garbage collection is the JVM's automatic memory management: the garbage collector finds heap objects that are no longer reachable through any reference and reclaims their memory, so Java has no `delete` or `free()`. See [C13](#c13-garbage-collection-and-automatic-memory-management) for the full answer.

**A14. What is the purpose of `System.gc()`?**

`System.gc()` **requests** the JVM to run the garbage collector; it is equivalent to `Runtime.getRuntime().gc()`. It is only a hint — the JVM may delay or ignore it, so a collection is not guaranteed.

**A15. What is `finalize()`?**

`finalize()` is a `protected` method of `java.lang.Object` that the garbage collector could call before reclaiming an object, historically used for cleanup. It is **deprecated** (since Java 9, and *for removal* since Java 18 by JEP 421) because it may never run; use try-with-resources or `java.lang.ref.Cleaner` instead.

---

### B. Short Answer Questions

Each answer is sized for about 5 marks.

### B1. Relationship between class and object

A **class** is a blueprint; an **object** is a concrete instance built from it — *an object is an instance of a class*.

- One class can produce **many objects**. Each object gets its own copy of the instance variables (its *state*) but shares the methods (the *behaviour*) defined in the class.
- A class is a **logical** entity — declaring it allocates no memory for fields. An object is a **physical** entity — heap memory is allocated each time `new` runs.
- The class fixes *what* every object has and can do; the object holds the actual values.

Analogy: a house plan (class) and the houses built from it (objects).

```java
class Car {                     // one class (blueprint)
    String model;               // each object gets its own copy
    void drive() {
        System.out.println(model + " is moving");
    }
}
```

```java
Car c1 = new Car();             // object 1
c1.model = "Charger";
Car c2 = new Car();             // object 2: same class, different state
c2.model = "Mustang";
c1.drive();                     // Charger is moving
c2.drive();                     // Mustang is moving
```

| Basis | Class | Object |
|---|---|---|
| Nature | Blueprint / template (logical) | Instance of the class (physical) |
| Memory | No memory for fields when declared | Heap memory allocated when created |
| Created with | `class` keyword, once | `new` keyword, any number of times |
| Contains | Field and method declarations | Actual field values (state) |
| Example | `class Car` | `new Car()` |

**Summary:** A class defines structure and behaviour once; objects are its runtime instances, each with its own state.

---

### B2. Abstraction with an example

**Abstraction** means hiding the complex implementation details and exposing only the essential features — the user knows *what* an object does, not *how* it does it.

**Real-world example:** a TV remote. You press *Power* or *Channel +*; the circuitry, signals and decoding stay hidden. Likewise, a driver uses the steering, accelerator and brake without knowing how the engine burns fuel.

**In Java**, abstraction is achieved with:

1. **Abstract classes** — may contain abstract methods (no body) and concrete methods; partial abstraction (0–100%). See [C3](#c3-abstraction-using-an-abstract-class).
2. **Interfaces** — declare *what* must be done; implementing classes supply *how* (fully abstract before Java 8; may now also hold `default` and `static` methods).

```java
interface Remote {                        // WHAT: only the essential operations
    void powerOn();
    void changeChannel(int channel);
}
class SmartTv implements Remote {         // HOW: hidden inside the implementing class
    public void powerOn() { System.out.println("Booting OS, starting display"); }
    public void changeChannel(int ch) { System.out.println("Tuning to channel " + ch); }
}
```

```java
Remote r = new SmartTv();                 // the user sees only Remote's operations
r.powerOn();                              // Booting OS, starting display
r.changeChannel(5);                       // Tuning to channel 5
```

**Benefits:** less complexity for the user, implementation can change without affecting callers, a common contract for all implementations, loose coupling.

**Summary:** Abstraction separates *what* from *how*; Java implements it with abstract classes and interfaces.

---

### B3. Encapsulation in Java

**Encapsulation** is bundling the data (fields) and the methods that operate on it into one unit — the class — and protecting the internal state from direct access from outside (**data hiding**).

**How to achieve it**

1. Declare the fields `private`.
2. Provide `public` getter methods to read them and setter methods to modify them.
3. Put validation inside the setters so invalid data never reaches the fields.

```java
class Account {
    private double balance;                          // hidden from other classes
    public double getBalance() { return balance; }   // getter: read access
    public void deposit(double amount) {             // controlled write access
        if (amount > 0) {                            // validation protects the data
            balance += amount;
        }
    }
}
```

Outside code cannot write `acc.balance = -500;` — the compiler rejects it with *balance has private access in Account*.

**Benefits**

- **Data protection and integrity** — values change only through validated methods.
- **Control** — a field can be made read-only (getter only) or write-only (setter only).
- **Flexibility** — the internal representation can change without affecting code that uses the class.
- **Maintainability** — each class is a self-contained, independently testable unit.

**Summary:** Encapsulation = data + methods in one class, with `private` fields reachable only through controlled `public` methods.

---

### B4. Advantages of inheritance

Inheritance lets a subclass acquire the fields and methods of a superclass with `extends`.

1. **Code reusability** — common code is written once in the superclass and reused by every subclass.
2. **Less duplication, easier maintenance** — a fix in the superclass automatically reaches all subclasses.
3. **Extensibility** — new features are added in a subclass without modifying (and re-testing) the existing superclass.
4. **Method overriding → runtime polymorphism** — a subclass can redefine inherited behaviour, and a superclass reference calls the right version at runtime.
5. **Logical hierarchy** — "is-a" relationships (`Student` *is a* `Person`) model the real world and make code easier to understand.
6. **Faster development** — build on tested classes; every class already inherits `toString()`, `equals()` and `hashCode()` from `Object`.

```java
class Person {                                     // common code written once
    String name;
    void introduce() {
        System.out.println("I am " + name);
    }
}
class Student extends Person { int rollNo; }       // gets name + introduce() for free
class Teacher extends Person { String subject; }   // reused again, no duplication
```

**Limitation to mention:** subclass and superclass are tightly coupled, and a Java class can extend only one class (multiple inheritance only through interfaces).

**Summary:** Inheritance gives reuse, extensibility and polymorphism with less duplicated code.

---

### B5. Compile-time vs runtime polymorphism

| Basis | Compile-time polymorphism | Runtime polymorphism |
|---|---|---|
| Also called | Static binding, early binding | Dynamic binding, late binding, dynamic method dispatch |
| Achieved by | **Method overloading** | **Method overriding** |
| Method signature | Same name, **different parameter list** (number, type or order) | Same name **and same parameter list** |
| Inheritance needed | No (usually within one class) | Yes (subclass overrides a superclass method) |
| Decided by | Compiler, from the argument types | JVM, from the actual object type |
| Return type | May differ (but cannot be the *only* difference) | Same, or a subtype (covariant) |
| Cost | Nothing to look up at runtime | Method looked up at runtime (small overhead) |
| Example | `add(int, int)` / `add(double, double)` | `Animal a = new Dog(); a.sound();` |

```java
class Calc {                                          // compile-time: overloading
    int add(int a, int b)          { return a + b; }
    double add(double a, double b) { return a + b; }
}
class Animal { void sound() { System.out.println("Some sound"); } }
class Dog extends Animal {                            // runtime: overriding
    @Override void sound() { System.out.println("Bark"); }
}
```

```java
Calc c = new Calc();
System.out.println(c.add(2, 3));         // 5    : compiler picks add(int, int)
System.out.println(c.add(2.5, 3.5));     // 6.0  : compiler picks add(double, double)
Animal a = new Dog();                    // superclass reference, subclass object
a.sound();                               // Bark : JVM picks Dog's sound() at runtime
```

**Summary:** Overloading is resolved by the compiler from the arguments; overriding is resolved by the JVM from the actual object.

---

### B6. Rules for naming identifiers

**Rules (enforced by the compiler)**

1. Allowed characters: letters (`A–Z`, `a–z`), digits (`0–9`), underscore `_` and dollar sign `$` (any Unicode letter also counts as a letter).
2. Must **not start with a digit** — `marks1` is valid, `1marks` is not.
3. Must not be a **keyword** (`class`, `int`, `goto`, …) or one of the literals **`true`, `false`, `null`**.
4. **No spaces or other symbols** (`-`, `#`, `@`, `%`, `.`, …).
5. **Case-sensitive** — `marks`, `Marks` and `MARKS` are three different names.
6. **No length limit**.
7. A single underscore `_` cannot be used as a name since Java 9 — it is a keyword (Java 22+ uses it only to mark unnamed variables).

| Identifier | Valid? | Reason |
|---|---|---|
| `studentName` | Yes | letters only, camelCase |
| `marks2`, `_count`, `$price` | Yes | digit not first; `_` and `$` allowed |
| `MAX_MARKS` | Yes | letters and underscore |
| `2marks` | No | starts with a digit |
| `student name` | No | contains a space |
| `total-marks` | No | `-` is not allowed |
| `class` | No | keyword |
| `true` | No | reserved literal |
| `_` | No | keyword since Java 9 |

**Conventions** (not rules, but expected): classes in `PascalCase`, variables and methods in `camelCase`, constants in `UPPER_SNAKE_CASE` (see [B8](#b8-coding-conventions-and-why-they-matter)). Contextual words such as `var`, `record` and `yield` are still legal variable names.

**Summary:** Letters, digits, `_` and `$` only; no leading digit, no keyword or literal, no spaces; case-sensitive.

---

### B7. Primitive data types

Java has **8 primitive types** in four families. Their sizes are the same on every platform, which is part of Java's platform independence.

| Type | Size | Range | Default* | Example |
|---|---|---|---|---|
| `byte` | 8-bit | −128 to 127 | `0` | `byte b = 100;` |
| `short` | 16-bit | −32,768 to 32,767 | `0` | `short s = 30000;` |
| `int` | 32-bit | −2³¹ to 2³¹−1 (about ±2.1 billion) | `0` | `int n = 150000;` |
| `long` | 64-bit | −2⁶³ to 2⁶³−1 | `0L` | `long l = 9000000000L;` |
| `float` | 32-bit | about ±3.4 × 10³⁸, 6–7 significant digits | `0.0f` | `float f = 3.14f;` |
| `double` | 64-bit | about ±1.8 × 10³⁰⁸, 15–16 significant digits | `0.0d` | `double d = 3.14159;` |
| `char` | 16-bit, unsigned | `'\u0000'` to `'\uffff'` (0 to 65,535) | `'\u0000'` | `char c = 'A';` |
| `boolean` | JVM-dependent | `true` or `false` | `false` | `boolean ok = true;` |

\* Defaults apply to fields and array elements. **Local variables get no default** — reading one before assigning it is a compile error (*variable n might not have been initialized*).

- **Families:** integer (`byte`, `short`, `int`, `long`), floating-point (`float`, `double`), character (`char`), boolean (`boolean`).
- **Literal suffixes:** whole-number literals are `int` by default, so a larger value needs `L`; decimal literals are `double` by default, so a `float` needs `f`.
- **`char` is 16-bit** because Java uses Unicode (a UTF-16 code unit), not 8-bit ASCII.
- Each primitive has a **wrapper class** (`Byte`, `Short`, `Integer`, `Long`, `Float`, `Double`, `Character`, `Boolean`); conversion between the two is automatic (autoboxing / unboxing).

```java
long bigNumber = 9_000_000_000L;   // L: whole-number literals are int by default
float pi = 3.14f;                  // f: decimal literals are double by default
// float bad = 3.14;               // error: possible lossy conversion from double to float
char grade = 'A';                  // single quotes; one 16-bit Unicode character
boolean passed = true;             // only true or false (not 1 or 0)
```

**Summary:** 8 primitives with fixed sizes — byte 1, short 2, int 4, long 8, float 4, double 8, char 2 bytes, boolean JVM-dependent.

---

### B8. Coding conventions and why they matter

**Coding conventions** are agreed guidelines — not compiler rules — for naming, formatting, commenting and organising code, so that a whole code base reads as if one person wrote it. Java's are based on Sun's (now Oracle's) *Code Conventions for the Java Programming Language*; many teams also follow the Google Java Style Guide.

| Element | Convention | Example |
|---|---|---|
| Class, interface | `PascalCase`, nouns | `Student`, `BankAccount`, `Runnable` |
| Method | `camelCase`, verbs | `calculateTotal()`, `getName()` |
| Variable | `camelCase`, meaningful | `totalMarks`, `rollNo` |
| Constant | `UPPER_SNAKE_CASE` (`static final`) | `MAX_SIZE`, `PI` |
| Package | all lowercase, reverse domain | `com.mitwpu.mca`, `java.util` |
| Boolean variable / method | `is`, `has`, `can` prefix | `isValid`, `hasNext()` |

**Formatting:** 4-space indentation, one statement per line, opening brace at the end of the line, braces even around one-line `if` bodies, spaces around operators, a blank line between methods, lines kept under about 80–100 characters, Javadoc (`/** … */`) on public classes and methods.

**Why they are important**

1. **Readability** — code is read far more often than it is written; good names reveal intent (`calculateGrade()` vs `cg()`).
2. **Maintainability** — Sun's conventions document notes that about 80% of the lifetime cost of software goes to maintenance, and hardly any software is maintained by its original author.
3. **Teamwork** — everyone can read and review everyone else's code.
4. **Fewer bugs** — e.g. always using braces avoids the classic "second line is not inside the `if`" mistake; `UPPER_CASE` makes constants obvious.
5. **Tool support and professionalism** — IDE formatters and tools such as Checkstyle apply or check conventions automatically.

**Summary:** Conventions are voluntary naming and layout rules that make Java code readable, maintainable and team-friendly.

---

### B9. Arithmetic, relational and logical expressions

| Type | Operators | Operands → result | Example (`a = 7`, `b = 2`) |
|---|---|---|---|
| Arithmetic | `+ - * / %` | numbers → number | `a / b` → `3`, `a % b` → `1` |
| Relational | `== != > < >= <=` | two values → `boolean` | `a > b` → `true` |
| Logical | `&& \|\| !` | `boolean` → `boolean` | `a > 5 && b > 5` → `false` |

- **Arithmetic expressions** compute numeric values. Integer division truncates (`7 / 2` is `3`, but `7.0 / 2` is `3.5`), and `%` gives the remainder. Integer division by zero throws `ArithmeticException`.
- **Relational expressions** compare two values and always produce `true` or `false`; they are the conditions of `if` statements and loops.
- **Logical expressions** combine conditions: `&&` (AND — true only if both are true), `||` (OR — true if at least one is true), `!` (NOT). `&&` and `||` **short-circuit**: the right side is skipped when the left side already decides the result.
- **Precedence:** arithmetic, then relational, then `&&`, then `||` — so `marks + bonus >= 40 && attendance >= 75` needs no brackets.

```java
int a = 7, b = 2;
System.out.println(a / b);              // 3     (integer division)
System.out.println(a % b);              // 1     (remainder)
System.out.println(7.0 / 2);            // 3.5
System.out.println(a > b);              // true
System.out.println(a > 5 && b > 5);     // false (b > 5 is false)
System.out.println(a > 5 || b > 5);     // true
System.out.println(!(a == b));          // true
```

**Summary:** Arithmetic expressions give numbers, relational expressions compare values and give booleans, and logical expressions combine booleans.

---

### B10. Decision-making statements

Decision-making (selection) statements choose which block of code runs, based on a condition.

| Statement | Use it when | Shape |
|---|---|---|
| `if` | a block should run only when a condition is true | `if (cond) { … }` |
| `if-else` | choosing between two alternatives | `if (cond) { … } else { … }` |
| `else-if` ladder | choosing one of many conditions, tested top to bottom | `if (c1) { … } else if (c2) { … } else { … }` |
| Nested `if` | a condition depends on an earlier one | `if (c1) { if (c2) { … } }` |
| `switch` | comparing one value against many fixed constants | `switch (x) { case 1: … break; default: … }` |
| Ternary `?:` | picking one of two values in one expression | `max = (a > b) ? a : b;` |

**`switch` rules:** the expression can be `byte`, `short`, `char`, `int`, their wrapper classes, `String` (Java 7+) or an `enum` — not `long`, `float`, `double` or `boolean` (Java 21+ also allows type patterns). Case labels must be unique constants; without `break`, execution *falls through* into the next case; `default` handles everything else. Since **Java 14** the arrow form `case 1 -> …` has no fall-through, and `switch` can also be an expression that returns a value.

```java
int day = 3;
switch (day) {
    case 1:  System.out.println("Monday");    break;
    case 2:  System.out.println("Tuesday");   break;
    case 3:  System.out.println("Wednesday"); break;   // printed
    default: System.out.println("Another day");
}
String type = (day >= 6) ? "Weekend" : "Weekday";      // ternary: "Weekday"
```

**Summary:** `if`, `if-else`, the `else-if` ladder, nested `if`, `switch` and the ternary operator — use the `if` family for conditions and ranges, `switch` for one value against fixed constants.

---

### B11. Arrays with an example

An **array** is a fixed-size object that stores many values of the **same type** under one name; each element is reached by an **index from 0 to `length - 1`**.

- **Declare:** `int[] marks;` (preferred) or `int marks[];`
- **Create:** `marks = new int[5];` — the size is fixed at creation; elements get default values (`0`, `0.0`, `false`, `'\u0000'` or `null`).
- **Initialise:** `int[] marks = {78, 85, 91, 66, 72};` or element by element, `marks[0] = 78;`
- **Size:** `marks.length` — a field, not a method.
- **Bounds check:** an index outside `0 … length - 1` throws `ArrayIndexOutOfBoundsException` at runtime.
- **Multi-dimensional:** `int[][] matrix = new int[3][4];` is an array of arrays.

```java
int[] marks = {78, 85, 91, 66, 72};      // declare + create + initialise
System.out.println(marks.length);        // 5
System.out.println(marks[0]);            // 78 (first element)
marks[4] = 80;                           // update the last element
int total = 0;
for (int m : marks) {                    // traverse with for-each
    total += m;
}
System.out.println(total);               // 400
```

**Advantages:** fast access by index, one name for many values, easy traversal with loops. **Limitations:** fixed size (use `ArrayList` when the size changes), one element type only, inserting or deleting in the middle means shifting elements.

**Summary:** An array is a fixed-length, zero-indexed, same-type collection whose size is `array.length`.

---

### B12. Common methods of the Arrays class

`java.util.Arrays` is a utility class of **static** methods for arrays (`import java.util.Arrays;`). The examples start from `int[] a = {42, 7, 19, 73, 5};`; rows after `sort` use the sorted array `[5, 7, 19, 42, 73]`.

| Method | What it does | Example | Result |
|---|---|---|---|
| `toString(arr)` | Readable string of the elements | `Arrays.toString(a)` | `[42, 7, 19, 73, 5]` |
| `sort(arr)` | Sorts in ascending order, in place | `Arrays.sort(a)` | `a` becomes `[5, 7, 19, 42, 73]` |
| `binarySearch(arr, key)` | Index of `key`; **array must be sorted first** | `Arrays.binarySearch(a, 19)` | `2` |
| `equals(a1, a2)` | `true` if same length and same elements in the same order | `Arrays.equals(new int[]{1, 2}, new int[]{1, 2})` | `true` |
| `fill(arr, val)` | Sets every element to `val` | `Arrays.fill(b, 9)` on an `int[4]` | `[9, 9, 9, 9]` |
| `copyOf(arr, len)` | New array of `len` elements (truncated or padded with defaults) | `Arrays.copyOf(a, 3)` | `[5, 7, 19]` |
| `copyOfRange(arr, from, to)` | Copy of indexes `from` to `to - 1` | `Arrays.copyOfRange(a, 1, 4)` | `[7, 19, 42]` |
| `asList(...)` | Fixed-size `List` view of objects | `Arrays.asList("JAVA", "RM")` | `[JAVA, RM]` |
| `deepToString(arr)` | Readable string of a multi-dimensional array | `Arrays.deepToString(new int[][]{{1, 2}, {3, 4}})` | `[[1, 2], [3, 4]]` |

- `binarySearch` returns `-(insertion point) - 1` for a missing key: searching for `20` above gives `-4`.
- `a1 == a2` and `a1.equals(a2)` compare **references**, not contents — use `Arrays.equals` (or `Arrays.deepEquals` for 2-D arrays).
- `Arrays.toString` on a 2-D array prints row addresses such as `[[I@…` — use `deepToString`.
- `sort` uses a Dual-Pivot Quicksort for primitives and a stable merge sort (TimSort) for objects; `sort(arr, from, to)` sorts part of an array.

**Summary:** `toString`, `sort`, `binarySearch`, `equals`, `fill`, `copyOf`, `copyOfRange`, `asList` and `deepToString` cover printing, sorting, searching, comparing, filling and copying arrays.

---

### B13. Garbage collection

**Garbage collection (GC)** is the automatic process by which the JVM reclaims heap memory occupied by objects that are no longer **reachable** from the running program. Objects are created with `new`, but Java has no `delete` or `free()` — the garbage collector frees them.

**When an object becomes eligible for GC** — when no live reference can reach it:

1. The reference is set to `null` — `s = null;`
2. The reference is reassigned — `s = new Student();` orphans the old object.
3. The object was created inside a method — its local reference disappears when the method returns.
4. **Island of isolation** — objects refer only to each other, with no reference from outside.
5. Anonymous objects — `new Student().display();` is eligible right after the call.

**How it works (outline):** starting from *GC roots* (local variables on thread stacks, static fields, active threads), the collector **marks** every reachable object, **sweeps** away the rest and may **compact** the survivors. The heap is **generational**: new objects go to the *young generation* (frequent, fast *minor* GCs); long-lived ones are promoted to the *old generation* (rarer *major/full* GCs).

**Key facts:** `System.gc()` only *requests* a collection; `finalize()` is deprecated; memory leaks are still possible when references are kept by mistake (e.g. in a static list).

**Advantages:** no manual freeing, so no dangling pointers or double-free bugs, and far fewer leaks. **Limitations:** CPU overhead, occasional pauses, and no control over *when* an object is collected.

The long answer is [C13](#c13-garbage-collection-and-automatic-memory-management).

**Summary:** GC automatically frees the memory of unreachable objects; an object becomes eligible as soon as nothing references it.

---

### B14. Why `System.gc()` does not guarantee collection

`System.gc()` (the same as `Runtime.getRuntime().gc()`) is defined as a **request**, not a command:

1. **The specification says so.** Its Javadoc says that calling it *suggests* the JVM expend effort toward recycling unused objects, and that there is **no guarantee** it will reclaim any particular amount of memory or complete at any particular time.
2. **The JVM decides when to collect.** The collector follows its own heuristics — heap occupancy, allocation rate, pause-time goals — and usually knows better than the program when a collection is worthwhile.
3. **It can be switched off or changed.** With `-XX:+DisableExplicitGC` the call does nothing; a no-op collector such as Epsilon ignores the request; with G1 and `-XX:+ExplicitGCInvokesConcurrent` it starts a background (concurrent) cycle instead of a full collection.
4. **A particular object may survive anyway.** It is reclaimed only if it is really unreachable — one forgotten reference keeps it alive.
5. **Cleanup actions run later.** `Cleaner` actions and (deprecated) finalizers run on separate threads, some time after the collector finds the object unreachable.

On the default G1 collector a `System.gc()` call triggers a full, **stop-the-world** collection, so calling it in application code usually *hurts* performance. You can see both behaviours with GC logging:

```text
java -Xlog:gc MyProgram                          # log shows: Pause Full (System.gc())
java -XX:+DisableExplicitGC -Xlog:gc MyProgram   # no collection is logged
```

**Summary:** `System.gc()` is a hint that the JVM may delay, downgrade or ignore, so it never guarantees immediate collection.

---

### B15. Current status of `finalize()`

`protected void finalize() throws Throwable` is a method of `java.lang.Object`. The garbage collector *may* call it once on an unreachable object before reclaiming its memory; it was meant for releasing non-memory resources.

| Java version | Status |
|---|---|
| 1.0 (1996) | Introduced as a cleanup hook called by the GC |
| 9 (2017) | Deprecated |
| 18 (2022) | **Deprecated for removal** by JEP 421; the `--finalization=disabled` option lets you run with finalization switched off |
| 25 (LTS, used for these notes) | Still present as `@Deprecated(since="9", forRemoval=true)` and still enabled by default; overriding it makes javac warn `[removal] finalize() in Object has been deprecated and marked for removal` |

**Why it was deprecated:** it may never run (or run very late), runs on an unspecified thread, can "resurrect" the object, silently ignores exceptions thrown inside it, makes objects slower to allocate and reclaim, and opens security holes. The Javadoc's verdict: finalization "can lead to problems with security, performance, and reliability".

**What to use instead:** implement `AutoCloseable` and use **try-with-resources** (deterministic cleanup), or call an explicit `close()` method; use `java.lang.ref.Cleaner` (Java 9+) only as a safety net. Details in [C14](#c14-finalize-and-why-it-is-not-recommended).

**Summary:** `finalize()` still exists in Java 25 but is deprecated for removal — never rely on it; use try-with-resources or `Cleaner`.

---

### C. Long Answer / Theory Questions

Each answer is a full 8–10-mark answer: definition, explanation, diagram or table, a program where the question asks for one, advantages and limitations, and a one-line summary.

### C1. Fundamental OOP concepts in Java

**Definition**

Object-Oriented Programming (OOP) is a programming paradigm that organises a program around **objects** — units that combine data (state) with the methods that act on it (behaviour) — instead of around functions and logic. Java is built on OOP: every method lives inside a class or interface.

**Diagram**

```text
   +------------------------------------------------------------------+
   |                   Object-Oriented Programming                    |
   +---------------+-----------------+---------------+----------------+
   |  Abstraction  |  Encapsulation  |  Inheritance  |  Polymorphism  |   <- four pillars
   +---------------+-----------------+---------------+----------------+
   |                       Classes and Objects                        |   <- foundation
   +------------------------------------------------------------------+
```

**The concepts**

1. **Class** — a blueprint or template for creating objects; it defines the attributes and behaviours its objects will have. `class Employee { … }`
2. **Object** — an instance of a class with its own state, created with `new`. `new Manager("Michael Scott", 80000)`
3. **Abstraction** — hiding implementation details and exposing only essential features, using `abstract` classes and interfaces: `abstract double calculatePay();` says *what*; each subclass decides *how*.
4. **Encapsulation** — bundling data and methods into one class and hiding the data, using `private` fields with `public` getters/setters.
5. **Inheritance** — a subclass acquires the members of a superclass with `extends`, giving reuse and an "is-a" hierarchy: `class Manager extends Employee`.
6. **Polymorphism** — one interface, many forms: the same call behaves differently for different objects — compile-time through overloading, runtime through overriding.

Related terms: **message passing** (objects interact by calling each other's methods) and **dynamic binding** (the method body to run is chosen at runtime).

**Program — all the concepts in one example**

```java
abstract class Employee {                        // ABSTRACTION: abstract class
    private String name;                         // ENCAPSULATION: private data
    private double baseSalary;

    Employee(String name, double baseSalary) {
        this.name = name;
        this.baseSalary = baseSalary;
    }

    public String getName() {                    // controlled read access
        return name;
    }

    public double getBaseSalary() {
        return baseSalary;
    }

    abstract double calculatePay();              // WHAT, not HOW

    void showPay() {                             // concrete method shared by all
        System.out.println(getName() + " earns Rs. " + calculatePay());
    }
}

class Manager extends Employee {                 // INHERITANCE: Manager is-a Employee
    Manager(String name, double baseSalary) {
        super(name, baseSalary);
    }

    @Override
    double calculatePay() {                      // POLYMORPHISM: overriding
        return getBaseSalary() * 1.5;
    }
}

class Intern extends Employee {
    Intern(String name, double baseSalary) {
        super(name, baseSalary);
    }

    @Override
    double calculatePay() {
        return getBaseSalary() * 0.5;
    }
}

public class OopDemo {
    public static void main(String[] args) {
        Employee[] staff = {                     // OBJECTS created with new
            new Manager("Michael Scott", 80000),
            new Intern("Ryan Howard", 20000)
        };
        for (Employee e : staff) {
            e.showPay();                         // same call, different behaviour
        }
    }
}
```

**Sample output**

```text
Michael Scott earns Rs. 120000.0
Ryan Howard earns Rs. 10000.0
```

**Where each concept appears**

| Concept | Java mechanism | In the program |
|---|---|---|
| Class | `class` | `Employee`, `Manager`, `Intern`, `OopDemo` |
| Object | `new` | `new Manager("Michael Scott", 80000)` |
| Abstraction | `abstract` class / method, `interface` | `abstract double calculatePay();` |
| Encapsulation | `private` fields + getters/setters | `private double baseSalary;` + `getBaseSalary()` |
| Inheritance | `extends`, `super(...)` | `Manager extends Employee`, `super(name, baseSalary)` |
| Polymorphism | overloading, overriding | `e.showPay()` runs a different `calculatePay()` for each object |

**Advantages of OOP:** modularity (each class is a self-contained unit), reusability, easier maintenance and debugging, data security through hiding, extensibility, and natural modelling of real-world entities.

**Limitations:** more design effort and code for small programs, more memory for objects, a steeper learning curve, and not every problem fits naturally into objects. Java is also not *purely* object-oriented, because the primitive types (`int`, `char`, …) are not objects.

**Summary:** OOP in Java rests on classes and objects plus four pillars — abstraction, encapsulation, inheritance and polymorphism — which together give modular, reusable and maintainable code.

---

### C2. Classes, objects, object creation and member access

**Class**

A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviours (methods) that objects of the class will have, and encapsulates the data together with the methods that manipulate it.

```text
[access-modifier] class ClassName [extends SuperClass] [implements Interface1, ...] {
    // fields       - instance variables (one copy per object), static variables (one per class)
    // constructors - initialise new objects
    // methods      - behaviour
}
```

**Object**

An object is an instance of a class: a runtime entity with **state** (the values of its fields), **behaviour** (its methods) and **identity** (a unique reference that distinguishes it from every other object, even one with equal state).

**How an object is created**

`Student s1 = new Student("Monica Geller", 12);` performs three steps:

1. **Declaration** — `Student s1` creates a reference variable that can point to a `Student` object (a local variable lives on the stack).
2. **Instantiation** — the `new` operator allocates memory for a new object on the **heap** and gives its fields default values.
3. **Initialisation** — the constructor `Student(...)` runs and sets the fields; `new` returns the object's reference, which is stored in `s1`.

```text
      STACK (main)                      HEAP
    +-------------+         +----------------------------+
    | s1   ref ---+-------->| Student object #1          |
    |             |    +--->|   name   = "Monica Geller" |
    | s3   ref ---+----+    |   rollNo = 12              |
    |             |         +----------------------------+
    | s2   ref ---+-------->| Student object #2          |
    +-------------+         |   name   = "Chandler Bing" |
                            |   rollNo = 28              |
                            +----------------------------+
    s3 = s1 copies the reference, so s1 and s3 share object #1.
    The static fields college and count belong to the class, not to either object.
```

`new` is by far the most common way to create objects; others are `clone()`, deserialization, reflection and factory methods such as `Integer.valueOf()`.

**How members are accessed**

- **Instance members** through a reference with the **dot operator**: `s1.name`, `s1.display()`.
- **Static members** through the class name: `Student.count` (one copy shared by all objects).
- **Inside the class**, members are used directly, or through `this` when a parameter has the same name: `this.name = name;`.
- **Access modifiers** decide who may use a member: `private` (only inside the class), default (same package), `protected` (package + subclasses), `public` (everywhere).

**Program**

```java
class Student {
    String name;                        // instance variables: one copy per object
    int rollNo;
    static String college = "MIT-WPU";  // static variable: one copy for the class
    static int count = 0;

    Student(String name, int rollNo) {  // constructor: initialises a new object
        this.name = name;               // this.name = field, name = parameter
        this.rollNo = rollNo;
        count++;
    }

    void display() {                    // instance method
        System.out.println(rollNo + " | " + name + " | " + college);
    }
}

public class ClassObjectDemo {
    public static void main(String[] args) {
        Student s1 = new Student("Monica Geller", 12);   // declare + instantiate + initialise
        Student s2 = new Student("Chandler Bing", 28);

        s1.display();                   // method access with the dot operator
        s2.display();

        s2.rollNo = 29;                 // field access (allowed: rollNo is not private)
        System.out.println("Updated roll no: " + s2.rollNo);

        Student s3 = s1;                // copies the reference, not the object
        s3.name = "Monica G.";
        System.out.println("s1.name after changing s3: " + s1.name);

        System.out.println("Objects created: " + Student.count);   // static member via class name
    }
}
```

**Sample output**

```text
12 | Monica Geller | MIT-WPU
28 | Chandler Bing | MIT-WPU
Updated roll no: 29
s1.name after changing s3: Monica G.
Objects created: 2
```

**Class vs object**

| Basis | Class | Object |
|---|---|---|
| Meaning | Blueprint / template | Instance of the blueprint |
| Nature | Logical entity | Physical (runtime) entity |
| Memory | No memory for instance fields when declared | Heap memory allocated by `new` |
| How many | Declared once | Any number from one class |
| Created by | `class` keyword | `new` keyword plus a constructor |
| Example | `class Student` | `new Student("Monica Geller", 12)` |

**Summary:** A class declares fields, constructors and methods; `new` allocates an object on the heap, the constructor initialises it, and its members are reached with the dot operator — instance members through a reference, static members through the class name.

---

### C3. Abstraction using an abstract class

**Definition**

Abstraction is hiding the complex implementation details of a system and exposing only the essential features or functionalities to the user. It lets us build simplified models of real-world entities and keeps complexity manageable. Example: a driver uses the steering wheel and pedals (the *what*) without knowing how fuel injection works (the *how*).

**Ways to achieve abstraction in Java**

1. **Abstract classes** — partial abstraction (0–100%): abstract and concrete methods can be mixed.
2. **Interfaces** — full abstraction of behaviour (before Java 8 every method was abstract; `default` and `static` methods are now allowed too).

**Rules for an abstract class**

1. It is declared with the `abstract` keyword: `abstract class Shape { … }`.
2. It can contain **abstract methods** (declared without a body, ending in `;`) as well as **concrete methods**.
3. It **cannot be instantiated** — `new Shape()` is a compile error: *Shape is abstract; cannot be instantiated*.
4. It can have fields, constructors (run through `super(...)` from a subclass), static methods and even `main`.
5. A subclass must **override every abstract method**, or be declared `abstract` itself.
6. A class with even one abstract method must be declared abstract (an abstract class may also have none).
7. An abstract method cannot be `private`, `static` or `final` — each would prevent overriding (*illegal combination of modifiers*).
8. A reference of the abstract type can point to any subclass object: `Shape s = new Circle(7);`.

**Diagram**

```text
                 +--------------------------------+
                 |     <<abstract>> Shape         |
                 |--------------------------------|
                 | # name : String                |
                 |--------------------------------|
                 | + Shape(name)                  |
                 | + area() : double   {abstract} |
                 | + display() : void             |
                 +----------------+---------------+
                                  ^  extends
                  +---------------+---------------+
                  |                               |
        +---------+---------+           +---------+---------+
        |      Circle       |           |     Rectangle     |
        |-------------------|           |-------------------|
        | - radius          |           | - length, width   |
        | + area()          |           | + area()          |
        +-------------------+           +-------------------+
```

**Program**

```java
abstract class Shape {
    protected String name;

    Shape(String name) {                    // an abstract class CAN have a constructor
        this.name = name;
    }

    abstract double area();                 // abstract method: no body

    void display() {                        // concrete method, shared by all shapes
        System.out.printf("%s area = %.2f%n", name, area());
    }
}

class Circle extends Shape {
    private double radius;

    Circle(double radius) {
        super("Circle");
        this.radius = radius;
    }

    @Override
    double area() {                         // HOW, for a circle
        return Math.PI * radius * radius;
    }
}

class Rectangle extends Shape {
    private double length;
    private double width;

    Rectangle(double length, double width) {
        super("Rectangle");
        this.length = length;
        this.width = width;
    }

    @Override
    double area() {                         // HOW, for a rectangle
        return length * width;
    }
}

public class AbstractionDemo {
    public static void main(String[] args) {
        // Shape s = new Shape("x");        // error: Shape is abstract; cannot be instantiated
        Shape[] shapes = { new Circle(7), new Rectangle(4, 5) };
        for (Shape s : shapes) {
            s.display();                    // caller knows WHAT (area), not HOW
        }
    }
}
```

**Sample output**

```text
Circle area = 153.94
Rectangle area = 20.00
```

`display()` is written once in `Shape` and calls `area()`, whose body each subclass supplies — the caller only ever deals with the abstract `Shape` view.

**Abstract class vs interface**

| Basis | Abstract class | Interface |
|---|---|---|
| Keyword / use | `abstract class`, used with `extends` | `interface`, used with `implements` |
| Methods | abstract and concrete | abstract; `default`/`static` (Java 8+), `private` (Java 9+) |
| Variables | any kind | only `public static final` constants |
| Constructors | yes | no |
| Inheritance | a class extends only **one** | a class can implement **many** |
| Abstraction level | partial (0–100%) | full, for its abstract methods |
| Use when | related classes share code and state | unrelated classes share a capability (`Comparable`, `Runnable`) |

**Advantages:** reduces complexity, hides implementation details so they can change without affecting callers, forces subclasses to follow a common contract, avoids duplication through shared concrete methods, and enables runtime polymorphism.

**Limitations:** an abstract class cannot be instantiated, a class can extend only one abstract class, and the extra layer of design is unnecessary for very small programs.

**Summary:** Abstraction shows *what* and hides *how*; an abstract class declares abstract methods (the *what*) that concrete subclasses must implement (the *how*) while sharing common code.

---

### C4. Encapsulation and data hiding

**Definition**

Encapsulation is a core principle of OOP that involves bundling the data (attributes) and the methods that operate on that data into a single unit called a class. It achieves **data hiding** and protects the internal state of an object from being accessed or modified directly from outside the class — just as a capsule wraps its medicine.

**Encapsulation vs data hiding:** data hiding is *restricting direct access* to fields (with `private`); encapsulation is the broader idea of packaging data together with the methods that control it. Data hiding is the result; encapsulation is the technique.

**How encapsulation is implemented**

1. Declare the fields `private`.
2. Provide `public` **getters** (accessors) to read them and **setters** (mutators) or other methods to change them.
3. Validate inside those methods, so the object never holds invalid data.
4. Leave out a setter to make a field **read-only** (or leave out the getter for write-only).

**Access modifiers**

| Modifier | Same class | Same package | Subclass in another package | Everywhere |
|---|---|---|---|---|
| `private` | Yes | No | No | No |
| default (none) | Yes | Yes | No | No |
| `protected` | Yes | Yes | Yes | No |
| `public` | Yes | Yes | Yes | Yes |

**Diagram**

```text
     +-----------------------------------------------------+
     |                  class BankAccount                  |
     |   +---------------------------------------------+   |
     |   |  private data (hidden):                     |   |
     |   |     accountNo, holder, balance              |   |
     |   +----------------------^----------------------+   |
     |                          |  reachable only through  |
     |   public methods:  getAccountNo(), getHolder(),     |
     |                    getBalance(), deposit(),         |
     |                    withdraw()                       |
     +--------------------------^--------------------------+
                                |
          outside code ---------+   (cannot touch balance directly)
```

**Program — data hiding**

```java
class BankAccount {
    private final String accountNo;      // read-only: getters but no setters
    private final String holder;
    private double balance;              // hidden: changed only by deposit()/withdraw()

    BankAccount(String accountNo, String holder, double openingBalance) {
        this.accountNo = accountNo;
        this.holder = holder;
        this.balance = (openingBalance > 0) ? openingBalance : 0;
    }

    public String getAccountNo() {
        return accountNo;
    }

    public String getHolder() {
        return holder;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            System.out.println("Deposit rejected: amount must be positive");
        } else {
            balance += amount;
            System.out.println("Deposited " + amount + ", balance = " + balance);
        }
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Withdrawal rejected: amount must be positive");
        } else if (amount > balance) {
            System.out.println("Withdrawal of " + amount + " rejected: insufficient balance");
        } else {
            balance -= amount;
            System.out.println("Withdrew " + amount + ", balance = " + balance);
        }
    }
}

public class DataHidingDemo {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount("SB-1001", "Rachel Green", 5000);

        // acc.balance = 1000000;      // error: balance has private access in BankAccount
        acc.deposit(2000);
        acc.deposit(-300);             // invalid data is stopped by validation
        acc.withdraw(10000);           // more than the balance
        acc.withdraw(1500);

        System.out.println("Account : " + acc.getAccountNo());
        System.out.println("Holder  : " + acc.getHolder());
        System.out.println("Balance : " + acc.getBalance());
    }
}
```

**Sample output**

```text
Deposited 2000.0, balance = 7000.0
Deposit rejected: amount must be positive
Withdrawal of 10000.0 rejected: insufficient balance
Withdrew 1500.0, balance = 5500.0
Account : SB-1001
Holder  : Rachel Green
Balance : 5500.0
```

If the commented line is enabled, compilation fails with *balance has private access in BankAccount* — the only way to change the balance is through `deposit()` and `withdraw()`, which validate every request.

**Advantages:** data protection and integrity, control over access (read-only/write-only fields), freedom to change the internal representation (e.g. store the balance in paise) without affecting other classes, modular and maintainable code, and easier testing and debugging.

**Limitations:** more code (a getter and setter per field), and blindly adding a setter for every field weakens the protection — expose only the operations the object really needs.

**Encapsulation vs abstraction**

| Basis | Encapsulation | Abstraction |
|---|---|---|
| Focus | Protecting data and bundling it with its methods | Hiding complexity; *what* an object does |
| Level | Implementation level | Design level |
| Hides | Internal state (fields) | Implementation details (method bodies) |
| Achieved by | `private` fields, getters/setters, access modifiers | Abstract classes, interfaces |
| Example | `private double balance` + `getBalance()` | `abstract double area()` in `Shape` |

**Summary:** Encapsulation binds data and methods into a class and hides the data behind `private`, so outside code can reach it only through validated public methods.

---

### C5. Inheritance and its types

**Definition**

Inheritance is a key feature of OOP that allows a new class (**subclass** / derived / child class) to inherit properties and behaviours (attributes and methods) from an existing class (**superclass** / base / parent class). This promotes code reusability: the subclass uses the superclass's functionality while adding its own features or overriding existing ones. Inheritance establishes an **"is-a"** relationship — a `Manager` *is an* `Employee`.

```text
class SubClass extends SuperClass {
    // extra fields and methods, overridden methods
}
```

**Key points**

- A subclass inherits the `public` and `protected` members of its superclass (and default-access members when both are in the same package).
- **`private` members are not inherited** — the fields still exist inside the subclass object, but the subclass can reach them only through the superclass's public or protected methods.
- **Constructors are not inherited.** A subclass constructor calls a superclass constructor with `super(...)` as its first statement; if it is omitted, `super()` is inserted automatically.
- `super.method()` calls the superclass version of an overridden method.
- Every class implicitly extends `java.lang.Object`, the root of the hierarchy.
- A `final` class (e.g. `String`) cannot be extended, and a `final` method cannot be overridden.

**Types of inheritance**

```text
 1. Single   2. Multilevel 3. Hierarchical     4. Multiple         5. Hybrid
                                            (interfaces only)  (interfaces only)

     A             A              A              A     B               A
     ^             ^             ^ ^              ^   ^               ^ ^
     |             |            /   \              \ /               /   \
     B             B           B     C              C               B     C
                   ^                                                 ^   ^
                   |                                                  \ /
                   C                                                   D
```

| Type | Meaning | Supported with classes? | Example |
|---|---|---|---|
| Single | One subclass extends one superclass | Yes | `Employee extends Person` |
| Multilevel | A chain: C extends B, B extends A | Yes | `Manager` → `Employee` → `Person` |
| Hierarchical | Several subclasses extend one superclass | Yes | `Employee` and `Student` both extend `Person` |
| Multiple | One class inherits from two or more parents | **No** with classes; **yes with interfaces** | `class Professor implements Teacher, Researcher` |
| Hybrid | A combination of two or more of the above | Only when the multiple part uses interfaces | `Professor extends Employee implements Teacher, Researcher` |

**Why Java has no multiple inheritance of classes — the diamond problem**

If classes `B` and `C` both override `show()` from `A`, and `D` could extend both, `d.show()` would be ambiguous. Java therefore rejects `class D extends B, C` outright. Interfaces carry no instance state, and if two interfaces supply the same `default` method the compiler forces the class to override it (*types B and C are incompatible; class D inherits unrelated defaults for show() from types B and C*), so the choice is made explicitly — for example with `B.super.show()`.

**Program — single, multilevel, hierarchical and multiple (through interfaces)**

```java
class Person {                                   // superclass
    String name;

    void introduce() {
        System.out.println("I am " + name);
    }
}

class Employee extends Person {                  // SINGLE: Employee -> Person
    void work() {
        System.out.println(name + " goes to work");
    }
}

class Manager extends Employee {                 // MULTILEVEL: Manager -> Employee -> Person
    void manage() {
        System.out.println(name + " manages a team");
    }
}

class Student extends Person {                   // HIERARCHICAL: Person has two subclasses
    void study() {
        System.out.println(name + " studies Java");
    }
}

interface Teacher {
    void teach();
}

interface Researcher {
    void research();
}

class Professor extends Employee implements Teacher, Researcher {   // MULTIPLE via interfaces
    public void teach() {
        System.out.println(name + " teaches OOP");
    }

    public void research() {
        System.out.println(name + " publishes papers");
    }
}

public class InheritanceTypesDemo {
    public static void main(String[] args) {
        Manager m = new Manager();
        m.name = "Michael Scott";        // field inherited from Person
        m.introduce();                   // from Person (two levels up)
        m.work();                        // from Employee
        m.manage();                      // Manager's own method

        Student s = new Student();
        s.name = "Monica Geller";
        s.introduce();
        s.study();

        Professor p = new Professor();
        p.name = "Ross Geller";
        p.teach();
        p.research();
    }
}
```

**Sample output**

```text
I am Michael Scott
Michael Scott goes to work
Michael Scott manages a team
I am Monica Geller
Monica Geller studies Java
Ross Geller teaches OOP
Ross Geller publishes papers
```

`Professor` extends one class and implements two interfaces, so together with the `Person` tree the design is **hybrid** inheritance. Constructor chaining with `super(...)` is shown in [P3](#p3-inheritance-using-extends).

**Advantages:** code reuse, method overriding and runtime polymorphism, extension without touching tested code, a logical "is-a" hierarchy, and less duplication.

**Limitations:** tight coupling (a change in the superclass can break subclasses), deep hierarchies are hard to follow, only one superclass per class, and inheritance suits only true "is-a" relationships — otherwise prefer composition ("has-a").

**Summary:** Inheritance (`extends`) lets a subclass reuse and extend a superclass; Java supports single, multilevel and hierarchical inheritance with classes, and multiple (hence hybrid) inheritance only through interfaces.

---

### C6. Compile-time and runtime polymorphism

**Definition**

Polymorphism (Greek *poly* = many, *morph* = forms) is a fundamental OOP concept that allows objects of different classes to be treated as objects of a common superclass. A single interface represents different underlying forms, so the same method name can behave differently depending on the object that invokes it.

| Form | Achieved by | Resolved at |
|---|---|---|
| Compile-time (static) polymorphism | Method overloading | Compile time |
| Runtime (dynamic) polymorphism | Method overriding | Runtime |

**1. Compile-time polymorphism — method overloading**

Several methods in the same class share a name but differ in their **parameter list**. The compiler picks the method by matching the arguments (*static* or *early binding*).

- The parameters must differ in **number**, **type** or **order** of types.
- A different return type alone is not enough — `int f(int)` and `double f(int)` together give *method f(int) is already defined*.
- If there is no exact match, Java widens the argument (`int` → `long` → `float` → `double`) to find one.
- Constructors can be overloaded too.

```java
class Calculator {
    int add(int a, int b) {                     // two int parameters
        return a + b;
    }

    int add(int a, int b, int c) {              // different NUMBER of parameters
        return a + b + c;
    }

    double add(double a, double b) {            // different TYPE of parameters
        return a + b;
    }

    String add(String a, String b) {            // different TYPE again
        return a + b;
    }
}

public class CompileTimePolymorphism {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println(calc.add(10, 20));            // add(int, int)
        System.out.println(calc.add(10, 20, 30));        // add(int, int, int)
        System.out.println(calc.add(2.5, 3.5));          // add(double, double)
        System.out.println(calc.add("Hello, ", "Java")); // add(String, String)
        System.out.println(calc.add(5, 2.5));            // 5 widened to 5.0 -> add(double, double)
    }
}
```

**Sample output**

```text
30
60
6.0
Hello, Java
7.5
```

**2. Runtime polymorphism — method overriding**

A subclass provides its own body for an inherited method, keeping the **same signature**. When the method is called through a **superclass reference** (upcasting), the JVM runs the version belonging to the **actual object** — *dynamic method dispatch* (*late binding*).

- Same method name, same parameter list, and the same return type (or a subtype — covariant return).
- Requires inheritance (an "is-a" relationship).
- The access level cannot be reduced (a `public` method cannot become `protected`).
- `static`, `final` and `private` methods cannot be overridden; neither can constructors.
- An overriding method cannot throw new or broader checked exceptions.
- `@Override` is optional but recommended — the compiler then catches mistakes such as a wrong parameter type.

```java
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("Cat meows");
    }
}

public class RuntimePolymorphism {
    public static void main(String[] args) {
        Animal a;                   // superclass reference

        a = new Animal();
        a.sound();                  // Animal's version

        a = new Dog();              // upcasting
        a.sound();                  // Dog's version, chosen at runtime

        a = new Cat();
        a.sound();                  // Cat's version
    }
}
```

**Sample output**

```text
Animal makes a sound
Dog barks
Cat meows
```

```text
  Animal a = new Dog();        reference type: Animal        object type: Dog
  a.sound();
     compile time : javac checks that class Animal HAS a sound() method
     run time     : the JVM looks at the real object (Dog) and runs Dog.sound()  ->  "Dog barks"
```

**Overloading vs overriding**

| Basis | Overloading (compile-time) | Overriding (runtime) |
|---|---|---|
| Where | Same class (or inherited) | Superclass and subclass |
| Parameters | Must differ | Must be the same |
| Return type | Can differ | Same or covariant |
| Binding | Static / early, by the compiler | Dynamic / late, by the JVM |
| Inheritance | Not required | Required |
| `static` / `final` / `private` methods | Can be overloaded | Cannot be overridden |
| Purpose | Same operation for different inputs | Specialised behaviour in a subclass |

**Advantages:** one name for related operations (readability), extensible code (a new subclass works with existing code written against the superclass), loose coupling, and no long `if`/`switch` chains on object type.

**Limitations:** dynamic dispatch is harder to trace while debugging, and careless overloading can make a call ambiguous — with `add(int, long)` and `add(long, int)`, the call `add(1, 2)` fails with *reference to add is ambiguous*.

**Summary:** Polymorphism lets one name take many forms — overloading is resolved by the compiler from the arguments, overriding by the JVM from the actual object.

---

### C7. Identifiers, keywords and naming rules

**Identifiers**

An identifier is a name given by the programmer to a program element — a class, interface, variable, method, constant, package, parameter or label. In `int totalMarks = 450;` the identifier is `totalMarks`.

**Rules for valid identifiers (enforced by the compiler)**

1. They may contain **letters** (`A–Z`, `a–z` and other Unicode letters), **digits** (`0–9`), the **underscore** `_` and the **dollar sign** `$`.
2. They **cannot start with a digit**.
3. They **cannot be a keyword** (`int`, `class`, `goto`, …) or one of the literals `true`, `false`, `null`.
4. **No spaces** or other symbols such as `-`, `#`, `@`, `%`, `.`.
5. They are **case-sensitive**: `total`, `Total` and `TOTAL` are different identifiers.
6. **Unlimited length** — but names should be meaningful.
7. A **single underscore `_`** cannot be a name since Java 9 (it is a keyword; Java 22+ uses it only to mark unnamed variables).

| Identifier | Valid? | Reason |
|---|---|---|
| `studentName` | Yes | letters only |
| `marks1` | Yes | digit allowed after the first character |
| `_count`, `$price` | Yes | `_` and `$` allowed, even first |
| `MAX_MARKS` | Yes | letters and underscore |
| `1marks` | No | starts with a digit |
| `student name` | No | contains a space |
| `roll#no` | No | `#` is not allowed |
| `int` | No | keyword |
| `null` | No | reserved literal |

**Naming conventions** (recommended, not enforced): `PascalCase` for classes (`StudentRecord`), `camelCase` for methods and variables (`getTotal`, `totalMarks`), `UPPER_SNAKE_CASE` for constants (`MAX_MARKS`), lowercase for packages (`com.mitwpu.mca`). Avoid `$` and a leading `_` in your own names.

**Keywords**

A keyword (reserved word) is a word whose meaning is predefined by the language, so it cannot be used as an identifier. All keywords are lowercase. Java SE 25 has **51 reserved keywords** — the 50 below plus `_`:

| Category | Keywords |
|---|---|
| Primitive types (8) | `byte` `short` `int` `long` `float` `double` `char` `boolean` |
| Flow control (11) | `if` `else` `switch` `case` `default` `for` `while` `do` `break` `continue` `return` |
| Exception handling (6) | `try` `catch` `finally` `throw` `throws` `assert` |
| Class and object (11) | `class` `interface` `enum` `extends` `implements` `new` `this` `super` `instanceof` `package` `import` |
| Access modifiers (3) | `public` `protected` `private` |
| Other modifiers (8) | `static` `final` `abstract` `synchronized` `volatile` `transient` `native` `strictfp` |
| Return type (1) | `void` |
| Reserved but unused (2) | `goto` `const` |

- `true`, `false` and `null` are **literals**, not keywords, but they are equally forbidden as identifiers.
- **Contextual keywords** such as `var`, `record`, `yield`, `sealed` and `permits` are special only in certain positions, so `int record = 5;` is still legal (though `var` and `record` cannot name a class).

**Identifier vs keyword**

| Basis | Identifier | Keyword |
|---|---|---|
| Defined by | Programmer | Language |
| Purpose | Names a program element | Gives structure or an instruction to the compiler |
| Case | Any mix (case-sensitive) | Always lowercase |
| How many | Unlimited | Fixed (51 reserved in Java SE 25) |
| Usable as a name | Yes | No |
| Example | `totalMarks`, `Student` | `int`, `class`, `static` |

**Program**

```java
public class IdentifierDemo {
    static final int MAX_MARKS = 100;        // constant: letters and underscore

    public static void main(String[] args) {
        String studentName = "Joey";         // camelCase variable
        int marks1 = 78;                     // digit allowed after the first character
        int Marks1 = 80;                     // legal, and different from marks1 (case-sensitive)
        int _count = 3;                      // may start with _
        double $price = 499.0;               // may start with $ (legal, but avoid)

        // int 1marks = 78;                  // invalid: starts with a digit
        // String student name = "Joey";     // invalid: contains a space
        // int total-marks = 90;             // invalid: '-' is not allowed
        // int class = 5;                    // invalid: class is a keyword
        // boolean true = false;             // invalid: true is a reserved literal

        System.out.println(studentName + " " + marks1 + " " + Marks1 + " "
                + _count + " " + $price + " " + MAX_MARKS);
    }
}
```

**Sample output**

```text
Joey 78 80 3 499.0 100
```

**Summary:** Identifiers are programmer-chosen names that may use only letters, digits, `_` and `$`, cannot start with a digit and cannot be a keyword or `true`/`false`/`null`; keywords are the 51 lowercase reserved words that make up the language itself.

---

### C8. Primitive and non-primitive data types

**Definition**

A data type tells the compiler what kind of value a variable holds, how much memory it needs and which operations are valid on it. Java is **statically typed** — every variable's type is fixed at compile time.

**Classification**

```text
                                 Java data types
                                        |
                  +---------------------+---------------------+
                  |                                           |
            Primitive (8)                         Non-primitive (reference)
                  |                                           |
    +---------+---+-------+---------+         +-------+-------+-------+-----------+------+
    |         |           |         |         |       |       |       |           |      |
 Integer   Floating   Character  Boolean    String  Array   Class  Interface    Enum  Wrapper
 byte      float      char       boolean                                            (Integer, ...)
 short     double
 int
 long
```

**1. Primitive data types** — built into the language, named by keywords, store the **actual value**, fixed size:

| Type | Size | Range | Default (fields) |
|---|---|---|---|
| `byte` | 8-bit | −128 to 127 | `0` |
| `short` | 16-bit | −32,768 to 32,767 | `0` |
| `int` | 32-bit | −2,147,483,648 to 2,147,483,647 | `0` |
| `long` | 64-bit | −2⁶³ to 2⁶³−1 | `0L` |
| `float` | 32-bit | about ±3.4 × 10³⁸ (6–7 digits) | `0.0f` |
| `double` | 64-bit | about ±1.8 × 10³⁰⁸ (15–16 digits) | `0.0d` |
| `char` | 16-bit | `'\u0000'` to `'\uffff'` (Unicode) | `'\u0000'` |
| `boolean` | JVM-dependent | `true` / `false` | `false` |

**2. Non-primitive (reference) data types** — created by the programmer or supplied by the Java library; the variable stores a **reference** to an object on the heap:

- **String** — a sequence of characters: `String name = "Chandler";` (a class, but with literal syntax)
- **Array** — a fixed-size collection of one type: `int[] marks = {78, 85, 91};`
- **Class** — a user-defined type: `Student s = new Student();`
- **Interface** — a contract that classes implement: `Comparable`, `Runnable`
- **Enum** — a fixed set of constants: `enum Day { MON, TUE, WED }`
- **Wrapper classes** — object versions of the primitives: `Integer`, `Double`, `Character`, …

**Primitive vs non-primitive**

| Basis | Primitive | Non-primitive |
|---|---|---|
| Defined by | Java language (keywords) | Programmer or Java library |
| Variable holds | The value itself | A reference to an object |
| Where the data lives | In the variable (stack for locals, inside the object for fields) | Object on the heap |
| Default value (fields) | `0`, `0.0`, `'\u0000'`, `false` | `null` |
| Can be `null` | No | Yes |
| Methods | None | Yes, e.g. `name.length()` |
| Size | Fixed (e.g. `int` = 4 bytes) | Depends on the object |
| Naming | lowercase keywords (`int`) | Class names start with uppercase (`String`) |
| Examples | `int`, `char`, `double`, `boolean` | `String`, `int[]`, `Student`, `Integer` |

**Type conversion**

- **Widening (automatic):** `byte → short → int → long → float → double`, and `char → int`; e.g. `double d = 10;` stores `10.0`.
- **Narrowing (explicit cast, may lose data):** `(int) 3.99` is `3`; `(byte) 130` is `-126`.
- **Autoboxing / unboxing:** `Integer x = 5;` (int → Integer), `int y = x;` (Integer → int).

**Program**

```java
public class DataTypesDemo {
    static int defaultInt;                 // fields get default values automatically
    static boolean defaultFlag;
    static String defaultText;

    public static void main(String[] args) {
        // primitive types: the variable holds the value itself
        byte age = 21;
        short year = 2026;
        int salary = 1_50_000;             // underscores for readability (Java 7+)
        long distance = 9_460_730_472_580L;   // beyond int range: needs the L suffix
        float price = 99.99f;              // f suffix: float literal
        double pi = 3.141592653589793;
        char grade = 'A';
        boolean passed = true;

        System.out.println("byte=" + age + ", short=" + year + ", int=" + salary);
        System.out.println("long=" + distance + ", float=" + price + ", double=" + pi);
        System.out.println("char=" + grade + ", boolean=" + passed);

        // non-primitive (reference) types: the variable holds a reference to an object
        String name = "Chandler";
        int[] marks = {78, 85, 91};
        StringBuilder course = new StringBuilder("MCA");

        System.out.println("String=" + name + " (length " + name.length() + ")");
        System.out.println("array length=" + marks.length + ", marks[1]=" + marks[1]);
        System.out.println("StringBuilder=" + course.append(" 2026"));

        // default values of fields
        System.out.println("defaults: int=" + defaultInt + ", boolean=" + defaultFlag
                + ", String=" + defaultText);

        // wrapper class: autoboxing and unboxing
        Integer boxed = salary;            // int -> Integer
        int unboxed = boxed;               // Integer -> int
        System.out.println("Integer.MAX_VALUE=" + Integer.MAX_VALUE + ", unboxed=" + unboxed);
    }
}
```

**Sample output**

```text
byte=21, short=2026, int=150000
long=9460730472580, float=99.99, double=3.141592653589793
char=A, boolean=true
String=Chandler (length 8)
array length=3, marks[1]=85
StringBuilder=MCA 2026
defaults: int=0, boolean=false, String=null
Integer.MAX_VALUE=2147483647, unboxed=150000
```

**Summary:** Primitive types are the 8 built-in value types with fixed sizes; non-primitive types (String, arrays, classes, interfaces, enums, wrappers) are references to heap objects whose default is `null`.

---

### C9. Naming and formatting conventions

**Definition**

Coding conventions are guidelines for naming, formatting, commenting and organising source code. The compiler does not check them — code that ignores them still compiles — but they make code consistent and readable. Java's standard conventions come from Sun's (now Oracle's) *Code Conventions for the Java Programming Language*; many organisations follow the Google Java Style Guide.

**Why they matter**

- About 80% of the lifetime cost of software goes to maintenance, and hardly any software is maintained by its original author (Sun's conventions document).
- Consistent code is quicker to read, review, debug and extend.
- Teams can share and merge code without arguing over style.
- Some conventions prevent bugs — e.g. braces around every `if` body.

**1. Naming conventions**

| Element | Convention | Good | Avoid |
|---|---|---|---|
| Package | all lowercase, reverse internet domain | `com.mitwpu.mca.lab` | `Com.MITWPU.Lab` |
| Class / interface / enum | `PascalCase` nouns (interfaces often adjectives) | `StudentRecord`, `Comparable` | `studentrecord`, `Student_Record` |
| Method | `camelCase`, starting with a verb | `calculateGrade()`, `getName()` | `Grade()`, `calculate_grade()` |
| Variable | `camelCase`, meaningful noun | `totalMarks`, `rollNo` | `tm`, `TotalMarks` |
| Constant | `UPPER_SNAKE_CASE`, `static final` | `MAX_STUDENTS`, `PASS_MARKS` | `maxStudents` |
| Boolean | `is` / `has` / `can` prefix | `isPassed`, `hasNext()` | `flag`, `check` |
| Type parameter | single uppercase letter | `T`, `E`, `K`, `V` | `Type` |
| Source file | same name as its public class | `StudentRecord.java` | anything else (a compile error) |

**2. Formatting conventions**

1. **Indentation:** 4 spaces per level (Sun; Google style uses 2) — never mix tabs and spaces.
2. **Line length:** under 80 characters (Sun; Google allows 100); break long lines after a comma or before an operator.
3. **Braces:** the opening brace ends the declaration line and the closing brace sits on its own line, aligned with the start of the statement (K&R style); use braces even for single-statement `if`/`for` bodies.
4. **One statement per line**, and preferably one variable declaration per line.
5. **White space:** a blank line between methods and between logical sections; spaces around binary operators (`a + b`), after commas and after keywords (`if (`), but none between a method name and its `(`.
6. **Class layout:** static variables → instance variables → constructors → methods.
7. **Comments:** `//` for short notes, `/* … */` for blocks, `/** … */` Javadoc for public classes and methods; explain *why*, not *what*.
8. **File structure:** the `package` statement, then `import`s, then one public top-level class.

**Before and after**

Ignoring the conventions — it compiles, but it is hard to read:

```java
class student_record{
int MARKS1,Marks2;static final int passmarks=100;
boolean Pass(){if(MARKS1+Marks2>=passmarks)return true;else return false;}}
```

Following the conventions:

```java
/** Stores the marks of one student and decides the result. */
class StudentRecord {
    static final int PASS_MARKS = 100;     // constant: UPPER_SNAKE_CASE

    private int marks1;                    // variables: camelCase, one per line
    private int marks2;

    /** Returns true if the total reaches PASS_MARKS. */
    boolean isPassed() {                   // method: verb; boolean method: "is" prefix
        return marks1 + marks2 >= PASS_MARKS;
    }
}
```

IDEs can reformat a file automatically (Eclipse, IntelliJ IDEA and VS Code all have a *Format Document* / *Reformat Code* command), and tools such as **Checkstyle** report convention violations.

**Summary:** Java conventions — PascalCase classes, camelCase methods and variables, UPPER_SNAKE_CASE constants, lowercase packages, 4-space indentation, K&R braces and one statement per line — make code readable and maintainable even though the compiler does not enforce them.

---

### C10. Expressions and operators

**Expression**

An expression is a combination of **operands** (variables, literals, method calls) and **operators** that the JVM evaluates to produce a single value; every expression has a type. In `total = marks + bonus * 2`, the operands are `marks`, `bonus` and `2`, and the operators are `+`, `*` and `=`.

By the number of operands, operators are **unary** (one: `-a`, `!flag`, `i++`), **binary** (two: `a + b`) or **ternary** (three: `c ? x : y`).

**Categories of operators** (results for `a = 10`, `b = 3`)

| Category | Operators | Example | Result |
|---|---|---|---|
| Arithmetic | `+` `-` `*` `/` `%` | `a / b`, `a % b` | `3`, `1` |
| Unary | `+` `-` `++` `--` `!` `~` | `x = 5; y = x++;` | `y = 5`, `x = 6` |
| Relational | `==` `!=` `>` `<` `>=` `<=` | `a > b` | `true` |
| Logical | `&&` `\|\|` `!` | `a > 5 && b > 5` | `false` |
| Bitwise | `&` `\|` `^` `~` | `a & b` (`1010 & 0011`) | `2` |
| Shift | `<<` `>>` `>>>` | `a << 1`, `a >> 1` | `20`, `5` |
| Assignment | `=` `+=` `-=` `*=` `/=` `%=` (also `&=` `\|=` `^=` `<<=` `>>=` `>>>=`) | `c = 10; c += 5;` | `15` |
| Conditional (ternary) | `? :` | `(a > b) ? a : b` | `10` |
| Type comparison | `instanceof` | `"Java" instanceof String` | `true` |

Other operators: `+` for string concatenation (`"Roll " + 28`), `.` for member access, `[]` for array indexing, `(type)` for casts, `new`, and `->` for lambdas.

**Important details**

- **Integer division** truncates: `10 / 3` is `3`, while `10.0 / 3` is `3.3333333333333335`. The result of `%` takes the sign of the left operand: `-7 % 2` is `-1`.
- **Pre vs post increment:** `++x` increments first and then uses the value; `x++` uses the value and then increments.
- **Short-circuit:** in `p && q`, `q` is not evaluated if `p` is false; in `p || q`, `q` is not evaluated if `p` is true. So `k != 0 && 10 / k > 1` is safe even when `k` is `0`.
- **Type promotion:** `byte`, `short` and `char` operands are promoted to `int`, so `byte z = x + y;` (with `byte x, y`) fails with *possible lossy conversion from int to byte*; an expression mixing `int` and `double` is `double`.
- **String concatenation** runs left to right: `1 + 2 + "3"` is `"33"`, but `"1" + 2 + 3` is `"123"`.

**Precedence and associativity (highest first)**

| Level | Operators | Associativity |
|---|---|---|
| 1 | postfix `x++` `x--` | left to right |
| 2 | unary `++x` `--x` `+` `-` `~` `!`, cast | right to left |
| 3 | multiplicative `*` `/` `%` | left to right |
| 4 | additive `+` `-` | left to right |
| 5 | shift `<<` `>>` `>>>` | left to right |
| 6 | relational `<` `>` `<=` `>=` `instanceof` | left to right |
| 7 | equality `==` `!=` | left to right |
| 8 | bitwise AND `&` | left to right |
| 9 | bitwise XOR `^` | left to right |
| 10 | bitwise OR `\|` | left to right |
| 11 | logical AND `&&` | left to right |
| 12 | logical OR `\|\|` | left to right |
| 13 | ternary `? :` | right to left |
| 14 | assignment `=` `+=` `-=` … | right to left |

Worked example — `10 + 20 * 3 / 4 - 2`:

```text
10 + 20 * 3 / 4 - 2
   = 10 + 60 / 4 - 2      * and / first, left to right
   = 10 + 15 - 2
   = 25 - 2               then + and -, left to right
   = 23
```

**Program**

```java
public class OperatorsDemo {
    public static void main(String[] args) {
        int a = 10, b = 3;

        // 1. Arithmetic
        System.out.println("a + b = " + (a + b) + ", a - b = " + (a - b));
        System.out.println("a * b = " + (a * b) + ", a / b = " + (a / b) + ", a % b = " + (a % b));
        System.out.println("10.0 / 3 = " + (10.0 / 3));

        // 2. Unary (increment)
        int x = 5;
        int y = x++;                       // post: use 5, then x becomes 6
        int z = ++x;                       // pre: x becomes 7, then use 7
        System.out.println("y = " + y + ", z = " + z + ", x = " + x);

        // 3. Relational
        System.out.println("a > b: " + (a > b) + ", a == b: " + (a == b) + ", a != b: " + (a != b));

        // 4. Logical (with short-circuit)
        System.out.println("a > 5 && b > 5: " + (a > 5 && b > 5));
        System.out.println("a > 5 || b > 5: " + (a > 5 || b > 5));
        int k = 0;
        // the right side is skipped, so there is no division by zero
        System.out.println("k != 0 && 10 / k > 1: " + (k != 0 && 10 / k > 1));

        // 5. Bitwise and shift (10 = 1010, 3 = 0011)
        System.out.println("a & b = " + (a & b) + ", a | b = " + (a | b));
        System.out.println("a ^ b = " + (a ^ b) + ", ~a = " + (~a));
        System.out.println("a << 1 = " + (a << 1) + ", a >> 1 = " + (a >> 1));

        // 6. Assignment
        int c = 10;
        c += 5;                            // same as c = c + 5
        System.out.println("c += 5 gives " + c);

        // 7. Conditional (ternary)
        System.out.println("max = " + ((a > b) ? a : b));

        // 8. instanceof
        String s = "Java";
        System.out.println("s instanceof String: " + (s instanceof String));

        // Precedence: * and / before + and -
        System.out.println("10 + 20 * 3 / 4 - 2 = " + (10 + 20 * 3 / 4 - 2));
    }
}
```

**Sample output**

```text
a + b = 13, a - b = 7
a * b = 30, a / b = 3, a % b = 1
10.0 / 3 = 3.3333333333333335
y = 5, z = 7, x = 7
a > b: true, a == b: false, a != b: true
a > 5 && b > 5: false
a > 5 || b > 5: true
k != 0 && 10 / k > 1: false
a & b = 2, a | b = 11
a ^ b = 9, ~a = -11
a << 1 = 20, a >> 1 = 5
c += 5 gives 15
max = 10
s instanceof String: true
10 + 20 * 3 / 4 - 2 = 23
```

**Summary:** An expression combines operands and operators into one value; Java's operators fall into arithmetic, unary, relational, logical, bitwise, shift, assignment, conditional and `instanceof` categories, evaluated by precedence and associativity.

---

### C11. Decision-making statements with examples

**Definition**

Decision-making (selection or conditional) statements let a program choose which statements to execute based on a condition — a `boolean` expression. Java provides `if`, `if-else`, the `else-if` ladder, nested `if`, `switch` and the conditional (ternary) operator.

**Flow of an if-else**

```text
               +--------------------+
               |   test condition   |
               +---------+----------+
                  true   |   false
            +------------+------------+
            v                         v
     +-------------+           +-------------+
     |  if block   |           | else block  |
     +------+------+           +------+------+
            +------------+------------+
                         v
                  next statement
```

**The statements**

1. **`if`** — runs a block only when the condition is true.
2. **`if-else`** — a two-way branch: one block when true, the other when false.
3. **`else-if` ladder** — tests conditions from top to bottom; the first true one runs and control leaves the ladder; the final `else` is the fallback.
4. **Nested `if`** — an `if` inside another `if`, for a condition that only matters when an outer condition holds.
5. **`switch`** — compares one expression with many constant `case` labels.
   - The expression may be `byte`, `short`, `char`, `int`, their wrappers, `String` (Java 7+) or an `enum`; not `long`, `float`, `double` or `boolean` (Java 21+ also allows type patterns).
   - Case labels must be unique compile-time constants (otherwise *duplicate case label* or *constant expression required*).
   - `break` ends the `switch`; without it control **falls through** into the next case (handy for grouping, e.g. `case 6: case 7:`).
   - `default` runs when no case matches; it is optional.
6. **Ternary operator `?:`** — `condition ? value1 : value2`, a compact if-else that produces a value.

**Program — all six forms**

```java
public class DecisionMakingDemo {
    public static void main(String[] args) {
        int marks = 72;
        int age = 20;
        int day = 3;

        // 1. if
        if (marks >= 40) {
            System.out.println("1. if         : passed");
        }

        // 2. if-else
        if (marks % 2 == 0) {
            System.out.println("2. if-else    : " + marks + " is even");
        } else {
            System.out.println("2. if-else    : " + marks + " is odd");
        }

        // 3. else-if ladder
        if (marks >= 75) {
            System.out.println("3. ladder     : Distinction");
        } else if (marks >= 60) {
            System.out.println("3. ladder     : First class");
        } else if (marks >= 40) {
            System.out.println("3. ladder     : Pass class");
        } else {
            System.out.println("3. ladder     : Fail");
        }

        // 4. nested if
        if (age >= 18) {
            if (marks >= 60) {
                System.out.println("4. nested if  : eligible for the scholarship");
            } else {
                System.out.println("4. nested if  : adult, but marks below 60");
            }
        } else {
            System.out.println("4. nested if  : not an adult");
        }

        // 5. switch (break stops fall-through)
        switch (day) {
            case 1:
                System.out.println("5. switch     : Monday");
                break;
            case 2:
                System.out.println("5. switch     : Tuesday");
                break;
            case 3:
                System.out.println("5. switch     : Wednesday");
                break;
            default:
                System.out.println("5. switch     : another day");
        }

        // 6. ternary operator
        String result = (marks >= 40) ? "Pass" : "Fail";
        System.out.println("6. ternary    : " + result);
    }
}
```

**Sample output**

```text
1. if         : passed
2. if-else    : 72 is even
3. ladder     : First class
4. nested if  : eligible for the scholarship
5. switch     : Wednesday
6. ternary    : Pass
```

**Java 14+: arrow labels and switch expressions**

```java
int day = 6;
String type = switch (day) {            // switch used as an expression
    case 1, 2, 3, 4, 5 -> "Weekday";    // several labels, no break needed
    case 6, 7 -> "Weekend";
    default -> "Invalid day";
};
System.out.println(type);               // Weekend
```

The arrow form never falls through, and a switch expression must cover every possible value (here through `default`).

**if-else ladder vs switch**

| Basis | `else-if` ladder | `switch` |
|---|---|---|
| Tests | any boolean condition — ranges, several variables | equality of one expression with constants |
| Types | anything that yields a `boolean` | `byte`, `short`, `char`, `int`, wrappers, `String`, `enum` |
| Readability | better for ranges (`marks >= 75`) | better for many fixed values (menu choices) |
| Fall-through | never | yes in the classic form, unless `break` |
| Speed | conditions checked one by one | can jump straight to the matching case |

**Summary:** Java chooses between code paths with `if`, `if-else`, the `else-if` ladder, nested `if`, `switch` (classic and the Java 14 arrow form) and the ternary operator; use the `if` family for conditions and ranges, and `switch` for one value against fixed constants.

---

### C12. Arrays and the Arrays class

**Definition**

An array is a container object that holds a **fixed number** of values of a **single type**. Each element is accessed by an integer **index** starting at 0, and the number of elements is stored in the field `length`.

**Characteristics**

- Fixed size, set when the array is created.
- Homogeneous: every element has the same type (primitive or reference).
- Zero-based: valid indexes are `0` to `length - 1`; any other index throws `ArrayIndexOutOfBoundsException`.
- Arrays are objects, created on the heap; the array variable holds a reference.
- Elements get default values when the array is created.

```text
   int[] marks = {78, 85, 91, 66, 72};

    stack                     heap: array object (length = 5)
  +-------+        +------+------+------+------+------+
  | marks |------->|  78  |  85  |  91  |  66  |  72  |
  +-------+        +------+------+------+------+------+
           index:     0      1      2      3      4
```

**1. Declaration, creation and initialisation**

```java
int[] marks;                              // declaration (int marks[]; also works)
marks = new int[5];                       // creation: 5 elements, all 0
marks[0] = 78;                            // initialisation, element by element
int[] scores = {78, 85, 91, 66, 72};      // declare + create + initialise in one line
int[] copy = new int[] {1, 2, 3};         // anonymous-array syntax
int[][] matrix = new int[3][4];           // 2-D: 3 rows x 4 columns
int[][] jagged = {{1, 2}, {3, 4, 5}};     // jagged: rows of different lengths
```

Default element values after `new`:

| Element type | Default |
|---|---|
| `byte`, `short`, `int`, `long` | `0` |
| `float`, `double` | `0.0` |
| `char` | `'\u0000'` |
| `boolean` | `false` |
| any reference (`String`, objects) | `null` |

Arrays can also be filled in a loop (for example from `Scanner` input) or with `Arrays.fill`.

**2. Traversal**

- A `for` loop with an index — when the position is needed or elements are modified.
- The enhanced `for` (for-each) loop — the simplest read-only traversal.
- `Arrays.toString(arr)` — quick printing.
- Nested loops for 2-D arrays (`matrix.length` rows, `matrix[i].length` columns).

**3. Commonly used `java.util.Arrays` methods**

| Method | Purpose |
|---|---|
| `Arrays.toString(a)` | String such as `[1, 2, 3]` for printing |
| `Arrays.sort(a)` / `Arrays.sort(a, from, to)` | Sort ascending (whole array or a range) |
| `Arrays.binarySearch(a, key)` | Index of `key` in a **sorted** array; negative if absent |
| `Arrays.equals(a, b)` | Compare contents element by element |
| `Arrays.fill(a, value)` | Set every element to `value` |
| `Arrays.copyOf(a, newLength)` | Copy, truncated or padded with defaults |
| `Arrays.copyOfRange(a, from, to)` | Copy of a range (`to` is exclusive) |
| `Arrays.asList(...)` | Fixed-size `List` view of an object array |
| `Arrays.deepToString(m)` / `Arrays.deepEquals(m1, m2)` | Print / compare multi-dimensional arrays |

**Program**

```java
import java.util.Arrays;

public class ArrayBasicsDemo {
    public static void main(String[] args) {
        // 1. creation: fixed size, default values
        int[] scores = new int[5];
        System.out.println("created   : " + Arrays.toString(scores));

        // 2. initialisation
        scores[0] = 42;                                       // element by element
        System.out.println("set [0]   : " + Arrays.toString(scores));
        int[] marks = {78, 85, 91, 66, 72};                   // array literal
        String[] subjects = new String[] {"JAVA", "ADBMS", "RM"};   // anonymous-array syntax

        // 3. traversal
        System.out.print("for loop  :");
        for (int i = 0; i < marks.length; i++) {
            System.out.print(" " + marks[i]);
        }
        System.out.println();

        System.out.print("for-each  :");
        for (String subject : subjects) {
            System.out.print(" " + subject);
        }
        System.out.println();

        // 4. two-dimensional array
        int[][] matrix = { {1, 2, 3}, {4, 5, 6} };
        System.out.println("matrix    : " + Arrays.deepToString(matrix)
                + " (" + matrix.length + " rows x " + matrix[0].length + " cols)");

        // 5. java.util.Arrays methods
        int[] sorted = Arrays.copyOf(marks, marks.length);  // sort a copy, not the original
        Arrays.sort(sorted);
        System.out.println("sort      : " + Arrays.toString(sorted));
        System.out.println("search 85 : index " + Arrays.binarySearch(sorted, 85));
        System.out.println("equals    : " + Arrays.equals(marks, sorted));
        System.out.println("range 1-3 : " + Arrays.toString(Arrays.copyOfRange(sorted, 1, 4)));
        Arrays.fill(scores, 7);
        System.out.println("fill 7    : " + Arrays.toString(scores));
        System.out.println("asList    : " + Arrays.asList(subjects));
    }
}
```

**Sample output**

```text
created   : [0, 0, 0, 0, 0]
set [0]   : [42, 0, 0, 0, 0]
for loop  : 78 85 91 66 72
for-each  : JAVA ADBMS RM
matrix    : [[1, 2, 3], [4, 5, 6]] (2 rows x 3 cols)
sort      : [66, 72, 78, 85, 91]
search 85 : index 3
equals    : false
range 1-3 : [72, 78, 85]
fill 7    : [7, 7, 7, 7, 7]
asList    : [JAVA, ADBMS, RM]
```

`equals` is `false` because `sorted` holds the same numbers in a different order. The class demo [src/theory/arrays/ArrayDemo.java](src/theory/arrays/ArrayDemo.java) also shows bounds checking with `ArrayIndexOutOfBoundsException`.

**Advantages:** constant-time access by index, compact storage, easy traversal with loops, and ready-made utilities in `Arrays`.

**Limitations:** fixed size (use `ArrayList` for a growing list), one element type, costly insertion and deletion in the middle, and `==` / `equals()` compare references rather than contents.

**Summary:** Arrays are fixed-size, zero-indexed, same-type objects; create them with `new` or a literal, traverse them with `for` or for-each, and use `java.util.Arrays` to sort, search, compare, fill, copy and print them.

---

### C13. Garbage collection and automatic memory management

**Definition**

Garbage collection is the JVM's automatic memory management: it identifies objects on the heap that the running program can no longer reach and reclaims their memory. The programmer allocates objects with `new` but never frees them — Java has no `delete` or `free()`.

**JVM memory areas**

```text
 +------------------------------- JVM runtime memory -------------------------------+
 |  Method area (Metaspace) : class metadata, method code, runtime constant pool    |
 |                                                                                  |
 |  Heap (shared by all threads, managed by the GC) : every object and array        |
 |    +------------------ Young generation ------------------+  +----------------+  |
 |    |    Eden     |    Survivor S0    |    Survivor S1     |  | Old generation |  |
 |    +------------------------------------------------------+  +----------------+  |
 |                                                                                  |
 |  Stack (one per thread) : one frame per method call - local variables, refs      |
 |  PC register and native method stack (one per thread)                            |
 +----------------------------------------------------------------------------------+
```

Stack memory is released automatically when a method returns (its frame is popped); heap memory is reclaimed by the garbage collector.

**How Java manages memory automatically**

1. **Allocation** — `new` places the object in the heap, normally in *Eden* (part of the young generation); allocation is very fast.
2. **Finding live objects** — the collector starts from the **GC roots**: local variables and parameters in active stack frames, static fields of loaded classes, active threads and JNI references. An object reachable from a root through a chain of references is **live**; everything else is **garbage**.
3. **Mark** — traverse the object graph from the roots and mark every reachable object.
4. **Sweep** — reclaim the memory of the unmarked objects.
5. **Compact** — slide the live objects together to remove fragmentation, so later allocations stay fast.

**Generational collection**

Most objects die young (the *weak generational hypothesis*), so the heap is split by object age:

```text
  new objects
      |
      v
  +--------+  minor GC: live objects  +---------------+  survived several  +------------------+
  |  Eden  | -----------------------> |   Survivor    | -----------------> |  Old generation  |
  +--------+  are copied              |  S0  <-->  S1 |  minor GCs         | (major/full GC,  |
                                      +---------------+  (promotion)       |  less frequent)  |
  <------------------ young generation ----------------->                  +------------------+
```

- **Minor GC** — collects the young generation; frequent and quick.
- **Major / full GC** — collects the old generation (or the whole heap); rarer and slower, often with a longer *stop-the-world* pause.
- Objects that survive enough minor GCs (the tenuring threshold, at most 15 by default in HotSpot) are **promoted** to the old generation.
- Class metadata lives in **Metaspace** (native memory), which replaced PermGen in Java 8.

**When does an object become eligible for GC?**

```java
class Student {
    String name;
    Student partner;                     // used for the island of isolation
    Student(String name) {
        this.name = name;
    }
}
```

```java
Student s1 = new Student("Ross");
s1 = null;                               // 1. nulling: "Ross" is now unreachable

Student s2 = new Student("Rachel");
s2 = new Student("Monica");              // 2. reassigning: "Rachel" lost its only reference

Student a = new Student("Joey");         // 3. island of isolation
Student b = new Student("Chandler");
a.partner = b;                           //    the two objects refer to each other ...
b.partner = a;
a = null;                                //    ... but no outside reference reaches them
b = null;
```

4. An object created **inside a method** becomes eligible when the method returns, because its only reference (a local variable) disappears.
5. An **anonymous object** such as `new Student("Phoebe");` is eligible as soon as the statement finishes.

```text
     stack                       heap
  +---------+     +------------+  partner  +------------+
  | a: null |     |    Joey    | --------> |  Chandler  |
  | b: null |     |            | <-------- |            |
  +---------+     +------------+  partner  +------------+
  No GC root reaches either object, so both are eligible
  even though they still refer to each other.
```

**Requesting a collection:** `System.gc()` or `Runtime.getRuntime().gc()` only *requests* a collection; the JVM may ignore it (for example when started with `-XX:+DisableExplicitGC`). See [B14](#b14-why-systemgc-does-not-guarantee-collection).

**Garbage collectors in HotSpot**

| Collector | Option | Notes |
|---|---|---|
| Serial | `-XX:+UseSerialGC` | single-threaded; small heaps |
| Parallel | `-XX:+UseParallelGC` | many threads; maximum throughput |
| G1 (Garbage-First) | `-XX:+UseG1GC` | region-based; **the default since Java 9** |
| ZGC | `-XX:+UseZGC` | very short pauses, even with very large heaps |

Cleanup of non-memory resources (files, sockets) should never be left to the garbage collector: `finalize()` is deprecated — use try-with-resources (see [C14](#c14-finalize-and-why-it-is-not-recommended)).

**Advantages:** no manual deallocation, so no dangling pointers, double frees or forgotten `free()` calls; simpler, safer code and faster development.

**Limitations:** GC uses CPU time, causes (usually short) pauses, runs at unpredictable times, and memory can still leak if references are kept unintentionally (static collections, caches, listeners).

**Summary:** The JVM allocates objects on the heap and its garbage collector automatically reclaims those no longer reachable from the GC roots, using mark-sweep-compact on a generational (young/old) heap; a program can only request a collection with `System.gc()`.

---

### C14. `finalize()` and why it is not recommended

**Definition**

`finalize()` is a method of `java.lang.Object`:

```text
@Deprecated(since="9", forRemoval=true)
protected void finalize() throws Throwable
```

The garbage collector calls it on an object when it determines that there are no more references to the object, before reclaiming the memory. A class could override it to release non-memory resources such as files, sockets or native memory — similar in intent to a C++ destructor, but with no guarantee of *when*, or even *whether*, it runs.

**Historical syntax — deprecated, do not use in new code**

```java
class LegacyResource {
    @Override
    protected void finalize() throws Throwable {   // deprecated for removal
        try {
            // release the resource here
        } finally {
            super.finalize();                      // not chained automatically
        }
    }
}
```

On JDK 25 this compiles only with the warning `[removal] finalize() in Object has been deprecated and marked for removal`.

**Life cycle of an object with a finalizer**

```text
 created --> reachable --> unreachable --> queued for finalization
                                                      |   finalizer thread: unknown delay,
                                                      v   possibly never
                                               finalize() runs
                                                      |   at a later GC, unless the object
                                                      v   was resurrected
                                              memory reclaimed
```

**Why it is not recommended**

1. **No guarantee that it runs** — the program may end first or the GC may never run; the Javadoc warns it may be called "only after an indefinite delay".
2. **Unpredictable timing** — scarce resources such as file handles or database connections can run out while objects wait to be finalized.
3. **Unspecified thread and order** — it runs on a JVM-chosen thread, in no particular order, inviting concurrency bugs.
4. **Resurrection** — `finalize()` can store `this` somewhere reachable and bring a "dead" object back to life.
5. **Exceptions are silently ignored** — an uncaught exception just stops that object's finalization.
6. **Performance cost** — objects with finalizers are slower to create and need at least two GC cycles to be reclaimed; a slow finalizer can back up the queue until the program runs out of memory.
7. **Security risk** — "finalizer attacks" use a subclass's `finalize()` to capture a partially constructed object.
8. **Not chained** — unlike constructors, `super.finalize()` has to be called by hand.

The Javadoc's verdict: finalization "can lead to problems with security, performance, and reliability".

**Status today**

| Java version | Change |
|---|---|
| 9 | `Object.finalize()` deprecated |
| 18 | JEP 421 — finalization **deprecated for removal**; `--finalization=disabled` added for testing; `System.runFinalization()` and `Runtime.runFinalization()` also deprecated for removal |
| 25 (LTS) | Still present and enabled by default, but scheduled for removal in a future release |

**Modern alternatives**

| Alternative | Since | How it works |
|---|---|---|
| `AutoCloseable` + **try-with-resources** | Java 7 | `close()` is called automatically, at a known point, when the `try` block ends — even if an exception is thrown. **First choice.** |
| Explicit `close()` in a `finally` block | Java 1.0 | Manual but deterministic cleanup |
| `java.lang.ref.Cleaner` | Java 9 | Registers a cleanup action that runs at most once — when `clean()` is called, or after the object becomes unreachable (a safety net only) |

**Program — deterministic cleanup with try-with-resources**

```java
class FileResource implements AutoCloseable {
    private final String name;

    FileResource(String name) {
        this.name = name;
        System.out.println("Opened " + name);
    }

    void read() {
        System.out.println("Reading " + name);
    }

    @Override
    public void close() {                      // replaces finalize(): runs at a known point
        System.out.println("Closed " + name);
    }
}

public class CleanupDemo {
    public static void main(String[] args) {
        try (FileResource file = new FileResource("marks.txt")) {
            file.read();
        }                                      // close() is called automatically here
        System.out.println("After the try block - resource already released");
    }
}
```

**Sample output**

```text
Opened marks.txt
Reading marks.txt
Closed marks.txt
After the try block - resource already released
```

**finalize() vs try-with-resources**

| Basis | `finalize()` | try-with-resources |
|---|---|---|
| Triggered by | The garbage collector | The end of the `try` block |
| When | Unpredictable, possibly never | Immediately, every time |
| Thread | A finalizer thread | The current thread |
| Exceptions | Silently ignored | Propagated (extra ones kept as *suppressed*) |
| Status | Deprecated for removal | Recommended |

**Summary:** `finalize()` was a GC-driven cleanup hook, but it may never run, runs at an unknown time on an unknown thread, harms performance and security, and has been deprecated for removal since Java 18 — release resources with try-with-resources (`AutoCloseable`) and use `Cleaner` only as a safety net.

---

### Multiple Choice Questions

Answers exactly as given in the question bank, each with a one-line reason.

| Q | Answer | Why |
|---|---|---|
| 1 | B. `new` | `new` allocates the object on the heap and calls the constructor; `class` only declares the blueprint |
| 2 | C. Abstraction | Abstraction exposes *what* an object does and hides *how* (abstract classes, interfaces) |
| 3 | A. Encapsulation | `private` fields reachable only through getters/setters protect the data |
| 4 | B. `extends` | A class extends a class; `implements` is for interfaces; `inherits` and `superclass` are not keywords |
| 5 | B. Method overloading | The compiler picks the overload from the arguments; overriding is resolved at runtime |
| 6 | C. `studentName` | `1student` starts with a digit, `student name` has a space, `class` is a keyword |
| 7 | B. `char` | 16-bit primitive holding one character; `String` holds a sequence; `character` and `text` are not types |
| 8 | C. `&&` | Logical (short-circuit) AND; `\|\|` is OR, `!` is NOT, `&` is bitwise AND (a non-short-circuit AND on booleans) |
| 9 | C. 0 | The first element is `arr[0]`, the last is `arr[arr.length - 1]` |
| 10 | B. `Arrays.sort()` | Sorts in ascending order, in place; the other three methods do not exist |
| 11 | C. `length` | Arrays have a `length` field; `length()` is a `String` method |
| 12 | A. `switch` | Matches one expression against several constant `case` values |
| 13 | B. JVM | The JVM interprets / JIT-compiles bytecode; the JDK is the development kit (`javac` and tools) |
| 14 | C. `finalize()` | Called by the GC before reclaiming an object — deprecated since Java 9, for removal since Java 18 |
| 15 | C. It requests the JVM to perform garbage collection. | Only a hint; the JVM may delay or ignore it |

---

### Practical Programming Exercises

Each program is complete: save it in a file named after its `public class` (for example `BookDemo.java`), then compile with `javac BookDemo.java` and run with `java BookDemo`. Values are hard-coded so that the output is reproducible; only P9 reads from the keyboard, because a menu needs a user's choice.

### P1. Class and object with details

```java
class Book {
    String title;                       // data members (state)
    String author;
    double price;

    void display() {                    // member method (behaviour)
        System.out.println("Title  : " + title);
        System.out.println("Author : " + author);
        System.out.println("Price  : Rs. " + price);
    }
}

public class BookDemo {
    public static void main(String[] args) {
        Book b1 = new Book();           // object 1
        b1.title = "Java: The Complete Reference";
        b1.author = "Herbert Schildt";
        b1.price = 899.0;

        Book b2 = new Book();           // object 2: same class, its own data
        b2.title = "Head First Java";
        b2.author = "Kathy Sierra & Bert Bates";
        b2.price = 650.0;

        System.out.println("Book 1 details:");
        b1.display();
        System.out.println("Book 2 details:");
        b2.display();
    }
}
```

**Sample output**

```text
Book 1 details:
Title  : Java: The Complete Reference
Author : Herbert Schildt
Price  : Rs. 899.0
Book 2 details:
Title  : Head First Java
Author : Kathy Sierra & Bert Bates
Price  : Rs. 650.0
```

`Book` is the class; `b1` and `b2` are two objects created with `new`, each holding its own field values, and `display()` is called on each with the dot operator. A similar lab program: [src/practical/lab1/q4.java](src/practical/lab1/q4.java).

---

### P2. Encapsulation with getters and setters

```java
class Employee {
    private int id;                     // private: hidden from other classes
    private String name;
    private double salary;

    // setters: the only way to change the data, with validation
    public void setId(int id) {
        if (id > 0) {
            this.id = id;
        } else {
            System.out.println("Invalid id: " + id);
        }
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSalary(double salary) {
        if (salary >= 0) {
            this.salary = salary;
        } else {
            System.out.println("Invalid salary: " + salary);
        }
    }

    // getters: read access to the data
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }
}

public class EncapsulationDemo {
    public static void main(String[] args) {
        Employee e = new Employee();
        e.setId(101);
        e.setName("Dwight Schrute");
        e.setSalary(65000);

        e.setSalary(-5000);             // rejected by the setter
        // e.salary = -5000;           // error: salary has private access in Employee

        System.out.println("ID     : " + e.getId());
        System.out.println("Name   : " + e.getName());
        System.out.println("Salary : " + e.getSalary());
    }
}
```

**Sample output**

```text
Invalid salary: -5000.0
ID     : 101
Name   : Dwight Schrute
Salary : 65000.0
```

The fields are `private`, so `main` can reach them only through the public getters and setters — and the setter refuses the negative salary.

---

### P3. Inheritance using `extends`

```java
class Vehicle {                                 // superclass
    protected String brand;
    protected int wheels;

    Vehicle(String brand, int wheels) {
        this.brand = brand;
        this.wheels = wheels;
    }

    void start() {
        System.out.println(brand + " started");
    }

    void showVehicle() {
        System.out.println("Brand  : " + brand);
        System.out.println("Wheels : " + wheels);
    }
}

class Car extends Vehicle {                     // subclass: Car IS-A Vehicle
    private String model;

    Car(String brand, String model) {
        super(brand, 4);                        // calls the superclass constructor
        this.model = model;
    }

    void showCar() {
        showVehicle();                          // inherited method
        System.out.println("Model  : " + model);
    }
}

public class InheritanceDemo {
    public static void main(String[] args) {
        Car car = new Car("Dodge", "Charger");
        car.start();                            // inherited from Vehicle
        car.showCar();                          // defined in Car
    }
}
```

**Sample output**

```text
Dodge started
Brand  : Dodge
Wheels : 4
Model  : Charger
```

`Car` reuses `brand`, `wheels`, `start()` and `showVehicle()` from `Vehicle` and adds `model` and `showCar()`; `super(brand, 4)` runs the superclass constructor first.

---

### P4. Method overloading

```java
class AreaCalculator {
    double area(double radius) {                    // circle: one double
        return Math.PI * radius * radius;
    }

    double area(double length, double breadth) {    // rectangle: two doubles
        return length * breadth;
    }

    int area(int side) {                            // square: one int
        return side * side;
    }
}

public class OverloadingDemo {
    public static void main(String[] args) {
        AreaCalculator calc = new AreaCalculator();
        System.out.printf("Circle    (r = 7.0)   : %.2f%n", calc.area(7.0));
        System.out.println("Rectangle (8.0 x 4.5) : " + calc.area(8.0, 4.5));
        System.out.println("Square    (side = 6)  : " + calc.area(6));
    }
}
```

**Sample output**

```text
Circle    (r = 7.0)   : 153.94
Rectangle (8.0 x 4.5) : 36.0
Square    (side = 6)  : 36
```

All three methods are called `area`; the compiler chooses one from the arguments — two arguments select the rectangle version, `6` (an `int`) selects `area(int)` and `7.0` (a `double`) selects `area(double)`.

---

### P5. Method overriding

```java
class Payment {
    void pay(double amount) {
        System.out.println("Payment of Rs. " + amount);
    }
}

class CardPayment extends Payment {
    @Override
    void pay(double amount) {                   // same signature as in Payment
        double fee = amount * 0.02;
        System.out.println("Card payment of Rs. " + amount + " + fee Rs. " + fee);
    }
}

class UpiPayment extends Payment {
    @Override
    void pay(double amount) {
        System.out.println("UPI payment of Rs. " + amount + " (no fee)");
    }
}

public class OverridingDemo {
    public static void main(String[] args) {
        Payment p = new Payment();
        p.pay(500);                             // Payment's version

        p = new CardPayment();                  // parent reference, child object
        p.pay(500);                             // CardPayment's version, chosen at runtime

        p = new UpiPayment();
        p.pay(500);                             // UpiPayment's version
    }
}
```

**Sample output**

```text
Payment of Rs. 500.0
Card payment of Rs. 500.0 + fee Rs. 10.0
UPI payment of Rs. 500.0 (no fee)
```

The overriding methods keep the exact signature `void pay(double)`; `@Override` makes the compiler check that. To run the parent's version as well, call `super.pay(amount)` inside the override — as in the lab program [src/practical/lab3/q5.java](src/practical/lab3/q5.java).

---

### P6. Positive, negative or zero

```java
public class NumberCheck {
    static void check(int num) {
        if (num > 0) {
            System.out.println(num + " is positive");
        } else if (num < 0) {
            System.out.println(num + " is negative");
        } else {
            System.out.println(num + " is zero");
        }
    }

    public static void main(String[] args) {
        check(25);
        check(-7);
        check(0);
    }
}
```

**Sample output**

```text
25 is positive
-7 is negative
0 is zero
```

Calling `check()` with three values exercises every branch of the if-else chain.

---

### P7. Largest of three numbers

```java
public class LargestOfThree {
    public static void main(String[] args) {
        int a = 25, b = 78, c = 43;
        int largest;

        if (a >= b && a >= c) {
            largest = a;
        } else if (b >= a && b >= c) {
            largest = b;
        } else {
            largest = c;
        }
        System.out.println("Numbers: " + a + ", " + b + ", " + c);
        System.out.println("Largest (if-else) : " + largest);

        // the same result with the ternary operator and with Math.max
        int big = (a > b) ? (a > c ? a : c) : (b > c ? b : c);
        System.out.println("Largest (ternary) : " + big);
        System.out.println("Largest (Math.max): " + Math.max(a, Math.max(b, c)));
    }
}
```

**Sample output**

```text
Numbers: 25, 78, 43
Largest (if-else) : 78
Largest (ternary) : 78
Largest (Math.max): 78
```

Using `>=` handles ties: if two numbers are equal and largest, either branch gives the correct value.

---

### P8. Grade using an else-if ladder

```java
public class GradeDemo {
    static String grade(int marks) {
        if (marks < 0 || marks > 100) {
            return "Invalid marks";
        } else if (marks >= 90) {
            return "A+";
        } else if (marks >= 75) {
            return "A";
        } else if (marks >= 60) {
            return "B";
        } else if (marks >= 50) {
            return "C";
        } else if (marks >= 40) {
            return "D";
        } else {
            return "F (Fail)";
        }
    }

    public static void main(String[] args) {
        int[] samples = {95, 82, 67, 55, 43, 28, 105};
        for (int marks : samples) {
            System.out.printf("%3d marks -> %s%n", marks, grade(marks));
        }
    }
}
```

**Sample output**

```text
 95 marks -> A+
 82 marks -> A
 67 marks -> B
 55 marks -> C
 43 marks -> D
 28 marks -> F (Fail)
105 marks -> Invalid marks
```

The ladder is tested top to bottom and stops at the first true condition, so each test only needs a lower bound. The grade boundaries are a sample scale — use the one given in the exam question.

---

### P9. Menu using `switch`

```java
import java.util.Scanner;

public class MenuDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter two numbers: ");
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println("===== MENU =====");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        System.out.print("Enter your choice (1-4): ");
        int choice = sc.nextInt();

        switch (choice) {
            case 1:
                System.out.println(a + " + " + b + " = " + (a + b));
                break;
            case 2:
                System.out.println(a + " - " + b + " = " + (a - b));
                break;
            case 3:
                System.out.println(a + " * " + b + " = " + (a * b));
                break;
            case 4:
                if (b != 0) {
                    System.out.println(a + " / " + b + " = " + ((double) a / b));
                } else {
                    System.out.println("Cannot divide by zero");
                }
                break;
            default:
                System.out.println("Invalid choice! Enter a number from 1 to 4.");
        }
        sc.close();
    }
}
```

**Sample output** (interactive run: the user types `20 5`, then `3`)

```text
Enter two numbers: 20 5
===== MENU =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter your choice (1-4): 3
20 * 5 = 100
```

Each `case` ends with `break` to stop fall-through, and `default` catches any other number. To show the menu repeatedly, wrap it in a `do-while` loop with an *Exit* option, as in the lab program [src/practical/lab3/q3.java](src/practical/lab3/q3.java).

---

### P10. Store and display five integers

```java
public class ArrayStoreDisplay {
    public static void main(String[] args) {
        int[] values = new int[5];          // room for 5 ints, all 0 at first

        // store
        values[0] = 10;
        values[1] = 25;
        values[2] = 30;
        values[3] = 45;
        values[4] = 50;

        // display with an index
        System.out.println("Array elements:");
        for (int i = 0; i < values.length; i++) {
            System.out.println("values[" + i + "] = " + values[i]);
        }

        // display with for-each
        System.out.print("Using for-each:");
        for (int v : values) {
            System.out.print(" " + v);
        }
        System.out.println();
    }
}
```

**Sample output**

```text
Array elements:
values[0] = 10
values[1] = 25
values[2] = 30
values[3] = 45
values[4] = 50
Using for-each: 10 25 30 45 50
```

To read the five values from the keyboard instead, create a `Scanner` and use `values[i] = sc.nextInt();` inside a `for` loop. The class demo [src/theory/arrays/Array.java](src/theory/arrays/Array.java) follows the same steps.

---

### P11. Largest element in an array

```java
import java.util.Arrays;

public class LargestInArray {
    public static void main(String[] args) {
        int[] arr = {45, 12, 89, 33, 67};
        int max = arr[0];                   // assume the first element is the largest
        int position = 0;

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {             // found a bigger element
                max = arr[i];
                position = i;
            }
        }

        System.out.println("Array   : " + Arrays.toString(arr));
        System.out.println("Largest : " + max + " (at index " + position + ")");
    }
}
```

**Sample output**

```text
Array   : [45, 12, 89, 33, 67]
Largest : 89 (at index 2)
```

Starting `max` at `arr[0]` (not at `0`) keeps the program correct even when every element is negative.

---

### P12. Sum and average of array elements

```java
import java.util.Arrays;

public class SumAverage {
    public static void main(String[] args) {
        int[] marks = {78, 85, 91, 66, 72};
        int sum = 0;

        for (int m : marks) {
            sum += m;
        }
        double average = (double) sum / marks.length;   // cast avoids integer division

        System.out.println("Elements : " + Arrays.toString(marks));
        System.out.println("Sum      : " + sum);
        System.out.println("Average  : " + average);
    }
}
```

**Sample output**

```text
Elements : [78, 85, 91, 66, 72]
Sum      : 392
Average  : 78.4
```

Without the `(double)` cast, `392 / 5` would be integer division and give `78`.

---

### P13. Sorting with `Arrays.sort()`

```java
import java.util.Arrays;
import java.util.Collections;

public class SortDemo {
    public static void main(String[] args) {
        int[] numbers = {42, 7, 19, 73, 5, 28};
        System.out.println("Before : " + Arrays.toString(numbers));
        Arrays.sort(numbers);                            // ascending, in place
        System.out.println("After  : " + Arrays.toString(numbers));

        String[] names = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"};
        Arrays.sort(names);                              // alphabetical order
        System.out.println("Names  : " + Arrays.toString(names));

        Integer[] desc = {42, 7, 19, 73, 5, 28};        // wrapper type needed for a Comparator
        Arrays.sort(desc, Collections.reverseOrder());   // descending order
        System.out.println("Desc   : " + Arrays.toString(desc));
    }
}
```

**Sample output**

```text
Before : [42, 7, 19, 73, 5, 28]
After  : [5, 7, 19, 28, 42, 73]
Names  : [Chandler, Joey, Monica, Phoebe, Rachel, Ross]
Desc   : [73, 42, 28, 19, 7, 5]
```

`Arrays.sort()` changes the original array. Strings are sorted by Unicode value, so uppercase letters come before lowercase ones (`"Zebra"` sorts before `"apple"`).

---

### P14. Comparing arrays with `Arrays.equals()`

```java
import java.util.Arrays;

public class CompareArrays {
    public static void main(String[] args) {
        int[] a = {10, 20, 30, 40};
        int[] b = {10, 20, 30, 40};
        int[] c = {40, 30, 20, 10};

        System.out.println("a == b              : " + (a == b));             // compares references
        System.out.println("a.equals(b)         : " + a.equals(b));          // also references
        System.out.println("Arrays.equals(a, b) : " + Arrays.equals(a, b));  // compares contents
        System.out.println("Arrays.equals(a, c) : " + Arrays.equals(a, c));  // different order

        Arrays.sort(c);
        System.out.println("After sorting c     : " + Arrays.equals(a, c));
    }
}
```

**Sample output**

```text
a == b              : false
a.equals(b)         : false
Arrays.equals(a, b) : true
Arrays.equals(a, c) : false
After sorting c     : true
```

`a` and `b` are two different objects, so `==` and `equals()` (inherited from `Object`) are `false`; `Arrays.equals()` compares length and elements position by position. Use `Arrays.deepEquals()` for 2-D arrays.

---

### P15. Object eligible for garbage collection

```java
class Student {
    String name;
    Student partner;                         // used for the island-of-isolation case

    Student(String name) {
        this.name = name;
        System.out.println("Created " + name);
    }
}

public class GcEligibilityDemo {

    static void createLocalObject() {
        Student temp = new Student("Gunther");       // local reference
        System.out.println("Inside method: using " + temp.name);
    }                                                // temp goes out of scope here

    public static void main(String[] args) {
        // 1. Nulling the reference
        Student s1 = new Student("Ross");
        s1 = null;
        System.out.println("1. s1 = null        -> Ross is eligible for GC");

        // 2. Reassigning the reference
        Student s2 = new Student("Rachel");
        s2 = new Student("Monica");
        System.out.println("2. s2 reassigned    -> Rachel is eligible for GC");

        // 3. Object created inside a method
        createLocalObject();
        System.out.println("3. method returned  -> Gunther is eligible for GC");

        // 4. Island of isolation
        Student a = new Student("Joey");
        Student b = new Student("Chandler");
        a.partner = b;                               // a -> b
        b.partner = a;                               // b -> a
        a = null;
        b = null;                                    // nothing outside reaches the pair
        System.out.println("4. a = b = null     -> Joey and Chandler are eligible for GC");

        // 5. Anonymous object
        new Student("Phoebe");                       // reference never stored
        System.out.println("5. anonymous object -> Phoebe is eligible for GC");

        System.out.println("Still reachable: " + s2.name);

        System.gc();   // only a REQUEST: the JVM may collect now, later, or never
        System.out.println("System.gc() requested - nothing above depends on it running");
    }
}
```

**Sample output**

```text
Created Ross
1. s1 = null        -> Ross is eligible for GC
Created Rachel
Created Monica
2. s2 reassigned    -> Rachel is eligible for GC
Created Gunther
Inside method: using Gunther
3. method returned  -> Gunther is eligible for GC
Created Joey
Created Chandler
4. a = b = null     -> Joey and Chandler are eligible for GC
Created Phoebe
5. anonymous object -> Phoebe is eligible for GC
Still reachable: Monica
System.gc() requested - nothing above depends on it running
```

*Eligible* does not mean *collected*: the program can only make objects unreachable and then request a collection. That is why it deliberately prints nothing from a `finalize()` method — `finalize()` is deprecated and may never run, so any output from it would be unreliable.

---

## Quick revision sheet

**OOP pillars**

| Pillar | One-liner | Java mechanism |
|---|---|---|
| Abstraction | Show *what*, hide *how* | `abstract` classes, interfaces |
| Encapsulation | Bundle data with methods and hide the data | `private` fields + getters/setters |
| Inheritance | Reuse a class; "is-a" | `extends` (classes), `implements` (interfaces) |
| Polymorphism | One name, many forms | Overloading (compile time), overriding (runtime) |

Class = blueprint; object = instance created with `new` (state + behaviour + identity). Java allows single, multilevel and hierarchical inheritance with classes; multiple and hybrid only through interfaces.

**Primitive types**

| Type | Size | Default | Literal |
|---|---|---|---|
| `byte` | 8-bit | `0` | `100` |
| `short` | 16-bit | `0` | `30000` |
| `int` | 32-bit | `0` | `150000` |
| `long` | 64-bit | `0L` | `9000000000L` |
| `float` | 32-bit | `0.0f` | `3.14f` |
| `double` | 64-bit | `0.0d` | `3.14` |
| `char` | 16-bit (UTF-16) | `'\u0000'` | `'A'` |
| `boolean` | JVM-dependent | `false` | `true` |

Defaults apply only to fields and array elements; local variables must be assigned before use.

**Operator categories**

| Category | Operators |
|---|---|
| Arithmetic | `+ - * / %` |
| Unary | `+ - ++ -- ! ~` |
| Relational | `== != > < >= <=` |
| Logical | `&& \|\| !` (`&&` and `\|\|` short-circuit) |
| Bitwise / shift | `& \| ^ ~` / `<< >> >>>` |
| Assignment | `= += -= *= /= %=` … |
| Ternary | `cond ? a : b` |
| Type check | `instanceof` |

**Decision making:** `if` · `if-else` · `else-if` ladder · nested `if` · `switch` (on `byte`/`short`/`char`/`int`, wrappers, `String`, `enum`; `break` stops fall-through; arrow form and switch expressions since Java 14) · ternary `?:`.

**Arrays and `java.util.Arrays`**

| Method | Remember |
|---|---|
| `toString(a)` | prints `[1, 2, 3]` |
| `sort(a)` | ascending, in place |
| `binarySearch(a, k)` | sorted array only; `-(insertion point) - 1` if absent |
| `equals(a, b)` | compares contents (`==` compares references) |
| `fill(a, v)` | every element becomes `v` |
| `copyOf(a, n)` | truncates or pads with defaults |
| `copyOfRange(a, from, to)` | `to` is exclusive |
| `asList(...)` | fixed-size `List` view |
| `deepToString(m)` | for 2-D arrays |

Indexes start at 0; `arr.length` is a field (`String` has the method `length()`); a bad index throws `ArrayIndexOutOfBoundsException`.

**Garbage collection facts**

- The heap is managed automatically; Java has no `delete` or `free()`.
- An object is **eligible** when no GC root can reach it: reference set to `null`, reference reassigned, method-local object after the method returns, island of isolation, anonymous object.
- Mark → sweep → compact on a generational heap: young generation (Eden + two survivor spaces, minor GC) and old generation (major/full GC); G1 has been the default collector since Java 9.
- `System.gc()` = `Runtime.getRuntime().gc()` = a **request** only; `-XX:+DisableExplicitGC` turns it into a no-op.
- `finalize()`: deprecated in Java 9, **deprecated for removal** in Java 18 (JEP 421), may never run — use try-with-resources (`AutoCloseable`) or `Cleaner`.

**Also remember:** JDK (compiler and tools) ⊃ JRE (class libraries) ⊃ JVM (runs bytecode) · a public class must live in a file of the same name · `L` suffix for `long` literals, `f` for `float` · `_` alone is a keyword since Java 9 · 51 reserved keywords, with `goto` and `const` unused · `true`, `false`, `null` are literals, not keywords.
