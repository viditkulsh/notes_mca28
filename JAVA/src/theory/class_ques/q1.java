// Write a Java Program to accept the marks of a student from the command line argument, calculate and display the percentage.
// Use
// 1. Try block to perform the calculation
// 2. Catch block to handle the exception if the user enters invalid input
// 3. Finally, block to display a message that the program has completed.

public class StudentPercentage {
    public static void main(String[] args) {

        try {
            // Accept marks from command line arguments
            int marks1 = Integer.parseInt(args[0]);
            int marks2 = Integer.parseInt(args[1]);
            int marks3 = Integer.parseInt(args[2]);
            int marks4 = Integer.parseInt(args[3]);
            int marks5 = Integer.parseInt(args[4]);

            // Calculate total and percentage
            int total = marks1 + marks2 + marks3 + marks4 + marks5;
            float percentage = (total / 500.0f) * 100;

            // Display result
            System.out.println("Total Marks: " + total);
            System.out.println("Percentage: " + percentage + "%");
        }

        catch (Exception e) {
            // Handle invalid input
            System.out.println("Invalid input! Please enter valid marks.");
        }

        finally {
            // Program completion message
            System.out.println("Program has completed.");
        }
    }
}