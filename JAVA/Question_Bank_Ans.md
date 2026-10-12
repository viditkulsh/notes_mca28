# Java — Answers to Question Bank

Structured, exam-oriented answers to every item in [Question_Bank.md](Question_Bank.md). Numbering matches the question bank exactly: **T3** answers theory question 3 and **P3** answers program 3.

Depth follows the question. T1–T5 are full long answers (definition → explanation → program → comparison → summary). T6 and T7 ("State the purpose") are short notes, and T8–T17 are about 5-mark answers. Every complete program was compiled and run on JDK 25, and every **Sample output** or **Sample run** block is the real output of that run; in a sample run, what the user typed appears right after each prompt. Apart from the one snippet marked *Java 16+*, all code also compiles with `javac --release 8`, so it works on older lab JDKs too.

> Student-written notes. The question bank is itself student-transcribed, so check each question against the copy given in class, and cross-check definitions with the prescribed textbook before the exam. Unit 1 answers are in [JAVA_UNIT1_Question_Bank_Ans.md](JAVA_UNIT1_Question_Bank_Ans.md).

## Contents

- [Theory Questions](#theory-questions)
  - [T1. Method overloading vs method overriding](#t1-method-overloading-vs-method-overriding)
  - [T2. The `this`, `super` and `final` keywords](#t2-the-this-super-and-final-keywords)
  - [T3. Upcasting, downcasting and dynamic method dispatch](#t3-upcasting-downcasting-and-dynamic-method-dispatch)
  - [T4. Abstract classes and abstract methods](#t4-abstract-classes-and-abstract-methods)
  - [T5. String, String array, StringBuffer and wrapper classes](#t5-string-string-array-stringbuffer-and-wrapper-classes)
  - [T6. Purpose of `this` and `super`](#t6-purpose-of-this-and-super)
  - [T7. Purpose of `static` and `final`](#t7-purpose-of-static-and-final)
  - [T8. Access modifiers](#t8-access-modifiers)
  - [T9. User-defined packages](#t9-user-defined-packages)
  - [T10. Interfaces and their advantages](#t10-interfaces-and-their-advantages)
  - [T11. Abstract class vs interface](#t11-abstract-class-vs-interface)
  - [T12. Adapter classes](#t12-adapter-classes)
  - [T13. Types of exceptions](#t13-types-of-exceptions)
  - [T14. `throw` vs `throws`](#t14-throw-vs-throws)
  - [T15. `try`, `catch` and `finally`](#t15-try-catch-and-finally)
  - [T16. Nested `try` blocks and multiple `catch` statements](#t16-nested-try-blocks-and-multiple-catch-statements)
  - [T17. User-defined exceptions](#t17-user-defined-exceptions)
- [Programs](#programs)
  - [P1. `Manager` interface implemented by `HRManager`](#p1-manager-interface-implemented-by-hrmanager)
  - [P2. Top two products by price](#p2-top-two-products-by-price)
  - [P3. `Student` and `Marks` using inheritance](#p3-student-and-marks-using-inheritance)
  - [P4. `InvalidEmailException` for an email address](#p4-invalidemailexception-for-an-email-address)
  - [P5. `Bank` class with constructors, deposit and withdraw](#p5-bank-class-with-constructors-deposit-and-withdraw)
  - [P6. Staff member with the highest salary](#p6-staff-member-with-the-highest-salary)
  - [P7. Abstract `Order` with `PurchaseOrder` and `SalesOrder`](#p7-abstract-order-with-purchaseorder-and-salesorder)
  - [P8. `InSufficientFundException` with the additional amount required](#p8-insufficientfundexception-with-the-additional-amount-required)
  - [P9. Abstract `Shape` and dynamic method dispatch](#p9-abstract-shape-and-dynamic-method-dispatch)
  - [P10. `Employee`, `Manager` and `Developer`: overriding, casting and `super`](#p10-employee-manager-and-developer-overriding-casting-and-super)
  - [P11. User-defined package `mypackage`](#p11-user-defined-package-mypackage)
  - [P12. `Vehicle` interface implemented by `Car`](#p12-vehicle-interface-implemented-by-car)
  - [P13. `Printable` and `Showable` implemented by `Document`](#p13-printable-and-showable-implemented-by-document)
  - [P14. Adapter class for `StudentActivity`](#p14-adapter-class-for-studentactivity)
  - [P15. Access modifiers across packages](#p15-access-modifiers-across-packages)
  - [P16. `try`, `catch` and `finally` for an arithmetic exception](#p16-try-catch-and-finally-for-an-arithmetic-exception)
  - [P17. Multiple `catch` statements](#p17-multiple-catch-statements)
  - [P18. Nested `try` blocks at different levels](#p18-nested-try-blocks-at-different-levels)
  - [P19. Validating an email with `InvalidEmailException`](#p19-validating-an-email-with-invalidemailexception)
  - [P20. `InSufficientFundException` on withdrawal](#p20-insufficientfundexception-on-withdrawal)
- [Quick revision sheet](#quick-revision-sheet)

---

## Theory Questions

### T1. Method overloading vs method overriding

**Definition**

- **Method overloading** means defining two or more methods with the **same name** in the **same class** but with **different parameter lists** (a different number, type or order of parameters). The compiler picks the method to call from the arguments, so overloading is **compile-time (static) polymorphism**.
- **Method overriding** means a **subclass** giving its own body to a method it **inherited** from its superclass, keeping the **same name, the same parameters and the same (or covariant) return type**. The JVM picks the version to run from the actual object, so overriding is **runtime (dynamic) polymorphism**.

**1. Method overloading**

```java
class AreaCalculator {
    double area(double radius) {                    // circle
        return Math.PI * radius * radius;
    }

    double area(double length, double breadth) {    // rectangle: different NUMBER of parameters
        return length * breadth;
    }

    int area(int side) {                            // square: different TYPE of parameter
        return side * side;
    }
}

public class OverloadingDemo {
    public static void main(String[] args) {
        AreaCalculator calc = new AreaCalculator();
        System.out.printf("Circle (r = 7.0)      : %.2f%n", calc.area(7.0));   // area(double)
        System.out.println("Rectangle (4.0 x 5.5) : " + calc.area(4.0, 5.5));  // area(double, double)
        System.out.println("Square (side = 6)     : " + calc.area(6));         // area(int)
    }
}
```

**Sample output**

```text
Circle (r = 7.0)      : 153.94
Rectangle (4.0 x 5.5) : 22.0
Square (side = 6)     : 36
```

The three calls look alike, but `javac` binds each one to a different method by matching the argument list: `area(7.0)` → `area(double)`, `area(4.0, 5.5)` → `area(double, double)`, `area(6)` → `area(int)`.

Rules of overloading:

- The name must be the same and the parameter list must differ in the **number**, **type** or **order** of parameters.
- The return type may be the same or different, but a different return type **alone** is not enough:

```java
double area(double radius) { ... }
int area(double radius) { ... }     // error: method area(double) is already defined in class AreaCalculator
```

- Access modifiers and `throws` clauses may differ freely.
- `static`, `final` and `private` methods can be overloaded, and so can constructors and even `main()` (the JVM still starts only `main(String[])`).
- With no exact match, Java widens the argument (`byte → short → int → long → float → double`). For example, there is no `area(long)`, so `calc.area(6L)` widens `6L` to `double` and calls `area(double)`.

**2. Method overriding**

```java
class Account {
    double interestRate() {
        return 3.0;
    }
}

class SavingsAccount extends Account {
    @Override
    double interestRate() {                         // same signature, new body
        return 4.0;
    }
}

class FixedDeposit extends Account {
    @Override
    double interestRate() {
        return super.interestRate() + 4.0;          // can still reuse the parent's version
    }
}

public class OverridingDemo {
    public static void main(String[] args) {
        Account acc;                                // superclass reference

        acc = new Account();
        System.out.println("Account        : " + acc.interestRate() + "%");   // Account's version

        acc = new SavingsAccount();                 // upcasting
        System.out.println("SavingsAccount : " + acc.interestRate() + "%");   // SavingsAccount's version

        acc = new FixedDeposit();
        System.out.println("FixedDeposit   : " + acc.interestRate() + "%");   // FixedDeposit's version
    }
}
```

**Sample output**

```text
Account        : 3.0%
SavingsAccount : 4.0%
FixedDeposit   : 7.0%
```

```text
  Account acc = new SavingsAccount();     reference type: Account     object type: SavingsAccount
  acc.interestRate();
     compile time : javac only checks that class Account HAS interestRate()
     run time     : the JVM sees a SavingsAccount object and runs SavingsAccount.interestRate()
```

Rules of overriding:

- Same method name and **exactly the same parameter list**.
- Same return type, or a **subtype** of it (covariant return type, Java 5+):

```java
class Animal {
    Animal getInstance() { return new Animal(); }
}
class Dog extends Animal {
    @Override
    Dog getInstance() { return new Dog(); }     // Dog is a subtype of Animal: allowed
}
```

- It needs inheritance (an IS-A relationship); it cannot happen inside a single class.
- The access level cannot be narrowed: a `public` method must stay `public` (*attempting to assign weaker access privileges; was public*).
- `final` methods cannot be overridden, `static` methods are hidden rather than overridden, and `private` methods are not inherited at all. Constructors are not inherited either, so they cannot be overridden.
- The overriding method cannot throw new or broader **checked** exceptions (*overridden method does not throw IOException*); it may throw fewer, narrower or unchecked ones.
- `super.method()` calls the parent's version, as `FixedDeposit` does. `@Override` is optional but recommended, because the compiler then catches a misspelt name or a wrong parameter type.

**3. Comparison**

| Basis | Method overloading | Method overriding |
|---|---|---|
| Definition | Same method name, different parameter list, usually within one class | A subclass redefines an inherited method with the same signature |
| Inheritance | Not required (an inherited method can also be overloaded in a subclass) | Required: always between a superclass and a subclass |
| Parameters | Must differ in number, type or order | Must be exactly the same |
| Return type | Same or different, but cannot be the only difference | Same, or a subtype (covariant) |
| Binding | Static / early binding, by the compiler | Dynamic / late binding, by the JVM at runtime |
| Polymorphism | Compile-time (static) polymorphism | Runtime (dynamic) polymorphism |
| Access modifier | Any | Same or wider, never narrower |
| `static` / `final` / `private` methods | Can be overloaded | Cannot be overridden |
| Checked exceptions | No restriction | No new or broader checked exceptions |
| Purpose | One name for the same operation on different inputs (readability) | Specialised behaviour in a subclass (extensibility) |
| Example | `area(double)`, `area(double, double)`, `area(int)` | `interestRate()` in `Account`, `SavingsAccount` and `FixedDeposit` |

**Summary:** Overloading means the same name with different parameters, resolved by the compiler (compile-time polymorphism). Overriding means the same signature redefined in a subclass, resolved by the JVM from the actual object (runtime polymorphism).

---

### T2. The `this`, `super` and `final` keywords

**1. The `this` keyword**

`this` is a reference variable that refers to the **current object**, the object whose method or constructor is running.

| # | Use | Syntax |
|---|---|---|
| 1 | Refer to an instance variable hidden by a parameter or local variable | `this.name = name;` |
| 2 | Call another constructor of the same class (constructor chaining) | `this(rollNo, name);` |
| 3 | Call a method of the current object | `this.display();` |
| 4 | Pass the current object as an argument | `room.add(this);` |
| 5 | Return the current object (enables method chaining) | `return this;` |

```java
class Student {
    private int rollNo;
    private String name;
    private String course;

    Student(int rollNo, String name) {
        this.rollNo = rollNo;                   // 1. this.field: the field, not the parameter
        this.name = name;
        this.course = "Not assigned";
    }

    Student(int rollNo, String name, String course) {
        this(rollNo, name);                     // 2. this(...): reuse the other constructor
        this.course = course;
    }

    void display() {
        System.out.println(rollNo + " | " + name + " | " + course);
    }

    void print() {
        this.display();                         // 3. this.method(): same as display()
    }

    void enrolIn(Classroom room) {
        room.add(this);                         // 4. pass the current object as an argument
    }

    Student changeCourse(String course) {
        this.course = course;
        return this;                            // 5. return the current object
    }
}

class Classroom {
    void add(Student s) {
        System.out.print("Added to classroom: ");
        s.display();
    }
}

public class ThisDemo {
    public static void main(String[] args) {
        Student s1 = new Student(1, "Pam");
        Student s2 = new Student(2, "Jim", "MCA");
        s1.print();
        s2.print();
        s2.enrolIn(new Classroom());
        s1.changeCourse("MBA").display();       // method chaining, possible because of return this
    }
}
```

**Sample output**

```text
1 | Pam | Not assigned
2 | Jim | MCA
Added to classroom: 2 | Jim | MCA
1 | Pam | MBA
```

Without `this` in the first constructor, `rollNo = rollNo;` would assign the parameter to itself and the field would stay `0`.

Rules: `this(...)` must be the first statement of a constructor, one constructor cannot call both `this(...)` and `super(...)`, and `this` cannot be used inside a `static` method because no object is involved.

**2. The `super` keyword**

`super` is a reference to the **immediate parent-class** part of the current object.

| # | Use | Syntax |
|---|---|---|
| 1 | Access a parent field hidden by a child field of the same name | `super.maxSpeed` |
| 2 | Call the parent's version of an overridden method | `super.describe();` |
| 3 | Call a parent constructor | `super(brand);` |

```java
class Vehicle {
    String brand;
    int maxSpeed = 120;

    Vehicle(String brand) {
        this.brand = brand;
        System.out.println("Vehicle constructor: brand = " + brand);
    }

    void describe() {
        System.out.println("A vehicle made by " + brand);
    }
}

class Car extends Vehicle {
    int maxSpeed = 180;                         // hides Vehicle's maxSpeed

    Car(String brand) {
        super(brand);                           // 3. call the parent constructor (first statement)
        System.out.println("Car constructor");
    }

    @Override
    void describe() {
        super.describe();                       // 2. run the parent's version first
        System.out.println("It is a car with top speed " + maxSpeed + " km/h");
    }

    void compareSpeeds() {
        System.out.println("this.maxSpeed  = " + this.maxSpeed);     // Car's field
        System.out.println("super.maxSpeed = " + super.maxSpeed);    // 1. Vehicle's field
    }
}

public class SuperDemo {
    public static void main(String[] args) {
        Car c = new Car("Dodge");
        c.describe();
        c.compareSpeeds();
    }
}
```

**Sample output**

```text
Vehicle constructor: brand = Dodge
Car constructor
A vehicle made by Dodge
It is a car with top speed 180 km/h
this.maxSpeed  = 180
super.maxSpeed = 120
```

Points to remember:

- The parent constructor always runs first (constructor chaining). If a constructor has no explicit `super(...)` or `this(...)`, the compiler inserts `super();`, which fails to compile if the parent has no no-argument constructor.
- `super(...)` must be the first statement of the constructor. *(JDK 25 relaxes this with "flexible constructor bodies": statements that do not use `this` may come before `super(...)`. Compiling with `--release 8`, or any release up to 24 without preview features, still rejects it, so write it first in the exam.)*
- Like `this`, `super` cannot be used in a `static` context.

**3. The `final` keyword**

`final` is a non-access modifier meaning "cannot be changed". What it freezes depends on where it is used:

| Applied to | Effect | Example |
|---|---|---|
| Local variable / field | Can be assigned only once: a constant | `final int MAX_MARKS = 100;` |
| Blank final field | Declared without a value; must be assigned exactly once in every constructor | `final int accountNo;` |
| `static final` field | One shared class constant | `static final double PI = 3.14159;` |
| Parameter | Cannot be reassigned inside the method | `void set(final int x)` |
| Reference variable | Cannot point to another object, but the object itself can still change | `final StringBuilder course` |
| Method | Cannot be overridden by a subclass | `final void showAccountNo()` |
| Class | Cannot be extended | `final class MathConstants` (like `String`, `Integer`, `Math`) |

```java
final class MathConstants {                     // final class: cannot be extended
    static final double PI = 3.14159;           // final variable: a constant
}

class Account {
    final int accountNo;                        // blank final: assigned exactly once...

    Account(int accountNo) {
        this.accountNo = accountNo;             // ...in the constructor
    }

    final void showAccountNo() {                // final method: cannot be overridden
        System.out.println("Account no : " + accountNo);
    }
}

class SavingsAccount extends Account {
    SavingsAccount(int accountNo) {
        super(accountNo);
    }
    // void showAccountNo() { }                 // error: overridden method is final
}

// class MyConstants extends MathConstants { }  // error: cannot inherit from final MathConstants

public class FinalDemo {
    public static void main(String[] args) {
        final int MAX_MARKS = 100;              // final local variable
        // MAX_MARKS = 120;                     // error: cannot assign a value to final variable MAX_MARKS

        Account acc = new SavingsAccount(1001);
        acc.showAccountNo();                    // a final method is still inherited and callable
        // acc.accountNo = 2002;                // error: cannot assign a value to final variable accountNo

        final StringBuilder course = new StringBuilder("MCA");
        course.append(" 2026-28");              // allowed: the OBJECT can change
        // course = new StringBuilder("MBA");   // error: the REFERENCE cannot

        System.out.println("PI         : " + MathConstants.PI);
        System.out.println("Max marks  : " + MAX_MARKS);
        System.out.println("Course     : " + course);
    }
}
```

**Sample output**

```text
Account no : 1001
PI         : 3.14159
Max marks  : 100
Course     : MCA 2026-28
```

Each commented-out line is a compile-time error, with the compiler's message written beside it.

**Why a `final` method cannot be overridden**

1. **That is what `final` means.** Marking a method `final` tells the compiler its implementation is complete and must be the same in every subclass. Overriding exists precisely to *replace* an inherited implementation through dynamic dispatch, so the two contradict each other and `javac` rejects the attempt:

```java
class Account {
    final void showAccountNo() { }
}
class SavingsAccount extends Account {
    void showAccountNo() { }        // tries to override a final method
}
```

```text
error: showAccountNo() in SavingsAccount cannot override showAccountNo() in Account
    void showAccountNo() { }
         ^
  overridden method is final
```

2. **Security and integrity.** A method that validates a PIN, checks a permission or updates a balance must not be replaced by a subclass with weaker logic.
3. **Consistent behaviour.** Other code relies on the method doing exactly what the superclass promises. In the *template method* design, a final method fixes the order of the steps while subclasses fill in the individual steps.
4. **Efficiency.** Since no subclass can replace it, a call to a `final` method can be bound at compile time (early binding), and the JIT compiler can inline it.

A `final` method is still **inherited** and can be **called** on subclass objects (`acc.showAccountNo()` above), and it can be **overloaded**; it just cannot be overridden. All methods of a `final` class are effectively final, and `private` methods behave the same way because a subclass cannot even see them.

**Summary:** `this` refers to the current object, `super` to its parent-class part, and `final` freezes a variable's value, a method's implementation or a class's hierarchy.

---

### T3. Upcasting, downcasting and dynamic method dispatch

Casting within an inheritance hierarchy changes only the **type of the reference** used to look at an object; the object itself never changes.

**1. Upcasting**

Upcasting is treating a subclass object as an object of its superclass, by assigning it to a superclass reference.

```java
Animal a = new Dog();           // implicit upcast: a Dog IS-A Animal
Animal b = (Animal) new Dog();  // an explicit cast is legal but unnecessary
```

- It is **implicit** and always **safe**, because a `Dog` has everything an `Animal` has.
- Through `a`, only members declared in `Animal` can be called (`a.fetch()` gives *cannot find symbol*), but an overridden method still runs the `Dog` version.
- It lets one piece of code work with every subclass, which is the basis of runtime polymorphism.

**2. Downcasting**

Downcasting is converting a superclass reference back to a subclass reference so that subclass-specific members can be used.

```java
Animal a = new Dog();
Dog d = (Dog) a;                // explicit downcast: needed to call d.fetch()
```

- It must be **explicit**, using the cast operator.
- It is **checked at runtime**: it succeeds only if the object really is a `Dog` (or a subclass of `Dog`); otherwise the JVM throws `ClassCastException`.

```text
             Animal
            /      \            upcasting    Dog -> Animal : implicit, always safe
          Dog      Cat          downcasting  Animal -> Dog : explicit, checked at run time
```

**3. Dynamic method dispatch**

Dynamic method dispatch is the mechanism by which a call to an **overridden method** through a **superclass reference** is resolved at **runtime**, using the class of the actual object rather than the type of the reference. It is how Java implements runtime polymorphism.

**How runtime polymorphism is achieved.** Three ingredients are needed:

1. **Inheritance**: `Dog` and `Cat` extend `Animal`.
2. **Method overriding**: each subclass overrides `sound()`.
3. **Upcasting**: the objects are used through an `Animal` reference.

```text
Animal a = new Cat();
a.sound();
  compile time : javac checks that class Animal declares sound()    -> compiles
  run time     : the JVM finds that the actual object is a Cat
                 -> looks up sound() in Cat's method table          -> runs Cat.sound()
                 (had Cat not overridden it, the search would move up to Animal)
```

```java
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }

    void eat() {
        System.out.println("Animal eats food");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }

    void fetch() {                                  // Dog-only method
        System.out.println("Dog fetches the ball");
    }
}

class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("Cat meows");
    }

    void climb() {                                  // Cat-only method
        System.out.println("Cat climbs the tree");
    }
}

public class CastingDemo {
    public static void main(String[] args) {
        System.out.println("1. Upcasting");
        Animal a = new Dog();                       // implicit: Dog -> Animal
        a.sound();                                  // Dog's version (dynamic dispatch)
        a.eat();                                    // inherited from Animal
        // a.fetch();                               // error: cannot find symbol (Animal has no fetch)

        System.out.println("2. Downcasting");
        Dog d = (Dog) a;                            // explicit: the object really is a Dog
        d.fetch();

        System.out.println("3. Dynamic method dispatch");
        Animal[] animals = { new Dog(), new Cat(), new Animal() };
        for (Animal x : animals) {
            x.sound();                              // one call, three behaviours
        }

        System.out.println("4. Safe downcasting with instanceof");
        for (Animal x : animals) {
            if (x instanceof Dog) {
                ((Dog) x).fetch();
            } else if (x instanceof Cat) {
                ((Cat) x).climb();
            } else {
                System.out.println("Plain Animal: no downcast");
            }
        }

        System.out.println("5. Incorrect downcasting");
        try {
            Animal generic = new Animal();
            Dog wrong = (Dog) generic;              // compiles, but the object is NOT a Dog
            wrong.fetch();
        } catch (ClassCastException e) {
            System.out.println("ClassCastException: " + e.getMessage());
        }
    }
}
```

**Sample output**

```text
1. Upcasting
Dog barks
Animal eats food
2. Downcasting
Dog fetches the ball
3. Dynamic method dispatch
Dog barks
Cat meows
Animal makes a sound
4. Safe downcasting with instanceof
Dog fetches the ball
Cat climbs the tree
Plain Animal: no downcast
5. Incorrect downcasting
ClassCastException: class Animal cannot be cast to class Dog (Animal and Dog are in unnamed module of loader 'app')
```

Only overridden **instance methods** are dispatched dynamically. Fields and `static` methods are chosen by the **reference** type:

```java
Parent p = new Child();     // both classes declare a field 'name' and a static method info()
System.out.println(p.name); // Parent field          -> fields follow the reference type
p.info();                   // Parent static method  -> static methods are hidden, not overridden
```

**4. Risks of incorrect downcasting**

1. **`ClassCastException` at runtime.** `(Dog) generic` compiles because an `Animal` reference *might* point to a `Dog`, but the JVM finds a plain `Animal` and throws (step 5 of the output). If nothing catches it, the program terminates.
2. **Compile-time error between unrelated classes.** Sibling classes can never be cast to each other, and `javac` knows it:

```java
Dog d = new Dog();
Cat c = (Cat) d;            // error: incompatible types: Dog cannot be converted to Cat
```

3. **Bugs that appear only with certain data.** A cast that works for every object during testing fails the day a collection holds a different subclass, and the crash happens far from where the wrong object was added.
4. **Weaker design.** Frequent downcasting usually means behaviour that belongs in an overridden method is being chosen with `if` checks instead, which defeats polymorphism.

**Safe downcasting:** check with `instanceof` first (step 4 of the program). Java 16+ combines the test and the cast:

```java
if (a instanceof Dog d) {   // Java 16+: pattern matching for instanceof
    d.fetch();
}
```

| Basis | Upcasting | Downcasting |
|---|---|---|
| Direction | Subclass → superclass | Superclass → subclass |
| Syntax | Implicit | Explicit cast, e.g. `(Dog) a` |
| Safety | Always safe | May throw `ClassCastException` |
| Members usable | Only those declared in the superclass (overridden ones run subclass code) | All members of the subclass |
| Purpose | General code; runtime polymorphism | Reach subclass-specific features |

**Summary:** Upcasting is implicit and safe, downcasting is explicit and checked at runtime, and dynamic method dispatch makes an overridden method called through a superclass reference run the version that belongs to the actual object.

---

### T4. Abstract classes and abstract methods

**Definition**

- An **abstract class** is a class declared with the `abstract` keyword. It **cannot be instantiated** and serves as a base class that may contain both abstract and concrete methods.
- An **abstract method** is a method declared with `abstract` and **no body**; the declaration ends with a semicolon. It states *what* a subclass must do and leaves *how* to the subclass.

```java
abstract class Shape {              // abstract class
    abstract double area();         // abstract method: no body
    void describe() {               // concrete method
        System.out.println("Area = " + area());
    }
}
```

**Features and rules**

- `new Payment(...)` is an error (*Payment is abstract; cannot be instantiated*), but a reference of the abstract type is fine: `Payment p = new CardPayment("Jim");`.
- It can have **constructors** (run through `super(...)` from a subclass), instance and static variables, and concrete, `static` and `final` methods.
- A class with even **one** abstract method must be declared abstract. An abstract class may also have **no** abstract methods, just to prevent direct instantiation.
- An abstract method cannot be `private`, `static` or `final`, because each of those makes overriding impossible (*illegal combination of modifiers: abstract and final*). For the same reason a class cannot be both `abstract` and `final`.
- It provides **partial abstraction** (anywhere from 0% to 100%).

**How subclasses implement abstract methods**

1. The subclass `extends` the abstract class.
2. It **overrides every abstract method** with the same signature and supplies a body; the access level may stay the same or widen, never narrow.
3. If it leaves even one abstract method unimplemented, it must itself be declared `abstract`. Otherwise:

```text
error: UpiPayment is not abstract and does not override abstract method mode() in Payment
```

4. An abstract subclass can implement some methods and leave the rest to the next level down:

```java
abstract class Polygon extends Shape {      // still abstract: area() is not implemented yet
    abstract int sides();
}
class Square extends Polygon {              // concrete: implements everything that is left
    double side = 4;
    double area() { return side * side; }
    int sides() { return 4; }
}
```

5. Calls made through the abstract-class reference run the subclass's implementation (dynamic method dispatch).

**Real-world example: online payments**

Every payment has a payer and follows the same overall procedure: work out the fee, add it to the amount, print a receipt. Only the **fee rule** and the **payment mode** differ between card and UPI. The common procedure goes in the abstract class, and the parts that vary become abstract methods.

```java
abstract class Payment {
    protected String payer;

    Payment(String payer) {                         // an abstract class can have a constructor
        this.payer = payer;
    }

    abstract String mode();                         // abstract methods: no body,
    abstract double fee(double amount);             // every concrete subclass must supply one

    void pay(double amount) {                       // concrete method shared by all subclasses
        double charge = fee(amount);
        System.out.printf("%-4s paid Rs. %7.2f by %-4s (fee Rs. %.2f)%n",
                payer, amount + charge, mode(), charge);
    }
}

class CardPayment extends Payment {
    CardPayment(String payer) {
        super(payer);
    }

    @Override
    String mode() {
        return "card";
    }

    @Override
    double fee(double amount) {
        return amount * 0.02;                       // 2% card processing fee
    }
}

class UpiPayment extends Payment {
    UpiPayment(String payer) {
        super(payer);
    }

    @Override
    String mode() {
        return "UPI";
    }

    @Override
    double fee(double amount) {
        return 0;                                   // no fee on UPI
    }
}

public class PaymentDemo {
    public static void main(String[] args) {
        // Payment p = new Payment("Jim");          // error: Payment is abstract; cannot be instantiated
        Payment[] payments = { new CardPayment("Jim"), new UpiPayment("Pam"), new CardPayment("Ryan") };
        double[] amounts = { 1500, 1500, 2400 };
        for (int i = 0; i < payments.length; i++) {
            payments[i].pay(amounts[i]);            // runs each subclass's own fee() and mode()
        }
    }
}
```

**Sample output**

```text
Jim  paid Rs. 1530.00 by card (fee Rs. 30.00)
Pam  paid Rs. 1500.00 by UPI  (fee Rs. 0.00)
Ryan paid Rs. 2448.00 by card (fee Rs. 48.00)
```

`pay()` is written once in `Payment`, yet each call uses the subclass's own `fee()` and `mode()`. Other everyday examples: `BankAccount` with an abstract `calculateInterest()` (savings, current, fixed deposit), `Employee` with an abstract `calculateSalary()` (permanent, contract, intern), and `Vehicle` with an abstract `fuelEfficiency()`.

**Abstract class vs normal (concrete) class**

| Basis | Abstract class | Normal (concrete) class |
|---|---|---|
| Declaration | `abstract class Payment` | `class CardPayment` |
| Object creation | Not allowed | Allowed |
| Abstract methods | May contain them | Cannot contain any |
| Concrete methods | Can contain them | Contains only concrete methods |
| Constructors | Yes (called via a subclass) | Yes |
| Can be `final` | No | Yes |
| Purpose | Common base / template for related classes; partial abstraction | Complete implementation, used directly |
| Obligation on subclasses | A concrete subclass must implement every abstract method | None; overriding is optional |

**Advantages:** shared code lives in one place, every subclass is forced to supply the essential methods, and code written against the abstract type works with any present or future subclass.

**Summary:** An abstract class is a non-instantiable base class that can mix abstract methods (no body) with concrete ones. A concrete subclass must override every abstract method; otherwise it must be declared abstract too.

---

### T5. String, String array, StringBuffer and wrapper classes

**1. `String`**

A `String` is an object of the class `java.lang.String` that represents a sequence of characters. The class is `final`, and every `String` object is **immutable**: once created, its contents never change. Methods that seem to modify a string (`concat()`, `toUpperCase()`, `replace()` …) return a **new** `String`.

There are two ways to create one:

```java
String s1 = "Java";              // literal: stored in the String Constant Pool (SCP)
String s2 = "Java";              // same literal, so the pooled object is reused
String s3 = new String("Java");  // new: always a separate object on the heap
```

```text
              Heap
              +----------- String Constant Pool -----------+
   s1 ------> |   "Java"   (one object shared by s1, s2)   | <------ s2
              +--------------------------------------------+
   s3 ------> "Java"   (separate object created by new)
```

`==` compares **references** (is it the same object?), while `equals()` compares **contents**. Strings are immutable so that pooled objects can be shared safely, so that they are thread-safe, so that their hash code can be cached (which makes them good `HashMap` keys), and for security: a file name, URL or class name cannot be altered after it has been checked.

**2. String array**

A String array stores several `String` references under one name: `String[] names = new String[3];` (each element starts as `null`) or `String[] subjects = { "Java", "DCN" };`. It is traversed like any other array and sorted alphabetically with `Arrays.sort()`. The `String[] args` parameter of `main()` is a String array holding the command-line arguments.

**3. String methods**

| Method | Purpose | Example (`t = "Object Oriented Programming"`) |
|---|---|---|
| `length()` | Number of characters | `27` |
| `charAt(i)` | Character at index `i` | `charAt(7)` → `'O'` |
| `substring(b, e)` | Characters from `b` up to `e - 1` | `substring(7, 15)` → `"Oriented"` |
| `indexOf(s)` | First position of `s`, or `-1` | `indexOf("Pro")` → `16` |
| `toUpperCase()` / `toLowerCase()` | Change the case | `"OBJECT ORIENTED PROGRAMMING"` |
| `trim()` | Remove leading and trailing spaces | `"  hi  "` → `"hi"` |
| `replace(a, b)` | Replace every `a` with `b` | `replace('o', '0')` |
| `contains(s)` / `startsWith(s)` / `endsWith(s)` | Test for a substring | `true` / `true` / `true` |
| `equals(s)` / `equalsIgnoreCase(s)` | Compare contents | `"JAVA".equalsIgnoreCase("java")` → `true` |
| `compareTo(s)` | Dictionary order: negative, 0 or positive | `"Apple".compareTo("Banana")` → `-1` |
| `split(regex)` | Break into a String array | `[Object, Oriented, Programming]` |
| `concat(s)` | Join two strings (like `+`) | `"Java".concat(" 25")` |
| `String.valueOf(x)` / `String.join(d, …)` | Convert to a String / join with a delimiter | `String.join("-", "MCA", "2026")` → `"MCA-2026"` |
| `isEmpty()` | `true` if the length is 0 | `"".isEmpty()` → `true` |

```java
import java.util.Arrays;

public class StringDemo {
    static void show(String label, Object value) {
        System.out.printf("%-31s : %s%n", label, value);
    }

    public static void main(String[] args) {
        // 1. Creating strings: literal vs new
        String s1 = "Java";                         // stored in the String Constant Pool
        String s2 = "Java";                         // reuses the same pooled object
        String s3 = new String("Java");             // a separate object on the heap
        show("s1 == s2", s1 == s2);
        show("s1 == s3", s1 == s3);
        show("s1.equals(s3)", s1.equals(s3));

        // 2. Immutability: methods return a NEW string
        String lang = "Java";
        lang.concat(" Programming");                // result ignored, lang is unchanged
        show("concat() without assignment", lang);
        lang = lang.concat(" Programming");         // lang now refers to a new object
        show("concat() with assignment", lang);

        // 3. Common String methods
        String t = "  Object Oriented Programming  ".trim();
        show("trim()", "\"" + t + "\"");
        show("length()", t.length());
        show("charAt(7)", t.charAt(7));
        show("substring(7, 15)", t.substring(7, 15));
        show("indexOf(\"Pro\")", t.indexOf("Pro"));
        show("toUpperCase()", t.toUpperCase());
        show("toLowerCase()", t.toLowerCase());
        show("replace('o', '0')", t.replace('o', '0'));
        show("contains(\"Oriented\")", t.contains("Oriented"));
        show("startsWith(\"Obj\")", t.startsWith("Obj"));
        show("endsWith(\"ing\")", t.endsWith("ing"));
        show("split(\" \")", Arrays.toString(t.split(" ")));
        show("\"JAVA\".equalsIgnoreCase(\"java\")", "JAVA".equalsIgnoreCase("java"));
        show("\"Apple\".compareTo(\"Banana\")", "Apple".compareTo("Banana"));
        show("String.join(\"-\", \"MCA\", \"2026\")", String.join("-", "MCA", "2026"));

        // 4. String array
        String[] subjects = { "Python", "Java", "DCN", "ADBMS", "Research Methodology" };
        System.out.println("Subjects (" + subjects.length + "):");
        for (String sub : subjects) {
            System.out.println("  " + sub + " - " + sub.length() + " characters");
        }
        Arrays.sort(subjects);                      // alphabetical order
        System.out.println("Sorted : " + Arrays.toString(subjects));
    }
}
```

**Sample output**

```text
s1 == s2                        : true
s1 == s3                        : false
s1.equals(s3)                   : true
concat() without assignment     : Java
concat() with assignment        : Java Programming
trim()                          : "Object Oriented Programming"
length()                        : 27
charAt(7)                       : O
substring(7, 15)                : Oriented
indexOf("Pro")                  : 16
toUpperCase()                   : OBJECT ORIENTED PROGRAMMING
toLowerCase()                   : object oriented programming
replace('o', '0')               : Object Oriented Pr0gramming
contains("Oriented")            : true
startsWith("Obj")               : true
endsWith("ing")                 : true
split(" ")                      : [Object, Oriented, Programming]
"JAVA".equalsIgnoreCase("java") : true
"Apple".compareTo("Banana")     : -1
String.join("-", "MCA", "2026") : MCA-2026
Subjects (5):
  Python - 6 characters
  Java - 4 characters
  DCN - 3 characters
  ADBMS - 5 characters
  Research Methodology - 20 characters
Sorted : [ADBMS, DCN, Java, Python, Research Methodology]
```

**4. `StringBuffer`**

`StringBuffer` (in `java.lang`) is a **mutable** sequence of characters: its methods change the same object instead of creating new ones. All its methods are **synchronized**, so it is thread-safe.

- Constructors: `StringBuffer()` with capacity 16, `StringBuffer(int capacity)`, and `StringBuffer(String s)` with capacity 16 + `s.length()`.
- **Capacity** is the size of the internal character array. When it fills up, the buffer grows to *(old capacity × 2) + 2*.

| Method | Effect |
|---|---|
| `append(x)` | Adds `x` at the end |
| `insert(i, x)` | Inserts `x` at index `i` |
| `replace(b, e, s)` | Replaces characters `b` to `e - 1` with `s` |
| `delete(b, e)` / `deleteCharAt(i)` | Removes characters |
| `reverse()` | Reverses the contents |
| `setCharAt(i, c)` | Changes one character |
| `length()` / `capacity()` | Characters stored / space available |
| `toString()` | Converts to an (immutable) `String` |

```java
public class StringBufferDemo {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer("Java");
        System.out.println("Start       : " + sb + "  (length " + sb.length() + ", capacity " + sb.capacity() + ")");

        StringBuffer result = sb.append(" Programming");     // changes sb itself
        System.out.println("append()    : " + sb);
        System.out.println("same object : " + (result == sb));

        sb.insert(0, "Core ");                                // Core Java Programming
        System.out.println("insert()    : " + sb);
        sb.replace(5, 9, "JAVA");                             // Core JAVA Programming
        System.out.println("replace()   : " + sb);
        sb.delete(0, 5);                                      // JAVA Programming
        System.out.println("delete()    : " + sb);
        sb.setCharAt(0, 'j');                                 // jAVA Programming
        System.out.println("setCharAt() : " + sb);
        sb.reverse();
        System.out.println("reverse()   : " + sb);

        // when the buffer is full, capacity grows to (old capacity * 2) + 2
        StringBuffer buf = new StringBuffer();
        System.out.println("Empty buffer capacity        : " + buf.capacity());
        buf.append("ABCDEFGHIJKLMNOPQ");                      // 17 characters > 16
        System.out.println("Capacity after 17 characters : " + buf.capacity());

        // a String cannot change: "modifying" it creates a new object
        String s = "Java";
        String before = s;                                    // remember the original object
        s = s + " 25";
        System.out.println("String s : \"" + before + "\" -> \"" + s + "\", same object? " + (before == s));

        // equals(): String compares content, StringBuffer compares references
        StringBuffer b1 = new StringBuffer("MCA");
        StringBuffer b2 = new StringBuffer("MCA");
        System.out.println("b1.equals(b2)                       : " + b1.equals(b2));
        System.out.println("b1.toString().equals(b2.toString()) : " + b1.toString().equals(b2.toString()));
    }
}
```

**Sample output**

```text
Start       : Java  (length 4, capacity 20)
append()    : Java Programming
same object : true
insert()    : Core Java Programming
replace()   : Core JAVA Programming
delete()    : JAVA Programming
setCharAt() : jAVA Programming
reverse()   : gnimmargorP AVAj
Empty buffer capacity        : 16
Capacity after 17 characters : 34
String s : "Java" -> "Java 25", same object? false
b1.equals(b2)                       : false
b1.toString().equals(b2.toString()) : true
```

**5. `String` vs `StringBuffer`: mutability and memory**

```java
String s = "Java";
s = s + " 25";          // builds a NEW object "Java 25"; the old "Java" is garbage if nothing else uses it

StringBuffer sb = new StringBuffer("Java");
sb.append(" 25");       // the SAME object is modified in place
```

Repeating `s = s + i;` 1,000 times in a loop leaves about 1,000 short-lived `String` objects for the garbage collector, while `sb.append(i)` keeps writing into one buffer and only occasionally grows its array. (`javac` compiles `+` on strings into a `StringBuilder` behind the scenes, but inside a loop a new one is created on every pass.)

| Basis | `String` | `StringBuffer` |
|---|---|---|
| Mutability | Immutable | Mutable |
| On "modification" | A new object is created; the original is unchanged | The same object is changed in place |
| Memory | Literals are stored once and shared in the String Constant Pool; repeated changes leave many garbage objects | Always on the heap; one internal array that grows when full (capacity × 2 + 2) |
| Thread safety | Safe, because it can never change | Safe, because its methods are synchronized |
| Repeated changes | Slow (a new object and a full copy each time) | Fast |
| `equals()` | Overridden: compares contents | Not overridden: compares references (use `toString().equals(...)`) |
| Joining | `+` or `concat()` | `append()` |
| Use when | The text rarely changes (names, keys, constants) | The text changes many times (building output in a loop) |

`StringBuilder` (Java 5) has the same methods as `StringBuffer` but is **not synchronized**, so it is faster. It is the usual choice when only one thread uses the object.

**6. Wrapper classes**

A wrapper class wraps a primitive value inside an object. Every primitive type has one; all are in `java.lang`, `final` and immutable:

| Primitive | Wrapper | Primitive | Wrapper |
|---|---|---|---|
| `byte` | `Byte` | `float` | `Float` |
| `short` | `Short` | `double` | `Double` |
| `int` | `Integer` | `char` | `Character` |
| `long` | `Long` | `boolean` | `Boolean` |

Since Java 5 the compiler converts between them automatically: **autoboxing** turns a primitive into its wrapper (`Integer x = 85;`) and **unboxing** turns a wrapper back into a primitive (`int y = x;`).

**Why wrapper classes are needed**

1. **Collections and generics accept only objects**: `ArrayList<Integer>` is valid, `ArrayList<int>` is not.
2. **A value can be absent**: a wrapper reference can be `null` (marks not yet entered, a NULL database column), while a primitive always holds a value.
3. **Utility methods and constants**: `Integer.parseInt("21")`, `Double.parseDouble()`, `Integer.toString()`, `Integer.toBinaryString()`, `Character.isDigit()`, `Integer.MAX_VALUE`.
4. **APIs that work with `Object`**: methods that take `Object` parameters, serialization and synchronization all need objects.

```java
import java.util.ArrayList;

public class WrapperDemo {
    static void show(String label, Object value) {
        System.out.printf("%-25s = %s%n", label, value);
    }

    public static void main(String[] args) {
        // 1. Autoboxing and unboxing (Java 5+)
        int marks = 85;
        Integer boxed = marks;                      // autoboxing: int -> Integer
        int unboxed = boxed;                        // unboxing:   Integer -> int
        System.out.println("boxed = " + boxed + ", unboxed = " + unboxed);

        // 2. Collections hold objects only
        ArrayList<Integer> scores = new ArrayList<>();   // ArrayList<int> would not compile
        scores.add(72);                             // each int is autoboxed
        scores.add(88);
        scores.add(95);
        int total = 0;
        for (int s : scores) {                      // each Integer is unboxed
            total += s;
        }
        System.out.println("scores = " + scores + ", total = " + total);

        // 3. Conversion methods and constants
        int age = Integer.parseInt("21");           // String -> int
        double price = Double.parseDouble("499.50");
        String year = Integer.toString(2026);       // int -> String
        show("parseInt(\"21\") + 1", age + 1);
        show("parseDouble(\"499.50\") * 2", price * 2);
        show("toString(2026).length()", year.length());
        show("toBinaryString(10)", Integer.toBinaryString(10));
        show("Integer.MAX_VALUE", Integer.MAX_VALUE);
        show("Character.isDigit('7')", Character.isDigit('7'));

        // 4. A wrapper can be null; a primitive cannot
        Integer notEntered = null;
        show("notEntered", notEntered);

        // 5. Compare wrapper objects with equals(), not ==
        Integer a = 127, b = 127, c = 128, d = 128;
        show("a == b  (127)", a == b);              // same cached object (-128 to 127)
        show("c == d  (128)", c == d);              // two different objects
        show("c.equals(d)", c.equals(d));
    }
}
```

**Sample output**

```text
boxed = 85, unboxed = 85
scores = [72, 88, 95], total = 255
parseInt("21") + 1        = 22
parseDouble("499.50") * 2 = 999.0
toString(2026).length()   = 4
toBinaryString(10)        = 1010
Integer.MAX_VALUE         = 2147483647
Character.isDigit('7')    = true
notEntered                = null
a == b  (127)             = true
c == d  (128)             = false
c.equals(d)               = true
```

Two pitfalls: compare wrapper objects with `equals()`, because `==` compares references and only values from −128 to 127 are cached as shared objects; and unboxing a `null` wrapper (`int n = notEntered;`) throws `NullPointerException`.

**Summary:** `String` is immutable and pool-backed, `StringBuffer` is mutable and synchronized for text that changes often, and wrapper classes turn primitives into objects for collections, `null` values and utility methods.

---

### T6. Purpose of `this` and `super`

**`this`** is a reference to the **current object**. Its purpose is to:

- tell an instance variable apart from a parameter or local variable with the same name: `this.name = name;`
- call another constructor of the same class: `this(...)`, as the first statement;
- call a method of the current object, pass the current object as an argument, or return it (`return this;`).

**`super`** is a reference to the **immediate parent class** part of the current object. Its purpose is to:

- access a parent field hidden by a child field of the same name: `super.maxSpeed`;
- call the parent's version of an overridden method: `super.show();`
- call a parent constructor: `super(...)`, as the first statement (the compiler inserts `super();` if it is left out).

```java
class Person {
    String name;

    Person(String name) {
        this.name = name;                               // this: field vs parameter
    }

    void show() {
        System.out.println("Name    : " + name);
    }
}

class Student extends Person {
    int rollNo;

    Student(String name, int rollNo) {
        super(name);                                    // super: parent constructor
        this.rollNo = rollNo;                           // this: current object's field
    }

    @Override
    void show() {
        super.show();                                   // super: parent's version of show()
        System.out.println("Roll no : " + rollNo);
    }
}

public class ThisSuperSnippet {
    public static void main(String[] args) {
        new Student("Kelly", 7).show();
    }
}
```

**Sample output**

```text
Name    : Kelly
Roll no : 7
```

| Basis | `this` | `super` |
|---|---|---|
| Refers to | Current class's object | Parent class part of the object |
| Constructor call | `this(...)`: same class | `super(...)`: parent class |
| Field / method access | `this.x`, `this.m()` | `super.x`, `super.m()` |
| Typical use | Resolve name shadowing, constructor chaining | Reuse the parent's constructor and overridden methods |

Neither can be used in a `static` method, and one constructor cannot contain both `this(...)` and `super(...)`. Full programs: [T2](#t2-the-this-super-and-final-keywords).

---

### T7. Purpose of `static` and `final`

**`static`** makes a member belong to the **class** rather than to any one object, so a single copy exists and it can be used without creating an object.

- **Static variable**: one copy shared by every object, e.g. a college name or an object counter.
- **Static method**: called on the class (`Math.sqrt()`, `main()`). It can directly use only static members and cannot use `this` or `super`.
- **Static block**: runs once, when the class is loaded; used to initialise static data.
- **Static nested class**: a nested class that does not need an object of the outer class.

**`final`** makes something **unchangeable**.

- **Final variable**: assigned once, so it is a constant.
- **Final method**: cannot be overridden.
- **Final class**: cannot be inherited (e.g. `String`, `Math`).

```java
class Student {
    static String college = "MIT-WPU";          // static variable: ONE copy shared by all objects
    static int count = 0;

    final int rollNo;                           // final variable: fixed once assigned
    String name;

    static {                                    // static block: runs once, when the class loads
        System.out.println("Static block: class Student loaded");
    }

    Student(String name) {
        count++;
        this.rollNo = count;
        this.name = name;
    }

    static void showCount() {                   // static method: called on the class itself
        System.out.println("Students created: " + count);
        // System.out.println(name);            // error: non-static variable name cannot be referenced from a static context
    }

    void display() {
        System.out.println(rollNo + " " + name + " - " + college);
    }
}

public class StaticDemo {
    public static void main(String[] args) {
        Student s1 = new Student("Kevin");
        Student s2 = new Student("Angela");
        s1.display();
        s2.display();

        Student.college = "MIT World Peace University";    // change the shared copy once...
        s1.display();                                       // ...and every object sees it
        s2.display();

        Student.showCount();                                // no object needed
    }
}
```

**Sample output**

```text
Static block: class Student loaded
1 Kevin - MIT-WPU
2 Angela - MIT-WPU
1 Kevin - MIT World Peace University
2 Angela - MIT World Peace University
Students created: 2
```

Changing `Student.college` once changed it for both objects, because there is only one copy; the static block ran once, before the first object was created. Together, `static final` gives a class-wide constant such as `Math.PI`.

| Basis | `static` | `final` |
|---|---|---|
| Meaning | Belongs to the class; one shared copy | Cannot be changed after being set |
| Applies to | Variables, methods, blocks, nested classes | Variables, methods, classes |
| Effect on methods | Called without an object; cannot be overridden (only hidden) | Cannot be overridden |
| Effect on variables | Shared by all objects | Value fixed after assignment |

---

### T8. Access modifiers

Access modifiers control **where** a class, constructor, field or method can be used from. They are how Java enforces encapsulation (data hiding).

1. **`private`**: visible only inside the class where it is declared. Used to hide fields, which are then exposed through public getters and setters.
2. **default** (no keyword, also called *package-private*): visible to every class in the **same package** only.
3. **`protected`**: visible in the same package, and also in **subclasses in other packages** (through inheritance).
4. **`public`**: visible from **everywhere**.

| Modifier | Same class | Same package (subclass or not) | Subclass in another package | Non-subclass in another package |
|---|---|---|---|---|
| `private` | Yes | No | No | No |
| default | Yes | Yes | No | No |
| `protected` | Yes | Yes | Yes (through inheritance) | No |
| `public` | Yes | Yes | Yes | Yes |

From most to least restrictive: `private` → default → `protected` → `public`.

```java
package bank;

public class Account {
    private double balance;         // only code inside Account
    String branch;                  // default: any class in package bank
    protected String holder;        // package bank + subclasses in any package
    public long accountNo;          // any class anywhere

    public double getBalance() {    // controlled, read-only access to the private field
        return balance;
    }
}
```

Points to remember:

- A top-level class can only be `public` or default; `private` and `protected` apply to members (and nested classes).
- A `public` class must be saved in a file with the same name.
- An overriding method cannot narrow the access of the method it overrides.
- A `private` constructor stops other classes from creating objects (used in the singleton pattern).

[P15](#p15-access-modifiers-across-packages) demonstrates every level across two packages, with the actual compiler errors.

---

### T9. User-defined packages

A **package** is a named group of related classes, interfaces and sub-packages; it acts as a folder and a namespace. Java has **built-in** packages (`java.lang`, `java.util`, `java.io`) and **user-defined** packages, which the programmer creates to organise their own classes.

Packages help to avoid name clashes (two classes called `Student` can live in different packages), keep a project organised, control access (default and `protected` members), and reuse classes across programs.

**Steps to create a package**

1. Choose a name, in lowercase by convention (organisations often use their reversed domain, e.g. `com.mitwpu.mca`).
2. Write `package mathutil;` as the **first statement** of the source file.
3. Declare as `public` every class, constructor and method that other packages should use.
4. Save the file in a folder with the same name as the package (`mathutil/Calculator.java`), or let `javac -d` create the folder.
5. Compile it. `javac -d . Calculator.java` creates the `mathutil` folder and puts `Calculator.class` inside it.

**Steps to import and use it**

1. In the other class, write `import mathutil.Calculator;` to import one class, or `import mathutil.*;` for every class in the package (sub-packages are not included). Alternatively, skip the import and use the fully qualified name `mathutil.Calculator`.
2. Compile and run from the folder that **contains** `mathutil`, or add that folder to the CLASSPATH (`-cp`).

```java
package mathutil;                           // the package statement must come first

public class Calculator {                   // public, so other packages can use it
    public int add(int a, int b) {
        return a + b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }
}
```

```java
import mathutil.Calculator;                 // import the class from the package

public class UseCalculator {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println("12 + 8 = " + calc.add(12, 8));
        System.out.println("12 x 8 = " + calc.multiply(12, 8));

        mathutil.Calculator calc2 = new mathutil.Calculator();  // fully qualified name: no import needed
        System.out.println("5 + 5  = " + calc2.add(5, 5));
    }
}
```

```text
project/
├── mathutil/
│   └── Calculator.java
└── UseCalculator.java
```

```text
javac mathutil/Calculator.java
javac UseCalculator.java
java UseCalculator
```

**Sample output**

```text
12 + 8 = 20
12 x 8 = 96
5 + 5  = 10
```

If `Calculator` is not declared `public`, the import fails with *Calculator is not public in mathutil; cannot be accessed from outside package*. `java.lang` is imported automatically, which is why `String` and `System` need no import. Another full example: [P11](#p11-user-defined-package-mypackage).

---

### T10. Interfaces and their advantages

An **interface** is a reference type that defines a **contract**: a set of method declarations (and constants) that any class implementing it must provide. It specifies *what* a class must do, not *how*. It is declared with `interface` and implemented with `implements`.

```java
interface Camera {
    int MEGAPIXELS = 50;        // a constant: public static final
    void takePhoto();           // an abstract method: public abstract
}
```

**Features and rules**

- Methods without a body are implicitly `public abstract`; fields are implicitly `public static final` (constants).
- An interface cannot be instantiated and has no constructors.
- A class `implements` one or more interfaces and must override every abstract method with a `public` method, or else be declared `abstract`.
- An interface can `extend` one or more other interfaces.
- Java 8 added `default` methods (with a body, inherited by implementing classes) and `static` methods; Java 9 added `private` helper methods.

```java
interface Camera {
    int MEGAPIXELS = 50;                        // implicitly public static final
    void takePhoto();                           // implicitly public abstract
}

interface MusicPlayer {
    void playMusic(String song);

    default void showEqualizer() {              // Java 8: default method (has a body)
        System.out.println("Equalizer: Normal");
    }

    static String version() {                   // Java 8: static method
        return "MusicPlayer v2";
    }
}

class SmartPhone implements Camera, MusicPlayer {      // one class, two interfaces
    @Override
    public void takePhoto() {
        System.out.println("Photo taken with the " + MEGAPIXELS + " MP camera");
    }

    @Override
    public void playMusic(String song) {
        System.out.println("Playing: " + song);
    }
}

public class InterfaceDemo {
    public static void main(String[] args) {
        SmartPhone phone = new SmartPhone();
        phone.takePhoto();
        phone.playMusic("Raag Yaman");
        phone.showEqualizer();                      // inherited default method
        System.out.println(MusicPlayer.version());  // static method: called on the interface

        Camera cam = phone;                         // interface reference to the same object
        cam.takePhoto();
        // cam.playMusic("x");                      // error: Camera declares no playMusic()
    }
}
```

**Sample output**

```text
Photo taken with the 50 MP camera
Playing: Raag Yaman
Equalizer: Normal
MusicPlayer v2
Photo taken with the 50 MP camera
```

**Advantages of interfaces**

1. **Abstraction**: callers see only the contract, never the implementation.
2. **Multiple inheritance of type**: a class can implement many interfaces (`SmartPhone` is both a `Camera` and a `MusicPlayer`), which Java does not allow with classes.
3. **Loose coupling**: code written against an interface works with any implementation, e.g. `List<String> list = new ArrayList<>();` can be switched to `LinkedList` without changing the code that uses `list`. JDBC works the same way through its `Connection` interface.
4. **Polymorphism**: an interface reference can point to any implementing object.
5. **A shared standard**: teams agree on the interface first and build the parts independently; plug-in designs depend on this.
6. **Easier testing and maintenance**: an implementation can be replaced, or mocked in tests, without touching its callers.
7. **Safe evolution**: `default` methods let an interface gain new methods without breaking classes that already implement it.

---

### T11. Abstract class vs interface

| Basis | Abstract class | Interface |
|---|---|---|
| Keyword | `abstract class` | `interface` |
| Inherited with | `extends`, and a class can extend only one | `implements`, and a class can implement many; an interface can `extend` many interfaces |
| Methods | Abstract and concrete | Abstract; plus `default` and `static` (Java 8) and `private` (Java 9) |
| Variables | Any kind: instance or static, final or not | Only `public static final` constants |
| Constructors | Yes | No |
| Member access | Any modifier (`private`, `protected` …) | Implicitly `public` (except Java 9 `private` methods) |
| Object state | Can hold instance state | Cannot hold instance state |
| Multiple inheritance | Not supported | Supported |
| Abstraction | Partial (0–100%) | Full (100%) for abstract methods; traditionally fully abstract |
| Relationship | IS-A: closely related classes sharing code | CAN-DO: a capability shared by unrelated classes |
| Example | `abstract class Shape` with `Circle`, `Square` | `Comparable`, `Runnable`, `Printable` |

```java
abstract class Shape {                  // shared state + shared code + an abstract part
    protected String colour;
    Shape(String colour) { this.colour = colour; }
    abstract double area();
    void paint() { System.out.println("Painting " + colour); }
}

interface Printable {                   // only a capability
    void print();
}

class Circle extends Shape implements Printable {   // one class, plus any number of interfaces
    double r = 1;
    Circle() { super("red"); }
    double area() { return Math.PI * r * r; }
    public void print() { System.out.println("Circle of area " + area()); }
}
```

**In common:** neither can be instantiated, both can be used as reference types, and both force subclasses or implementing classes to supply method bodies.

**Which to use:** choose an abstract class when related classes share fields and code; choose an interface when unrelated classes need a common capability, or when a class needs more than one supertype.

---

### T12. Adapter classes

An **adapter class** is a class that implements a listener interface and gives **every method an empty body**. A class that needs only some of the interface's methods extends the adapter and overrides just those, instead of writing empty bodies for all the others.

Java AWT provides adapter classes in `java.awt.event` for each listener interface that has more than one method:

| Adapter class | Listener interface(s) it implements |
|---|---|
| `WindowAdapter` | `WindowListener` (7 methods), `WindowStateListener`, `WindowFocusListener` |
| `MouseAdapter` | `MouseListener` (5 methods), `MouseMotionListener`, `MouseWheelListener` |
| `MouseMotionAdapter` | `MouseMotionListener` (2 methods) |
| `KeyAdapter` | `KeyListener` (3 methods) |
| `FocusAdapter` | `FocusListener` (2 methods) |
| `ComponentAdapter` | `ComponentListener` (4 methods) |
| `ContainerAdapter` | `ContainerListener` (2 methods) |

**Purpose:** implementing an interface directly forces a class to implement *all* of its methods. To close a window you need only `windowClosing()`, but implementing `WindowListener` means writing all seven methods. Extending `WindowAdapter` means writing one.

```java
import java.awt.Frame;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class CloseWindow {
    public static void main(String[] args) {
        Frame f = new Frame("Adapter demo");
        f.setSize(300, 200);
        f.addWindowListener(new WindowAdapter() {   // WindowListener has 7 methods,
            @Override                               // but we override only windowClosing()
            public void windowClosing(WindowEvent e) {
                f.dispose();
            }
        });
        f.setVisible(true);
    }
}
```

This compiles as shown; it opens a window rather than printing anything. The same idea works with your own interfaces, in a program that runs on the console:

```java
interface PhoneListener {
    void onIncomingCall(String caller);
    void onMessage(String sender);
    void onLowBattery(int percent);
    void onCharging();
}

// Adapter class: empty bodies for every method of the interface
abstract class PhoneAdapter implements PhoneListener {
    public void onIncomingCall(String caller) { }
    public void onMessage(String sender) { }
    public void onLowBattery(int percent) { }
    public void onCharging() { }
}

// Interested in ONE event only, so it overrides just that method
class BatteryMonitor extends PhoneAdapter {
    @Override
    public void onLowBattery(int percent) {
        System.out.println("Battery at " + percent + "% - power saver switched on");
    }
}

class Phone {
    private PhoneListener listener;

    void setListener(PhoneListener listener) {
        this.listener = listener;
    }

    void simulateDay() {                            // fires all four events
        listener.onIncomingCall("Michael");
        listener.onMessage("Dwight");
        listener.onLowBattery(15);
        listener.onCharging();
    }
}

public class AdapterDemo {
    public static void main(String[] args) {
        Phone phone = new Phone();

        phone.setListener(new BatteryMonitor());
        phone.simulateDay();                        // only onLowBattery() prints

        phone.setListener(new PhoneAdapter() {      // anonymous subclass of the adapter
            @Override
            public void onIncomingCall(String caller) {
                System.out.println("Ringing: call from " + caller);
            }
        });
        phone.simulateDay();                        // only onIncomingCall() prints
    }
}
```

**Sample output**

```text
Battery at 15% - power saver switched on
Ringing: call from Michael
```

Each `simulateDay()` fires all four events, but only the overridden method produces output; the other three run the adapter's empty bodies.

**Advantages**

- Less code: only the needed methods are written.
- More readable: the class shows only the events it actually handles.
- Fewer mistakes: no long lists of empty methods to keep in sync with the interface.
- Works neatly with anonymous inner classes for one-off listeners.

**Limitation:** Java allows only one superclass, so a class that already extends something else cannot also extend an adapter; it must use an inner or anonymous class. Since Java 8, interfaces can provide `default` methods, which removes the need for adapters in newly designed interfaces.

A second example, with a `StudentActivity` interface: [P14](#p14-adapter-class-for-studentactivity).

---

### T13. Types of exceptions

An **exception** is an abnormal event that occurs while a program is running and disrupts its normal flow, such as dividing by zero or opening a missing file. In Java, an exception is an object of a class derived from `java.lang.Throwable`. Exception handling lets the program catch it, respond and carry on instead of terminating.

```text
java.lang.Object
└── java.lang.Throwable
    ├── java.lang.Error                          serious JVM / system problems (unchecked)
    │   ├── VirtualMachineError
    │   │   ├── OutOfMemoryError
    │   │   └── StackOverflowError
    │   ├── AssertionError
    │   └── LinkageError  (e.g. NoClassDefFoundError)
    └── java.lang.Exception
        ├── IOException                          ┐
        │   └── FileNotFoundException            │  CHECKED exceptions
        ├── SQLException                         │  (the compiler forces you
        ├── ClassNotFoundException               │   to handle or declare them)
        ├── InterruptedException                 ┘
        └── RuntimeException                     ┐
            ├── ArithmeticException              │
            ├── NullPointerException             │  UNCHECKED exceptions
            ├── ClassCastException               │  (not checked by the compiler)
            ├── IllegalArgumentException         │
            │   └── NumberFormatException        │
            └── IndexOutOfBoundsException        │
                ├── ArrayIndexOutOfBoundsException
                └── StringIndexOutOfBoundsException ┘
```

**1. Checked exceptions (compile-time exceptions)**

Subclasses of `Exception` other than `RuntimeException`. The compiler checks that each one is either caught with `try`/`catch` or declared with `throws`; otherwise the code does not compile:

```text
error: unreported exception FileNotFoundException; must be caught or declared to be thrown
```

They usually come from conditions outside the program's control.

| Exception | Typical cause |
|---|---|
| `IOException` / `FileNotFoundException` | File missing or unreadable |
| `SQLException` | Database access error |
| `ClassNotFoundException` | Class not found when loaded by name (e.g. a JDBC driver) |
| `InterruptedException` | A sleeping or waiting thread is interrupted |

**2. Unchecked exceptions (runtime exceptions)**

`RuntimeException` and its subclasses. The compiler does not force handling; they usually signal programming mistakes or bad input.

| Exception | Typical cause |
|---|---|
| `ArithmeticException` | Integer division by zero |
| `ArrayIndexOutOfBoundsException` | Index < 0 or ≥ the array's length |
| `StringIndexOutOfBoundsException` | Bad index in `charAt()` or `substring()` |
| `NullPointerException` | Calling a method or field on `null` |
| `NumberFormatException` | `Integer.parseInt("abc")` |
| `ClassCastException` | Invalid downcast |
| `IllegalArgumentException` | A method receives an unacceptable argument |

**3. Errors**

`Error` and its subclasses: serious problems in the JVM or its environment, such as `OutOfMemoryError` and `StackOverflowError`. They are unchecked, and normal programs should not try to catch them because they generally cannot recover.

Exceptions can also be classified as **built-in** (provided by Java, as above) and **user-defined** (written by the programmer, see [T17](#t17-user-defined-exceptions)).

```java
import java.io.FileReader;
import java.io.IOException;

public class ExceptionTypes {
    static String text = null;

    public static void main(String[] args) {
        // ---- Unchecked (runtime) exceptions: the compiler does not force handling ----
        try {
            int a = 10, b = 0;
            System.out.println(a / b);
        } catch (ArithmeticException e) {
            System.out.println("1. " + e);
        }

        try {
            int[] marks = new int[3];
            marks[5] = 90;
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("2. " + e);
        }

        try {
            int n = Integer.parseInt("abc");
        } catch (NumberFormatException e) {
            System.out.println("3. " + e);
        }

        try {
            System.out.println(text.length());
        } catch (NullPointerException e) {
            System.out.println("4. " + e);
        }

        try {
            Object o = "hello";
            Integer i = (Integer) o;
        } catch (ClassCastException e) {
            System.out.println("5. " + e);
        }

        // ---- Checked exception: must be caught or declared, or the code will not compile ----
        try {
            FileReader fr = new FileReader("missing.txt");
            fr.close();
        } catch (IOException e) {
            System.out.println("6. " + e);
        }

        // ---- Error: a JVM-level problem; caught here ONLY to show it ----
        try {
            recurse(1);
        } catch (StackOverflowError e) {
            System.out.println("7. " + e);
        }
    }

    static int recurse(int n) {
        return recurse(n + 1);                  // never stops -> StackOverflowError
    }
}
```

**Sample output**

```text
1. java.lang.ArithmeticException: / by zero
2. java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 3
3. java.lang.NumberFormatException: For input string: "abc"
4. java.lang.NullPointerException: Cannot invoke "String.length()" because "ExceptionTypes.text" is null
5. java.lang.ClassCastException: class java.lang.String cannot be cast to class java.lang.Integer (java.lang.String and java.lang.Integer are in module java.base of loader 'bootstrap')
6. java.io.FileNotFoundException: missing.txt (No such file or directory)
7. java.lang.StackOverflowError
```

The messages are from JDK 25; older JDKs print shorter ones (Java 8 prints just `java.lang.NullPointerException` and `java.lang.ArrayIndexOutOfBoundsException: 5`), and on Windows message 6 ends with *(The system cannot find the file specified)*.

| Basis | Checked exceptions | Unchecked exceptions |
|---|---|---|
| Checked by | Compiler, at compile time | Not checked; occur at runtime |
| Classes | `Exception` subclasses except `RuntimeException` | `RuntimeException` and its subclasses (and `Error`) |
| Handling | Mandatory: `try`/`catch` or `throws` | Optional |
| Usual cause | External conditions (files, network, database) | Programming errors, bad input |
| Examples | `IOException`, `SQLException` | `ArithmeticException`, `NullPointerException` |

---

### T14. `throw` vs `throws`

- **`throw`** is a statement used **inside a method body** to explicitly throw **one** exception object, either built-in or user-defined: `throw new IllegalArgumentException("Age is below 18");`. Execution of the current block stops at once and control jumps to the nearest matching `catch`.
- **`throws`** is a clause in a **method signature** that **declares** the exception types the method may pass on to its caller: `void readMarksFile(String f) throws IOException`. The caller must then handle them or declare them itself. It is mandatory for checked exceptions that the method does not catch.

```java
import java.io.IOException;

public class ThrowThrowsDemo {
    // throw: explicitly throws ONE exception object
    static void checkAge(int age) {
        if (age < 18) {
            throw new IllegalArgumentException("Age " + age + " is below 18");
        }
        System.out.println("Age " + age + ": eligible to vote");
    }

    // throws: declares that this method may pass an IOException to its caller
    static void readMarksFile(String fileName) throws IOException {
        if (!fileName.endsWith(".csv")) {
            throw new IOException("Unsupported file type: " + fileName);
        }
        System.out.println("Reading " + fileName);
    }

    public static void main(String[] args) {
        checkAge(21);
        try {
            checkAge(15);
        } catch (IllegalArgumentException e) {
            System.out.println("Caught: " + e.getMessage());
        }

        try {
            readMarksFile("marks.csv");
            readMarksFile("marks.pdf");
        } catch (IOException e) {                   // the caller must handle (or re-declare) it
            System.out.println("Caught: " + e.getMessage());
        }
    }
}
```

**Sample output**

```text
Age 21: eligible to vote
Caught: Age 15 is below 18
Reading marks.csv
Caught: Unsupported file type: marks.pdf
```

`checkAge()` throws an unchecked exception, so it needs no `throws` clause. `readMarksFile()` throws a checked `IOException` without catching it, so the `throws IOException` clause is mandatory, and `main()` is forced to call it inside `try`/`catch`.

| Basis | `throw` | `throws` |
|---|---|---|
| Purpose | Actually throws an exception | Declares exceptions that may be thrown |
| Where | Inside a method or block | In the method signature, after the parameter list |
| Followed by | An exception **object**: `throw new IOException("…")` | Exception **class names**: `throws IOException` |
| How many | One exception at a time | Several, comma-separated: `throws IOException, SQLException` |
| Checked exceptions | Throwing one requires a matching `throws` clause or an enclosing `try`/`catch` | Passes checked exceptions on to the caller |
| Effect | Transfers control immediately | Informs the compiler and the caller; changes nothing at runtime |

---

### T15. `try`, `catch` and `finally`

- **`try`** encloses the code that might throw an exception. It must be followed by at least one `catch` or a `finally` (*'try' without 'catch', 'finally' or resource declarations* otherwise).
- **`catch (Type e)`** handles an exception of the matching type (or a subclass of it). There can be several catch blocks; only the first matching one runs. The parameter `e` describes the exception: `e.getMessage()`, `e.toString()`, `e.printStackTrace()`.
- **`finally`** always runs, whether an exception occurs or not and whether it is caught or not, even if the `try` or `catch` executes `return`. It is used for clean-up such as closing files, database connections or a `Scanner`. It is skipped only if the JVM stops, e.g. through `System.exit()`.

```java
try {
    // code that may throw an exception
} catch (ExceptionType1 e) {
    // handle ExceptionType1
} catch (ExceptionType2 e) {
    // handle ExceptionType2
} finally {
    // clean-up: always runs
}
```

| Situation | `try` | `catch` | `finally` | Afterwards |
|---|---|---|---|---|
| No exception | Runs completely | Skipped | Runs | Execution continues after the block |
| Exception that is caught | Stops at the faulty line | The matching block runs | Runs | Execution continues after the block |
| Exception that is not caught | Stops at the faulty line | No block matches | Runs | The exception propagates to the caller; if nobody catches it, the program terminates with a stack trace |

```java
public class TryCatchFinallyDemo {
    static int divide(int a, int b) {
        try {
            System.out.println("try     : dividing " + a + " by " + b);
            return a / b;                           // even a return does not skip finally
        } catch (ArithmeticException e) {
            System.out.println("catch   : " + e.getMessage());
            return 0;
        } finally {
            System.out.println("finally : cleanup done");
        }
    }

    public static void main(String[] args) {
        System.out.println("Result = " + divide(20, 4));
        System.out.println();
        System.out.println("Result = " + divide(20, 0));
    }
}
```

**Sample output**

```text
try     : dividing 20 by 4
finally : cleanup done
Result = 5

try     : dividing 20 by 0
catch   : / by zero
finally : cleanup done
Result = 0
```

In the first call `try` executes `return a / b;`, yet `finally` still prints before the result reaches `main()`. In the second call the division throws, `catch` handles it, and `finally` runs again.

Rules: a variable declared inside `try` is not visible in `catch` or `finally`; catch blocks for subclasses must come before catch blocks for their superclasses ([T16](#t16-nested-try-blocks-and-multiple-catch-statements)). Since Java 7, **try-with-resources** closes resources automatically, without an explicit `finally`:

```java
try (Scanner sc = new Scanner(System.in)) {     // sc.close() is called automatically
    int n = sc.nextInt();
}
```

A simple arithmetic-exception program: [P16](#p16-try-catch-and-finally-for-an-arithmetic-exception).

---

### T16. Nested `try` blocks and multiple `catch` statements

**Multiple `catch` statements**

One `try` block can be followed by several `catch` blocks, each handling a different exception type. When an exception occurs, the catch blocks are checked **from top to bottom**; the first one whose type matches runs and the rest are skipped.

```java
public class MultipleCatch {
    public static void main(String[] args) {
        String[] values = { "50", "0", "abc" };
        for (String v : values) {
            try {
                int divisor = Integer.parseInt(v);                     // may throw NumberFormatException
                System.out.println("100 / " + v + " = " + (100 / divisor)); // may throw ArithmeticException
            } catch (NumberFormatException e) {
                System.out.println("\"" + v + "\" is not a number");
            } catch (ArithmeticException e) {
                System.out.println("Cannot divide by " + v);
            } catch (Exception e) {                                    // most general type LAST
                System.out.println("Unexpected: " + e);
            }
        }
    }
}
```

**Sample output**

```text
100 / 50 = 2
Cannot divide by 0
"abc" is not a number
```

Rules:

- At most one catch block runs for each exception.
- A subclass must be caught **before** its superclass. Putting `catch (Exception e)` first makes every later catch unreachable, which is a compile error: *exception ArithmeticException has already been caught*.
- Since Java 7, one block can catch several unrelated types with `|` (multi-catch). The alternatives must not be subclasses of one another (*Alternatives in a multi-catch statement cannot be related by subclassing*), and `e` is implicitly `final`:

```java
catch (NumberFormatException | ArithmeticException e) {
    System.out.println("Bad input: " + e.getMessage());
}
```

**Nested `try` blocks**

A `try` block (with its own `catch`/`finally`) placed **inside another `try` block** is a nested try. It is used when part of a block can fail in a way that should be handled locally, while other failures are left to the outer block.

If an exception in the inner `try` is not matched by any inner `catch`, it **propagates to the outer `try`**'s catch blocks; if none of those match either, it goes to the method's caller.

```java
public class NestedTry {
    public static void main(String[] args) {
        int[] data = { 10, 0 };
        try {                                           // outer try
            try {                                       // inner try
                System.out.println(data[0] / data[1]);
            } catch (ArithmeticException e) {           // handled at the inner level
                System.out.println("Inner catch: " + e.getMessage());
            }
            System.out.println(data[2]);                // no inner try covers this line
        } catch (ArrayIndexOutOfBoundsException e) {    // handled at the outer level
            System.out.println("Outer catch: " + e.getMessage());
        }
    }
}
```

**Sample output**

```text
Inner catch: / by zero
Outer catch: Index 2 out of bounds for length 2
```

```text
outer try ─┬─ inner try ── 10 / 0 ── ArithmeticException ──> inner catch (handled, continue)
           │
           └─ data[2] ── ArrayIndexOutOfBoundsException ──> no inner handler ──> outer catch
```

| Basis | Multiple catch | Nested try |
|---|---|---|
| Structure | One `try`, several `catch` blocks | A `try` block inside another `try` |
| Purpose | Handle different exception types differently | Handle exceptions at different levels |
| Search order | Catch blocks from top to bottom | Inner catches first, then outer catches, then the caller |

Longer programs: [P17](#p17-multiple-catch-statements) (multiple catch) and [P18](#p18-nested-try-blocks-at-different-levels) (three levels of nesting).

---

### T17. User-defined exceptions

A **user-defined (custom) exception** is an exception class written by the programmer to represent an error condition specific to the application, such as an age below 18, an invalid email or insufficient funds. It is created by extending `Exception` or `RuntimeException`.

**Why use them**

- Built-in exceptions describe technical failures, not business rules; there is no built-in `InvalidAgeException`.
- A meaningful class name makes the code and the error report self-explanatory.
- The class can carry extra data (for example, the shortfall amount in [P8](#p8-insufficientfundexception-with-the-additional-amount-required)).
- Each rule can get its own `catch` block.

**Procedure for creating and using one**

1. **Create a class** that extends `Exception` (a checked exception) or `RuntimeException` (an unchecked exception).
2. **Add constructors**, usually one that takes a `String` message and passes it on with `super(message)`, so that `getMessage()` returns it. A no-argument constructor and extra fields are optional.
3. **Throw it** with `throw new MyException("…")` when the rule is broken.
4. **Declare it** with `throws MyException` in the signature of the method that throws it (mandatory for a checked exception).
5. **Handle it** by calling the method inside `try` and catching it with `catch (MyException e)`, typically printing `e.getMessage()`.

```java
// Step 1: extend Exception (a checked exception)
class InvalidAgeException extends Exception {
    // Step 2: constructors that pass the message up to Exception
    public InvalidAgeException() {
        super("Invalid age");
    }

    public InvalidAgeException(String message) {
        super(message);
    }
}

public class VoterRegistration {
    // Step 4: declare it with throws
    static void register(String name, int age) throws InvalidAgeException {
        if (age < 18) {
            // Step 3: throw it when the rule is broken
            throw new InvalidAgeException(name + " is " + age + "; the minimum voting age is 18");
        }
        System.out.println(name + " registered as a voter");
    }

    public static void main(String[] args) {
        // Step 5: call it inside try and handle it in catch
        try {
            register("Jim", 30);
            register("Luke", 15);
            register("Pam", 28);                    // skipped: control already jumped to catch
        } catch (InvalidAgeException e) {
            System.out.println("InvalidAgeException: " + e.getMessage());
        }
        System.out.println("Registration desk closed");
    }
}
```

**Sample output**

```text
Jim registered as a voter
InvalidAgeException: Luke is 15; the minimum voting age is 18
Registration desk closed
```

Once `register("Luke", 15)` throws, the rest of the `try` block is skipped, so Pam is never registered; control resumes after the `catch`.

| Basis | Extends `Exception` (checked) | Extends `RuntimeException` (unchecked) |
|---|---|---|
| Compiler check | Must be caught or declared with `throws` | Not enforced |
| Use for | Recoverable conditions the caller should deal with (invalid input, insufficient balance) | Programming errors or rules the caller cannot reasonably recover from |
| Example | `class InvalidAgeException extends Exception` | `class InvalidMarksException extends RuntimeException` |

More examples: [P4](#p4-invalidemailexception-for-an-email-address), [P8](#p8-insufficientfundexception-with-the-additional-amount-required), [P19](#p19-validating-an-email-with-invalidemailexception), [P20](#p20-insufficientfundexception-on-withdrawal), and the class exercise [src/theory/class_ques/q2.java](src/theory/class_ques/q2.java) (`InvalidMarksException` with nested try and multiple catch).

---

## Programs

Each program is complete: save it in a file named after its `public class` (for example `ManagerDemo.java`), compile with `javac ManagerDemo.java` and run with `java ManagerDemo`. Programs whose question says "accept" read from the keyboard with `Scanner`, and their **Sample run** shows what the user typed after each prompt. The rest use fixed values so that the output is reproducible. P11 and P15 use packages, so they show the folder layout and the exact commands.

### P1. `Manager` interface implemented by `HRManager`

```java
interface Manager {
    void showDetails();                     // implicitly public abstract
}

class HRManager implements Manager {
    private String name;
    private String department;
    private int teamSize;

    HRManager(String name, String department, int teamSize) {
        this.name = name;
        this.department = department;
        this.teamSize = teamSize;
    }

    @Override
    public void showDetails() {             // must be public: interface methods are public
        System.out.println("Name       : " + name);
        System.out.println("Role       : HR Manager");
        System.out.println("Department : " + department);
        System.out.println("Team size  : " + teamSize);
    }
}

public class ManagerDemo {
    public static void main(String[] args) {
        Manager m = new HRManager("Toby Flenderson", "Human Resources", 4);  // interface reference
        m.showDetails();                    // runs HRManager's implementation
    }
}
```

**Sample output**

```text
Name       : Toby Flenderson
Role       : HR Manager
Department : Human Resources
Team size  : 4
```

`showDetails()` is called through a `Manager` (interface) reference, and the JVM runs `HRManager`'s implementation. The implementing method must be `public`: leaving it package-private gives *attempting to assign weaker access privileges; was public*, because interface methods are implicitly `public`.

---

### P2. Top two products by price

```java
import java.util.Scanner;

class Product {
    int productId;
    String productName;
    int quantity;
    double price;

    Product(int productId, String productName, int quantity, double price) {
        this.productId = productId;
        this.productName = productName;
        this.quantity = quantity;
        this.price = price;
    }

    void display() {
        System.out.printf("%-5d %-12s %8d %10.2f%n", productId, productName, quantity, price);
    }
}

public class TopProducts {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Product[] products = new Product[10];

        System.out.println("Enter details of 10 products (id name quantity price):");
        for (int i = 0; i < products.length; i++) {
            System.out.print("Product " + (i + 1) + ": ");
            int id = sc.nextInt();
            String name = sc.next();                // one-word product name
            int qty = sc.nextInt();
            double price = sc.nextDouble();
            products[i] = new Product(id, name, qty, price);
        }

        // one pass: track the highest and the second-highest price
        Product first = null, second = null;
        for (Product p : products) {
            if (first == null || p.price > first.price) {
                second = first;                     // old highest becomes second
                first = p;
            } else if (second == null || p.price > second.price) {
                second = p;
            }
        }

        System.out.println("\nTop two products by price:");
        System.out.printf("%-5s %-12s %8s %10s%n", "ID", "Name", "Quantity", "Price");
        first.display();
        second.display();
        sc.close();
    }
}
```

**Sample run**

```text
Enter details of 10 products (id name quantity price):
Product 1: 101 Keyboard 25 1500
Product 2: 102 Monitor 10 12000
Product 3: 103 Mouse 40 600
Product 4: 104 Laptop 5 55000
Product 5: 105 Printer 8 9000
Product 6: 106 Webcam 15 2500
Product 7: 107 Speaker 12 3200
Product 8: 108 Router 20 2800
Product 9: 109 Headphones 18 4500
Product 10: 110 Tablet 6 18000

Top two products by price:
ID    Name         Quantity      Price
104   Laptop              5   55000.00
110   Tablet              6   18000.00
```

A single pass finds both answers: when a product beats the current highest, the old highest moves down to second place; otherwise it is compared with the second. Sorting gives the same result in more code; with Java 8 it is `Arrays.sort(products, (a, b) -> Double.compare(b.price, a.price));` followed by printing `products[0]` and `products[1]`.

---

### P3. `Student` and `Marks` using inheritance

```java
class Student {
    protected int rollNo;
    protected String name;

    Student(int rollNo, String name) {
        this.rollNo = rollNo;
        this.name = name;
    }

    void displayStudent() {
        System.out.println("Roll no        : " + rollNo);
        System.out.println("Name           : " + name);
    }
}

class Marks extends Student {                   // Marks IS-A Student
    private int theory;                         // out of 60
    private int practical;                      // out of 40

    Marks(int rollNo, String name, int theory, int practical) {
        super(rollNo, name);                    // initialise the inherited Student part
        this.theory = theory;
        this.practical = practical;
    }

    int calculateTotal() {
        return theory + practical;
    }

    void displayResult() {
        displayStudent();                       // inherited from Student
        int total = calculateTotal();
        System.out.println("Java theory    : " + theory + " / 60");
        System.out.println("Java practical : " + practical + " / 40");
        System.out.println("Total          : " + total + " / 100");
        System.out.println("Result         : " + (total >= 40 ? "PASS" : "FAIL"));
    }
}

public class StudentResult {
    public static void main(String[] args) {
        Marks m1 = new Marks(1, "Oscar Martinez", 52, 36);
        Marks m2 = new Marks(2, "Kevin Malone", 21, 14);
        m1.displayResult();
        System.out.println();
        m2.displayResult();
    }
}
```

**Sample output**

```text
Roll no        : 1
Name           : Oscar Martinez
Java theory    : 52 / 60
Java practical : 36 / 40
Total          : 88 / 100
Result         : PASS

Roll no        : 2
Name           : Kevin Malone
Java theory    : 21 / 60
Java practical : 14 / 40
Total          : 35 / 100
Result         : FAIL
```

`Marks extends Student`, so a `Marks` object has the roll number and name too: `super(rollNo, name)` fills them in, and `displayResult()` reuses the inherited `displayStudent()`. The 60 + 40 split and the pass mark of 40 are assumptions; change them to match your scheme.

---

### P4. `InvalidEmailException` for an email address

```java
import java.util.Scanner;

class InvalidEmailException extends Exception {
    public InvalidEmailException(String message) {
        super(message);
    }
}

public class EmailValidation {
    static void validateEmail(String email) throws InvalidEmailException {
        if (email.isEmpty()) {
            throw new InvalidEmailException("Email cannot be empty");
        }
        if (Character.isDigit(email.charAt(0))) {
            throw new InvalidEmailException("Email must not start with a digit");
        }
        if (!email.contains("@")) {
            throw new InvalidEmailException("Email must contain @");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter email address: ");
        String email = sc.nextLine().trim();
        try {
            validateEmail(email);
            System.out.println("Valid email: " + email);
        } catch (InvalidEmailException e) {
            System.out.println("InvalidEmailException: " + e.getMessage());
        }
        sc.close();
    }
}
```

**Sample run 1 (valid)**

```text
Enter email address: jim.halpert@example.com
Valid email: jim.halpert@example.com
```

**Sample run 2 (starts with a digit)**

```text
Enter email address: 9jim@example.com
InvalidEmailException: Email must not start with a digit
```

**Sample run 3 (no `@`)**

```text
Enter email address: jim.halpert.example.com
InvalidEmailException: Email must contain @
```

`InvalidEmailException extends Exception`, so it is checked: `validateEmail()` must declare `throws InvalidEmailException`, and `main()` must call it inside `try`/`catch`. The empty-string check comes first because `charAt(0)` on an empty string would throw `StringIndexOutOfBoundsException`.

---

### P5. `Bank` class with constructors, deposit and withdraw

```java
class Bank {
    private String customerName;
    private long accountNumber;
    private double balance;

    Bank() {                                            // default constructor
        this("Unknown", 0L, 0.0);
    }

    Bank(String customerName, long accountNumber) {     // new account, zero balance
        this(customerName, accountNumber, 0.0);
    }

    Bank(String customerName, long accountNumber, double balance) {   // all details
        this.customerName = customerName;
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    void deposit(double amount) {
        if (amount <= 0) {
            System.out.println("Deposit failed: amount must be positive");
            return;
        }
        balance += amount;
        System.out.printf("Deposited Rs. %.2f -> balance Rs. %.2f%n", amount, balance);
    }

    void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Withdrawal failed: amount must be positive");
        } else if (amount > balance) {
            System.out.printf("Withdrawal of Rs. %.2f failed: balance is only Rs. %.2f%n", amount, balance);
        } else {
            balance -= amount;
            System.out.printf("Withdrew  Rs. %.2f -> balance Rs. %.2f%n", amount, balance);
        }
    }

    void display() {
        System.out.println("Customer : " + customerName);
        System.out.println("Account  : " + accountNumber);
        System.out.printf("Balance  : Rs. %.2f%n", balance);
    }
}

public class BankDemo {
    public static void main(String[] args) {
        System.out.println("--- Account 1 (all details) ---");
        Bank acc1 = new Bank("Stanley Hudson", 50012345L, 10000);
        acc1.display();
        acc1.deposit(2500);
        acc1.withdraw(4000);
        acc1.withdraw(20000);
        System.out.println("Updated details:");
        acc1.display();

        System.out.println("\n--- Account 2 (zero opening balance) ---");
        Bank acc2 = new Bank("Phyllis Vance", 50067890L);
        acc2.deposit(5000);
        acc2.withdraw(1200);
        acc2.display();

        System.out.println("\n--- Account 3 (default constructor) ---");
        Bank acc3 = new Bank();
        acc3.display();
    }
}
```

**Sample output**

```text
--- Account 1 (all details) ---
Customer : Stanley Hudson
Account  : 50012345
Balance  : Rs. 10000.00
Deposited Rs. 2500.00 -> balance Rs. 12500.00
Withdrew  Rs. 4000.00 -> balance Rs. 8500.00
Withdrawal of Rs. 20000.00 failed: balance is only Rs. 8500.00
Updated details:
Customer : Stanley Hudson
Account  : 50012345
Balance  : Rs. 8500.00

--- Account 2 (zero opening balance) ---
Deposited Rs. 5000.00 -> balance Rs. 5000.00
Withdrew  Rs. 1200.00 -> balance Rs. 3800.00
Customer : Phyllis Vance
Account  : 50067890
Balance  : Rs. 3800.00

--- Account 3 (default constructor) ---
Customer : Unknown
Account  : 0
Balance  : Rs. 0.00
```

The class has three overloaded constructors chained with `this(...)`, so the assignments are written only once. The fields are `private`, so the balance can change only through `deposit()` and `withdraw()`, which reject non-positive amounts and overdrafts.

---

### P6. Staff member with the highest salary

```java
class Staff {
    String name;
    String birthDate;                       // dd-mm-yyyy
    String designation;
    double salary;

    Staff(String name, String birthDate, String designation, double salary) {
        this.name = name;
        this.birthDate = birthDate;
        this.designation = designation;
        this.salary = salary;
    }

    void display() {
        System.out.printf("%-16s %-11s %-18s %10.2f%n", name, birthDate, designation, salary);
    }
}

public class HighestSalary {
    public static void main(String[] args) {
        Staff[] staff = {
            new Staff("Michael Scott", "15-03-1965", "Regional Manager", 85000),
            new Staff("Dwight Schrute", "20-01-1970", "Assistant Manager", 62000),
            new Staff("Jim Halpert", "01-10-1978", "Sales Executive", 58000),
            new Staff("Pam Beesly", "25-03-1979", "Receptionist", 40000),
            new Staff("Oscar Martinez", "18-05-1972", "Accountant", 64000)
        };

        System.out.printf("%-16s %-11s %-18s %10s%n", "Name", "Birth date", "Designation", "Salary");
        for (Staff s : staff) {
            s.display();
        }

        Staff highest = staff[0];                   // assume the first is highest...
        for (int i = 1; i < staff.length; i++) {
            if (staff[i].salary > highest.salary) { // ...and replace it whenever we find more
                highest = staff[i];
            }
        }
        System.out.printf("%nHighest salary: %s (Rs. %.2f)%n", highest.name, highest.salary);
    }
}
```

**Sample output**

```text
Name             Birth date  Designation            Salary
Michael Scott    15-03-1965  Regional Manager     85000.00
Dwight Schrute   20-01-1970  Assistant Manager    62000.00
Jim Halpert      01-10-1978  Sales Executive      58000.00
Pam Beesly       25-03-1979  Receptionist         40000.00
Oscar Martinez   18-05-1972  Accountant           64000.00

Highest salary: Michael Scott (Rs. 85000.00)
```

The search assumes the first object has the highest salary and replaces it whenever a larger one appears, so it needs only one pass over the five objects.

---

### P7. Abstract `Order` with `PurchaseOrder` and `SalesOrder`

```java
import java.util.Scanner;

abstract class Order {
    protected int orderId;
    protected String item;
    protected int quantity;
    protected double rate;

    protected void acceptCommon(Scanner sc) {       // concrete method shared by both subclasses
        orderId = sc.nextInt();
        item = sc.next();
        quantity = sc.nextInt();
        rate = sc.nextDouble();
    }

    double amount() {
        return quantity * rate;
    }

    abstract void accept(Scanner sc);               // each subclass also reads its own field
    abstract void display();
}

class PurchaseOrder extends Order {
    private String vendor;

    @Override
    void accept(Scanner sc) {
        acceptCommon(sc);
        vendor = sc.next();
    }

    @Override
    void display() {
        System.out.printf("%-5d %-8s %4d %8.2f %10.2f  %s%n", orderId, item, quantity, rate, amount(), vendor);
    }
}

class SalesOrder extends Order {
    private String customer;

    @Override
    void accept(Scanner sc) {
        acceptCommon(sc);
        customer = sc.next();
    }

    @Override
    void display() {
        System.out.printf("%-5d %-8s %4d %8.2f %10.2f  %s%n", orderId, item, quantity, rate, amount(), customer);
    }
}

public class OrderDemo {
    static final int COUNT = 5;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Order[] purchases = new Order[COUNT];       // arrays of the abstract type
        Order[] sales = new Order[COUNT];

        System.out.println("Enter " + COUNT + " purchase orders (id item quantity rate vendor):");
        for (int i = 0; i < COUNT; i++) {
            System.out.print("PO " + (i + 1) + ": ");
            purchases[i] = new PurchaseOrder();
            purchases[i].accept(sc);                // PurchaseOrder.accept()
        }

        System.out.println("Enter " + COUNT + " sales orders (id item quantity rate customer):");
        for (int i = 0; i < COUNT; i++) {
            System.out.print("SO " + (i + 1) + ": ");
            sales[i] = new SalesOrder();
            sales[i].accept(sc);                    // SalesOrder.accept()
        }

        printOrders("PURCHASE ORDERS", "Vendor", purchases);
        printOrders("SALES ORDERS", "Customer", sales);
        sc.close();
    }

    static void printOrders(String title, String party, Order[] orders) {
        System.out.println("\n" + title);
        System.out.printf("%-5s %-8s %4s %8s %10s  %s%n", "ID", "Item", "Qty", "Rate", "Amount", party);
        double total = 0;
        for (Order o : orders) {
            o.display();                            // dynamic dispatch picks the subclass's display()
            total += o.amount();
        }
        System.out.printf("Total value: Rs. %.2f%n", total);
    }
}
```

**Sample run**

```text
Enter 5 purchase orders (id item quantity rate vendor):
PO 1: 201 Paper 50 250 PaperMart
PO 2: 202 Toner 10 1800 InkWorld
PO 3: 203 Stapler 25 120 OfficeHub
PO 4: 204 Chair 8 3500 FurniCo
PO 5: 205 Router 3 2800 TechZone
Enter 5 sales orders (id item quantity rate customer):
SO 1: 301 Paper 120 320 Holly
SO 2: 302 Toner 6 2100 Jan
SO 3: 303 Stapler 15 150 Karen
SO 4: 304 Chair 4 4200 David
SO 5: 305 Router 2 3300 Robert

PURCHASE ORDERS
ID    Item      Qty     Rate     Amount  Vendor
201   Paper      50   250.00   12500.00  PaperMart
202   Toner      10  1800.00   18000.00  InkWorld
203   Stapler    25   120.00    3000.00  OfficeHub
204   Chair       8  3500.00   28000.00  FurniCo
205   Router      3  2800.00    8400.00  TechZone
Total value: Rs. 69900.00

SALES ORDERS
ID    Item      Qty     Rate     Amount  Customer
301   Paper     120   320.00   38400.00  Holly
302   Toner       6  2100.00   12600.00  Jan
303   Stapler    15   150.00    2250.00  Karen
304   Chair       4  4200.00   16800.00  David
305   Router      2  3300.00    6600.00  Robert
Total value: Rs. 76650.00
```

`Order` cannot be instantiated, but `Order[]` arrays can hold either subclass. The fields common to both orders are read by the concrete method `acceptCommon()`, written once in the abstract class; each subclass's `accept()` adds its own field (vendor or customer). `display()` is abstract, so each subclass prints in its own way, and `printOrders()` works for both through dynamic method dispatch.

---

### P8. `InSufficientFundException` with the additional amount required

```java
class InSufficientFundException extends Exception {
    private double shortfall;                       // extra data carried by the exception

    public InSufficientFundException(double shortfall) {
        super("Insufficient balance");
        this.shortfall = shortfall;
    }

    public double getShortfall() {
        return shortfall;
    }
}

class BankAccount {
    private String holder;
    private double balance;

    BankAccount(String holder, double balance) {
        this.holder = holder;
        this.balance = balance;
    }

    void withdraw(double amount) throws InSufficientFundException {
        if (amount > balance) {
            throw new InSufficientFundException(amount - balance);
        }
        balance -= amount;
        System.out.printf("  Success. Remaining balance: Rs. %.2f%n", balance);
    }

    double getBalance() {
        return balance;
    }

    String getHolder() {
        return holder;
    }
}

public class InsufficientFundDemo {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount("Kevin Malone", 10000);
        System.out.printf("Account holder: %s, opening balance: Rs. %.2f%n", acc.getHolder(), acc.getBalance());

        double[] requests = { 4000, 7500, 6000 };
        for (double amount : requests) {
            System.out.printf("Withdraw Rs. %.2f%n", amount);
            try {
                acc.withdraw(amount);
            } catch (InSufficientFundException e) {
                System.out.printf("  %s! Available: Rs. %.2f%n", e.getMessage(), acc.getBalance());
                System.out.printf("  Additional amount required: Rs. %.2f%n", e.getShortfall());
            }
        }
    }
}
```

**Sample output**

```text
Account holder: Kevin Malone, opening balance: Rs. 10000.00
Withdraw Rs. 4000.00
  Success. Remaining balance: Rs. 6000.00
Withdraw Rs. 7500.00
  Insufficient balance! Available: Rs. 6000.00
  Additional amount required: Rs. 1500.00
Withdraw Rs. 6000.00
  Success. Remaining balance: Rs. 0.00
```

The exception carries extra data: when `withdraw()` finds the balance too low, it stores the shortfall (`amount - balance`) in the exception object, and the `catch` block reads it back with `getShortfall()`. After the failed request the balance is unchanged, so the final withdrawal of Rs. 6000 still succeeds.

---

### P9. Abstract `Shape` and dynamic method dispatch

```java
abstract class Shape {
    protected String name;

    Shape(String name) {
        this.name = name;
    }

    abstract double area();                         // no body: each shape computes it differently

    void display() {                                // concrete method that calls the abstract one
        System.out.printf("%-9s area = %.2f%n", name, area());
    }
}

class Circle extends Shape {
    private double radius;

    Circle(double radius) {
        super("Circle");
        this.radius = radius;
    }

    @Override
    double area() {
        return Math.PI * radius * radius;
    }
}

class Rectangle extends Shape {
    private double length, breadth;

    Rectangle(double length, double breadth) {
        super("Rectangle");
        this.length = length;
        this.breadth = breadth;
    }

    @Override
    double area() {
        return length * breadth;
    }
}

class Triangle extends Shape {
    private double base, height;

    Triangle(double base, double height) {
        super("Triangle");
        this.base = base;
        this.height = height;
    }

    @Override
    double area() {
        return 0.5 * base * height;
    }
}

public class ShapeDemo {
    public static void main(String[] args) {
        Shape s;                                    // reference of the abstract type

        s = new Circle(5);
        System.out.printf("Circle    : %.2f%n", s.area());     // Circle.area()
        s = new Rectangle(4, 6);
        System.out.printf("Rectangle : %.2f%n", s.area());     // Rectangle.area()
        s = new Triangle(8, 5);
        System.out.printf("Triangle  : %.2f%n", s.area());     // Triangle.area()

        System.out.println("\nThrough an array of Shape references:");
        Shape[] shapes = { new Circle(2.5), new Rectangle(3, 7), new Triangle(6, 4) };
        double total = 0;
        for (Shape sh : shapes) {
            sh.display();                           // display() calls the right area()
            total += sh.area();
        }
        System.out.printf("Total area = %.2f%n", total);
    }
}
```

**Sample output**

```text
Circle    : 78.54
Rectangle : 24.00
Triangle  : 20.00

Through an array of Shape references:
Circle    area = 19.63
Rectangle area = 21.00
Triangle  area = 12.00
Total area = 52.63
```

The same statement `s.area()` runs three different methods because `s` points to a different object each time; the JVM decides at runtime which `area()` to call. In the loop, the concrete method `display()` in `Shape` calls the abstract `area()`, and dynamic dispatch again picks the right subclass version.

---

### P10. `Employee`, `Manager` and `Developer`: overriding, casting and `super`

```java
class Employee {
    protected String name;
    protected double salary;

    Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }

    void work() {
        System.out.println(name + " works for the company");
    }

    void display() {
        System.out.println("Name   : " + name);
        System.out.println("Salary : Rs. " + salary);
    }
}

class Manager extends Employee {
    private int teamSize;

    Manager(String name, double salary, int teamSize) {
        super(name, salary);                    // super(...): parent constructor
        this.teamSize = teamSize;
    }

    @Override
    void work() {                               // overriding
        System.out.println(name + " manages a team of " + teamSize);
    }

    @Override
    void display() {
        super.display();                        // super.method(): reuse the parent's display()
        System.out.println("Team   : " + teamSize + " members");
    }

    void conductMeeting() {                     // Manager-only method
        System.out.println(name + " is conducting a meeting");
    }
}

class Developer extends Employee {
    private String language;

    Developer(String name, double salary, String language) {
        super(name, salary);
        this.language = language;
    }

    @Override
    void work() {
        System.out.println(name + " develops software in " + language);
    }

    @Override
    void display() {
        super.display();
        System.out.println("Skill  : " + language);
    }

    void writeCode() {                          // Developer-only method
        System.out.println(name + " is writing " + language + " code");
    }
}

public class EmployeeDemo {
    public static void main(String[] args) {
        // Upcasting: subclass objects held in Employee references
        Employee e1 = new Manager("Michael Scott", 90000, 12);
        Employee e2 = new Developer("Ryan Howard", 75000, "Java");

        System.out.println("--- Overriding through upcast references ---");
        e1.work();                              // Manager.work()
        e2.work();                              // Developer.work()

        System.out.println("\n--- super.display() inside the overriding display() ---");
        e1.display();
        e2.display();

        System.out.println("\n--- Downcasting to reach subclass-only methods ---");
        Employee[] staff = { e1, e2 };
        for (Employee e : staff) {
            if (e instanceof Manager) {
                Manager m = (Manager) e;        // safe: checked with instanceof first
                m.conductMeeting();
            } else if (e instanceof Developer) {
                Developer d = (Developer) e;
                d.writeCode();
            }
        }

        System.out.println("\n--- Wrong downcast ---");
        try {
            Developer d = (Developer) e1;       // e1 is a Manager, not a Developer
            d.writeCode();
        } catch (ClassCastException ex) {
            System.out.println("ClassCastException: a Manager cannot be cast to Developer");
        }
    }
}
```

**Sample output**

```text
--- Overriding through upcast references ---
Michael Scott manages a team of 12
Ryan Howard develops software in Java

--- super.display() inside the overriding display() ---
Name   : Michael Scott
Salary : Rs. 90000.0
Team   : 12 members
Name   : Ryan Howard
Salary : Rs. 75000.0
Skill  : Java

--- Downcasting to reach subclass-only methods ---
Michael Scott is conducting a meeting
Ryan Howard is writing Java code

--- Wrong downcast ---
ClassCastException: a Manager cannot be cast to Developer
```

| Concept | Where it appears |
|---|---|
| Method overriding | `work()` and `display()` are redefined in both subclasses |
| Upcasting | `Employee e1 = new Manager(...)` |
| Dynamic dispatch | `e1.work()` runs `Manager.work()` |
| `super(...)` | Subclass constructors call `Employee(name, salary)` |
| `super.method()` | Each overriding `display()` first runs `Employee.display()` |
| Downcasting | `(Manager) e`, after an `instanceof` check, to reach `conductMeeting()` |
| Wrong downcast | `(Developer) e1` throws `ClassCastException` |

---

### P11. User-defined package `mypackage`

```java
package mypackage;                          // must be the first statement in the file

public class Student {                      // public: usable outside mypackage
    private int rollNo;
    private String name;
    private String course;

    public Student(int rollNo, String name, String course) {   // public constructor
        this.rollNo = rollNo;
        this.name = name;
        this.course = course;
    }

    public void display() {                 // public method
        System.out.println("Roll no : " + rollNo);
        System.out.println("Name    : " + name);
        System.out.println("Course  : " + course);
    }
}
```

```java
import mypackage.Student;                   // or: import mypackage.*;

public class StudentDetails {
    public static void main(String[] args) {
        Student s1 = new Student(1, "Kelly Kapoor", "MCA");
        Student s2 = new Student(2, "Darryl Philbin", "MBA");

        System.out.println("Student 1");
        s1.display();
        System.out.println("Student 2");
        s2.display();
    }
}
```

```text
project/
├── mypackage/
│   └── Student.java
└── StudentDetails.java
```

Compile and run from the `project` folder:

```text
javac mypackage/Student.java
javac StudentDetails.java
java StudentDetails
```

(On Windows, write `mypackage\Student.java`. If `Student.java` sits directly in `project` instead, `javac -d . Student.java` creates the `mypackage` folder for you.)

**Sample output**

```text
Student 1
Roll no : 1
Name    : Kelly Kapoor
Course  : MCA
Student 2
Roll no : 2
Name    : Darryl Philbin
Course  : MBA
```

`package mypackage;` must be the first statement of `Student.java`, and the class, its constructor and `display()` must all be `public` to be usable from `StudentDetails`, which is outside the package.

---

### P12. `Vehicle` interface implemented by `Car`

```java
interface Vehicle {
    void start();                           // public abstract by default
    void stop();
}

class Car implements Vehicle {
    private String model;
    private int speed;

    Car(String model) {
        this.model = model;
    }

    @Override
    public void start() {
        speed = 20;
        System.out.println(model + " started. Speed: " + speed + " km/h");
    }

    @Override
    public void stop() {
        speed = 0;
        System.out.println(model + " stopped. Speed: " + speed + " km/h");
    }
}

public class VehicleDemo {
    public static void main(String[] args) {
        Vehicle v = new Car("Dodge Charger");    // interface reference, Car object
        v.start();
        v.stop();
    }
}
```

**Sample output**

```text
Dodge Charger started. Speed: 20 km/h
Dodge Charger stopped. Speed: 0 km/h
```

`Car` must implement both `start()` and `stop()`, and as `public` methods; leaving either one out gives *Car is not abstract and does not override abstract method stop() in Vehicle*.

---

### P13. `Printable` and `Showable` implemented by `Document`

```java
interface Printable {
    void print();
}

interface Showable {
    void show();
}

class Document implements Printable, Showable {     // one class, two interfaces
    private String title;
    private int pages;

    Document(String title, int pages) {
        this.title = title;
        this.pages = pages;
    }

    @Override
    public void print() {
        System.out.println("Printing \"" + title + "\": " + pages + " pages sent to the printer");
    }

    @Override
    public void show() {
        System.out.println("Showing \"" + title + "\" on the screen");
    }
}

public class DocumentDemo {
    public static void main(String[] args) {
        Document doc = new Document("Java Notes", 12);
        doc.print();
        doc.show();

        Printable p = doc;                          // the same object seen as a Printable...
        p.print();                                  // (p.show() would not compile)
        Showable s = doc;                           // ...and as a Showable
        s.show();
    }
}
```

**Sample output**

```text
Printing "Java Notes": 12 pages sent to the printer
Showing "Java Notes" on the screen
Printing "Java Notes": 12 pages sent to the printer
Showing "Java Notes" on the screen
```

This is how Java gets multiple inheritance: a class can extend only one class but can implement any number of interfaces. Through a `Printable` reference only `print()` is visible, and through a `Showable` reference only `show()`.

If both interfaces had a `default` method with the same signature, `Document` would have to override it (*class Document inherits unrelated defaults for info() from types Printable and Showable*), and it could pick one version explicitly:

```java
@Override
public void info() {
    Printable.super.info();     // call Printable's default version
}
```

---

### P14. Adapter class for `StudentActivity`

```java
interface StudentActivity {
    void attendLecture();
    void submitAssignment();
    void takeExam();
    void joinSports();
    void attendSeminar();
}

// Adapter class: implements every method with an empty body
abstract class StudentActivityAdapter implements StudentActivity {
    public void attendLecture() { }
    public void submitAssignment() { }
    public void takeExam() { }
    public void joinSports() { }
    public void attendSeminar() { }
}

// Student needs only takeExam(), so it overrides just that one
class Student extends StudentActivityAdapter {
    private String name;

    Student(String name) {
        this.name = name;
    }

    @Override
    public void takeExam() {
        System.out.println(name + " is writing the Java mid-term exam");
    }
}

public class StudentAdapterDemo {
    public static void main(String[] args) {
        StudentActivity s = new Student("Erin Hannon");
        s.takeExam();                               // overridden: prints a message
        s.attendLecture();                          // adapter's empty body: prints nothing
        s.joinSports();                             // adapter's empty body: prints nothing
        System.out.println("attendLecture() and joinSports() also ran, using the adapter's empty bodies");

        // An anonymous subclass of the adapter, overriding a different method
        StudentActivity captain = new StudentActivityAdapter() {
            @Override
            public void joinSports() {
                System.out.println("Andy Bernard joined the cricket team");
            }
        };
        captain.joinSports();
    }
}
```

**Sample output**

```text
Erin Hannon is writing the Java mid-term exam
attendLecture() and joinSports() also ran, using the adapter's empty bodies
Andy Bernard joined the cricket team
```

Implementing `StudentActivity` directly would force `Student` to write all five methods. `StudentActivityAdapter` provides empty bodies for all of them, so `Student` overrides only `takeExam()`. The adapter is declared `abstract` (as AWT's `WindowAdapter` is) because objects of the adapter itself are never useful.

---

### P15. Access modifiers across packages

```java
package company;

public class Employee {
    private double salary = 65000;              // private   : only inside Employee
    int empCode = 101;                          // default   : only inside package company
    protected String department = "Sales";      // protected : package company + subclasses anywhere
    public String name = "Andy Bernard";        // public    : everywhere

    public double getSalary() {                 // public getter: controlled access to private data
        return salary;
    }
}
```

```java
package hr;                                     // a DIFFERENT package

import company.Employee;

public class Manager extends Employee {         // subclass of Employee
    public void showAccess() {
        System.out.println("public    name       : " + name);         // allowed everywhere
        System.out.println("protected department : " + department);   // allowed: inherited by a subclass
        // System.out.println(empCode);         // error: empCode is not public in Employee; cannot be accessed from outside package
        // System.out.println(salary);          // error: salary has private access in Employee
        System.out.println("private   salary     : " + getSalary() + " (only through the public getter)");

        Employee e = new Employee();            // a plain Employee object, not this Manager
        System.out.println("e.name               : " + e.name);       // public: still fine
        // System.out.println(e.department);    // error: department has protected access in Employee
    }

    public static void main(String[] args) {
        new Manager().showAccess();
    }
}
```

```text
project/
├── company/
│   └── Employee.java
└── hr/
    └── Manager.java
```

Compile and run from the `project` folder:

```text
javac company/Employee.java hr/Manager.java
java hr.Manager
```

**Sample output**

```text
public    name       : Andy Bernard
protected department : Sales
private   salary     : 65000.0 (only through the public getter)
e.name               : Andy Bernard
```

Un-commenting the three marked lines gives exactly these compiler errors:

```text
hr/Manager.java:9: error: empCode is not public in Employee; cannot be accessed from outside package
hr/Manager.java:10: error: salary has private access in Employee
hr/Manager.java:15: error: department has protected access in Employee
```

| Member of `Employee` | Inside `Employee` | `Manager` (subclass, other package) via inheritance | Through an `Employee` object in `Manager` |
|---|---|---|---|
| `private salary` | Yes | No (only via the public `getSalary()`) | No |
| default `empCode` | Yes | No | No |
| `protected department` | Yes | **Yes** | No |
| `public name` | Yes | Yes | Yes |

The last column is the subtle point: in another package, a subclass can use a `protected` member only on its **own** objects (through inheritance), not on a separate superclass object such as `e`.

---

### P16. `try`, `catch` and `finally` for an arithmetic exception

```java
import java.util.Scanner;

public class ArithmeticDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter numerator   : ");
        int a = sc.nextInt();
        System.out.print("Enter denominator : ");
        int b = sc.nextInt();

        try {
            int result = a / b;                     // throws ArithmeticException when b is 0
            System.out.println("Result: " + a + " / " + b + " = " + result);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException caught: " + e.getMessage());
            System.out.println("A number cannot be divided by zero.");
        } finally {
            System.out.println("finally block executed");   // runs in both cases
            sc.close();
        }
        System.out.println("Program continues normally");
    }
}
```

**Sample run 1 (no exception)**

```text
Enter numerator   : 20
Enter denominator : 4
Result: 20 / 4 = 5
finally block executed
Program continues normally
```

**Sample run 2 (division by zero)**

```text
Enter numerator   : 20
Enter denominator : 0
ArithmeticException caught: / by zero
A number cannot be divided by zero.
finally block executed
Program continues normally
```

In both runs `finally` executes and the program continues; without the `try`/`catch`, run 2 would end with an `ArithmeticException` stack trace.

---

### P17. Multiple `catch` statements

```java
public class MultipleCatchDemo {
    static void process(String[] data, int index, int divisor) {
        System.out.print("data[" + index + "] / " + divisor + " -> ");
        try {
            String value = data[index];                     // ArrayIndexOutOfBoundsException
            int number = Integer.parseInt(value.trim());    // NullPointerException, NumberFormatException
            System.out.println(number / divisor);           // ArithmeticException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBoundsException: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.out.println("NumberFormatException: " + e.getMessage());
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException: " + e.getMessage());
        } catch (NullPointerException e) {
            System.out.println("NullPointerException: the element is null");
        } catch (Exception e) {                             // most general type goes LAST
            System.out.println("Some other exception: " + e);
        }
    }

    public static void main(String[] args) {
        String[] data = { "100", "abc", null };
        process(data, 0, 4);        // no exception
        process(data, 5, 4);        // index 5 does not exist
        process(data, 1, 4);        // "abc" is not a number
        process(data, 0, 0);        // division by zero
        process(data, 2, 4);        // element is null
    }
}
```

**Sample output**

```text
data[0] / 4 -> 25
data[5] / 4 -> ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 3
data[1] / 4 -> NumberFormatException: For input string: "abc"
data[0] / 0 -> ArithmeticException: / by zero
data[2] / 4 -> NullPointerException: the element is null
```

Each call triggers a different exception, and each is caught by its own `catch` block. `catch (Exception e)` comes last as a safety net; placed first, it would make the specific blocks unreachable, and the code would not compile (*exception ArrayIndexOutOfBoundsException has already been caught*).

---

### P18. Nested `try` blocks at different levels

```java
public class NestedTryDemo {
    public static void main(String[] args) {
        int[] numbers = { 40, 0, 25 };
        String input = "eight";

        try {                                                   // LEVEL 1 (outer)
            System.out.println("Level 1: outer try started");

            try {                                               // LEVEL 2
                System.out.println("Level 2: computing 40 / 0");
                System.out.println(numbers[0] / numbers[1]);
            } catch (ArithmeticException e) {                   // handled at level 2
                System.out.println("Level 2 catch: ArithmeticException (" + e.getMessage() + ")");
            }

            try {                                               // LEVEL 2
                System.out.println("Level 2: parsing \"" + input + "\"");
                try {                                           // LEVEL 3 (innermost)
                    int n = Integer.parseInt(input);
                    System.out.println("Parsed " + n);
                } catch (ArithmeticException e) {               // wrong type: cannot handle it
                    System.out.println("Level 3 catch: never runs");
                } finally {
                    System.out.println("Level 3 finally: runs as the exception passes through");
                }
            } catch (NumberFormatException e) {                 // handled one level up
                System.out.println("Level 2 catch: NumberFormatException (" + e.getMessage() + ")");
            }

            System.out.println("Level 1: reading numbers[3]");
            System.out.println(numbers[3]);                     // no inner try around this line
            System.out.println("Level 1: this line is skipped");
        } catch (ArrayIndexOutOfBoundsException e) {            // handled at level 1
            System.out.println("Level 1 catch: ArrayIndexOutOfBoundsException (" + e.getMessage() + ")");
        } finally {
            System.out.println("Level 1 finally: always runs");
        }
        System.out.println("Program ends normally");
    }
}
```

**Sample output**

```text
Level 1: outer try started
Level 2: computing 40 / 0
Level 2 catch: ArithmeticException (/ by zero)
Level 2: parsing "eight"
Level 3 finally: runs as the exception passes through
Level 2 catch: NumberFormatException (For input string: "eight")
Level 1: reading numbers[3]
Level 1 catch: ArrayIndexOutOfBoundsException (Index 3 out of bounds for length 3)
Level 1 finally: always runs
Program ends normally
```

| Exception | Raised at | Handled at | Why |
|---|---|---|---|
| `ArithmeticException` | Level 2 | Level 2 | Its own `catch` matches |
| `NumberFormatException` | Level 3 | Level 2 | Level 3 catches only `ArithmeticException`, so the exception moves out one level (level 3's `finally` runs on the way) |
| `ArrayIndexOutOfBoundsException` | Level 1 | Level 1 | No inner `try` surrounds the line |

---

### P19. Validating an email with `InvalidEmailException`

This version keeps asking until the address is valid, and checks a few more rules than [P4](#p4-invalidemailexception-for-an-email-address).

```java
import java.util.Scanner;

class InvalidEmailException extends Exception {
    public InvalidEmailException(String message) {
        super(message);
    }
}

class EmailValidator {
    static void validate(String email) throws InvalidEmailException {
        if (email.isEmpty()) {
            throw new InvalidEmailException("email cannot be empty");
        }
        if (Character.isDigit(email.charAt(0))) {
            throw new InvalidEmailException("it cannot start with a digit");
        }
        int at = email.indexOf('@');
        if (at == -1) {
            throw new InvalidEmailException("it must contain @");
        }
        if (at != email.lastIndexOf('@')) {
            throw new InvalidEmailException("it must contain only one @");
        }
        if (at == 0) {
            throw new InvalidEmailException("there must be a name before @");
        }
        String domain = email.substring(at + 1);
        if (!domain.contains(".") || domain.startsWith(".") || domain.endsWith(".")) {
            throw new InvalidEmailException("the part after @ must look like example.com");
        }
    }
}

public class EmailRegistration {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {                                      // keep asking until the email is valid
            System.out.print("Enter your email: ");
            String email = sc.nextLine().trim();
            try {
                EmailValidator.validate(email);
                System.out.println("Registered successfully with " + email);
                break;
            } catch (InvalidEmailException e) {
                System.out.println("InvalidEmailException: " + e.getMessage() + ". Try again.");
            }
        }
        sc.close();
    }
}
```

**Sample run**

```text
Enter your email: 7up@example.com
InvalidEmailException: it cannot start with a digit. Try again.
Enter your email: angela.example.com
InvalidEmailException: it must contain @. Try again.
Enter your email: angela@@example.com
InvalidEmailException: it must contain only one @. Try again.
Enter your email: angela@example
InvalidEmailException: the part after @ must look like example.com. Try again.
Enter your email: angela.martin@example.com
Registered successfully with angela.martin@example.com
```

Each rule that fails throws the same custom exception with a different message; the loop catches it, prints the reason and asks again, and `break` ends the loop once `validate()` returns without throwing.

---

### P20. `InSufficientFundException` on withdrawal

```java
import java.util.Scanner;

class InSufficientFundException extends Exception {
    public InSufficientFundException(String message) {
        super(message);
    }
}

class Account {
    private double balance;

    Account(double balance) {
        this.balance = balance;
    }

    void withdraw(double amount) throws InSufficientFundException {
        if (amount > balance) {
            throw new InSufficientFundException("Cannot withdraw Rs. " + amount
                    + "; available balance is Rs. " + balance);
        }
        balance -= amount;
    }

    double getBalance() {
        return balance;
    }
}

public class WithdrawDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Account acc = new Account(5000);
        System.out.println("Available balance: Rs. " + acc.getBalance());
        System.out.print("Enter amount to withdraw: ");
        double amount = sc.nextDouble();

        try {
            acc.withdraw(amount);
            System.out.println("Withdrawal successful. Remaining balance: Rs. " + acc.getBalance());
        } catch (InSufficientFundException e) {
            System.out.println("InSufficientFundException: " + e.getMessage());
        } finally {
            sc.close();
        }
    }
}
```

**Sample run 1 (enough balance)**

```text
Available balance: Rs. 5000.0
Enter amount to withdraw: 3000
Withdrawal successful. Remaining balance: Rs. 2000.0
```

**Sample run 2 (amount greater than balance)**

```text
Available balance: Rs. 5000.0
Enter amount to withdraw: 8000
InSufficientFundException: Cannot withdraw Rs. 8000.0; available balance is Rs. 5000.0
```

`withdraw()` throws the custom exception instead of quietly refusing, so the caller has to deal with the failure; `finally` closes the `Scanner` in both cases. [P8](#p8-insufficientfundexception-with-the-additional-amount-required) extends the same idea by storing the shortfall inside the exception.

---

## Quick revision sheet

**Overloading vs overriding**

| | Overloading | Overriding |
|---|---|---|
| Parameters | Must differ | Must be the same |
| Return type | Free (but not the only difference) | Same or covariant |
| Inheritance | Not needed | Needed |
| Binding | Compile time (static) | Runtime (dynamic) |
| `static` / `final` / `private` | Can be overloaded | Cannot be overridden |

**Casting:** upcasting (`Animal a = new Dog();`) is implicit and always safe. Downcasting (`Dog d = (Dog) a;`) is explicit; guard it with `instanceof` or risk a `ClassCastException`. Casting between sibling classes does not compile. Dynamic method dispatch applies only to overridden instance methods, never to fields or `static` methods.

**Keywords**

| Keyword | On a variable | On a method | On a class | Also |
|---|---|---|---|---|
| `this` | `this.x`: the current object's field | `this.m()` | — | `this(...)` calls another constructor; `return this` |
| `super` | `super.x`: the parent's hidden field | `super.m()`: the parent's version | — | `super(...)` calls the parent constructor (inserted automatically if omitted) |
| `final` | Constant (assign once) | Cannot be overridden | Cannot be extended | Blank final: assigned once in the constructor |
| `static` | One copy shared by all objects | Called without an object; uses only static members | Static nested class | Static block runs once, when the class loads |

**Access modifiers:** `private` (same class) < default (same package) < `protected` (same package + subclasses anywhere) < `public` (everywhere). A top-level class can only be `public` or default.

**Abstract class vs interface:** one `extends` vs many `implements` · constructors vs none · any fields vs only `public static final` constants · abstract + concrete methods vs abstract + `default`/`static` (Java 8) + `private` (Java 9) · IS-A vs CAN-DO. Neither can be instantiated.

**Strings**

| | `String` | `StringBuffer` | `StringBuilder` |
|---|---|---|---|
| Mutable | No | Yes | Yes |
| Thread-safe | Yes (immutable) | Yes (synchronized) | No |
| Many modifications | Slow (new object each time) | Fast | Fastest |
| `equals()` compares | Contents | References | References |
| Since | Java 1.0 | Java 1.0 | Java 5 |

Literals live in the String Constant Pool; `new String(...)` always creates a new heap object; use `equals()`, not `==`, to compare contents. `StringBuffer` capacity: 16 by default, and it grows to (old × 2) + 2.

**Wrapper classes:** `Byte`, `Short`, `Integer`, `Long`, `Float`, `Double`, `Character`, `Boolean`. They are needed for collections and generics, `null` values and utility methods (`parseInt`, `valueOf`, `MAX_VALUE`). Autoboxing: `Integer i = 5;`. Unboxing: `int n = i;`. Only −128 to 127 are cached, so compare with `equals()`.

**Packages:** `package name;` must be the first statement → make classes `public` → `javac -d . File.java` → `import name.Class;` or `import name.*;` → run from the folder that contains the package folder.

**Adapter classes:** empty implementations of listener interfaces (`WindowAdapter`, `MouseAdapter`, `KeyAdapter`, `FocusAdapter`, `ComponentAdapter`, `ContainerAdapter`, `MouseMotionAdapter`). Extend one and override only the methods you need.

**Exceptions**

- `Throwable` → `Error` (do not catch) and `Exception`; `Exception` → `RuntimeException` (**unchecked**) and everything else (**checked**: handle or declare).
- `try` must be followed by `catch` or `finally` · catch blocks go from specific to general · `finally` always runs (unless the JVM exits).
- `throw new X("msg");` throws one object, inside a method · `throws X, Y` declares, in the signature.
- Multiple catch: the first matching block runs · multi-catch `catch (A | B e)` since Java 7, for unrelated types only.
- Nested try: an unmatched exception moves to the outer try's catches, then to the caller.
- Custom exception: `class MyEx extends Exception` → constructor calling `super(msg)` → `throw` → `throws` → `catch` and `e.getMessage()`.
