// Que. 1) Write a Java program to create a user-defined exception InvalidMarksException and demonstrate nested try blocks and multiple catch statements. If the marks entered are greater than 100 or less than 0, throw the user-defined exception and display an appropriate message. Also demonstrate ArithmeticException using division by zero.
// Que. 1
// Demonstrate user-defined exception, nested try blocks
// and multiple catch statements.

import java.util.Scanner;

// User-defined exception
class InvalidMarksException extends Exception {

    public InvalidMarksException(String message) {
        super(message);
    }
}

public class q2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.print("Enter marks: ");
            int marks = sc.nextInt();

            // Check for invalid marks
            if (marks > 100 || marks < 0) {
                throw new InvalidMarksException(
                    "Invalid marks! Marks must be between 0 and 100."
                );
            }

            System.out.println("Valid marks: " + marks);

            // Nested try block
            try {
                System.out.println("\nPerforming division...");
                int result = marks / 0;
                System.out.println("Result: " + result);
            }
            catch (ArithmeticException e) {
                System.out.println(
                    "ArithmeticException: Cannot divide by zero."
                );
            }
        }

        // Catch user-defined exception
        catch (InvalidMarksException e) {
            System.out.println("InvalidMarksException: " + e.getMessage());
        }

        // Catch invalid input
        catch (java.util.InputMismatchException e) {
            System.out.println("Invalid input! Please enter an integer.");
        }

        finally {
            sc.close();
        }
    }
}