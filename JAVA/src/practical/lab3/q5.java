package practical.lab3;
// WAP to demonstrate method overriding using Person and Manager classes and the super keyword.

class Person {
    String name;

    Person(String name) {
        this.name = name;
    }

    void display() {
        System.out.println("Name: " + name);
    }
}

class Manager extends Person {
    String department;

    Manager(String name, String department) {
        super(name); // calls Person constructor
        this.department = department;
    }

    // Overriding display() of Person
    void display() {
        super.display(); // calls Person's display()
        System.out.println("Department: " + department);
    }
}

public class q5 {
    public static void main(String[] args) {
        Person p = new Person("Jim Halpert");
        p.display();

        System.out.println();

        Manager m = new Manager("Michael Scott", "Sales");
        m.display();
    }
}
