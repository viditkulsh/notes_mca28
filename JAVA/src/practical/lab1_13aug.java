package practical;
import java.util.Scanner;

public class lab1_13aug {
    public static void main(String[] args) {

        //Input from user:
        Scanner sc = new Scanner(System.in);

        // Q1 Prgm to accept stud name, roll, and marks. Print them.
        /*String name = "Tyrion Lannister";
        int roll = 12345;
        double marks = 89.5;

        System.out.println("Name: " + name);
        System.out.println("Roll: " + roll);
        System.out.println("Marks: " + marks);*/

        // Q2 Prgm to accept 2 numb and print their +, -, *, /.
        int num1 = 10;
        int num2 = 5;
        System.out.println("Sum: " + (num1 + num2));
        System.out.println("Difference: " + (num1 - num2));
        System.out.println("Product: " + (num1 * num2));
        System.out.println("Quotient: " + (num1 / num2));
    }
}