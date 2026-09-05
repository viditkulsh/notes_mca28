package practical.lab1;

// WAP create a class Employee with data members employee ID, employee name, and salary. Create two objects and display their details.

class Employee {
    int empId;
    String empName;
    double salary;

    void display() {
        System.out.println("Employee ID: " + empId);
        System.out.println("Employee Name: " + empName);
        System.out.println("Salary: " + salary);
        System.out.println();
    }
}

public class q4 {
    public static void main(String[] args) {
        Employee e1 = new Employee();
        e1.empId = 101;
        e1.empName = "Michael Scott";
        e1.salary = 90000;

        Employee e2 = new Employee();
        e2.empId = 102;
        e2.empName = "Dwight Schrute";
        e2.salary = 65000;

        e1.display();
        e2.display();
    }
}
