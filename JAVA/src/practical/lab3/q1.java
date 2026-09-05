package practical.lab3;
import java.util.Scanner;
// Q1 WAP to create an Employee class with instance variable and methods to accept and display employee details. Emp no, name, salary dept.
public class q1 {
    void acceptDetails(Scanner scanner) {
        System.out.print("Enter Employee Number: ");
        int empNo = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        System.out.print("Enter Employee Name: ");
        String empName = scanner.nextLine();
        System.out.print("Enter Employee Salary: ");
        double empSalary = scanner.nextDouble();
        scanner.nextLine(); // Consume newline
        System.out.print("Enter Employee Department: ");
        String empDept = scanner.nextLine();

        displayDetails(empNo, empName, empSalary, empDept);
    }

    void displayDetails(int empNo, String empName, double empSalary, String empDept) {
        System.out.println("Employee Details:");
        System.out.println("Employee Number: " + empNo);
        System.out.println("Employee Name: " + empName);
        System.out.println("Employee Salary: " + empSalary);
        System.out.println("Employee Department: " + empDept);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        q1 employee = new q1();
        try {
            employee.acceptDetails(scanner);
        } finally {
            scanner.close();
        }
    }
}
