package practical;
import java.util.Scanner;
public class aug13 {
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
        /*int num1 = 10;
        int num2 = 5;
        System.out.println("Sum: " + (num1 + num2));
        System.out.println("Difference: " + (num1 - num2));
        System.out.println("Product: " + (num1 * num2));
        System.out.println("Quotient: " + (num1 / num2));*/

        // Q3 accept num and check it is even or odd.
        /*int num = 7;
        if (num % 2 == 0) {
            System.out.println(num + " is even.");
        } else {
            System.out.println(num + " is odd.");
        }*/

        // Q4 prgm to check if num is -ve, +ve or 0.
        /*int num = 23456;
        if (num > 0){
            System.out.println(num + " is positive.");
        } else if (num < 0) {
            System.out.println(num + " is negative.");
        } else {
            System.out.println(num + " is zero.");
        }*/


       // Q5 prgm to acpt 3 num and find the largest.
       System.out.println("Input Value:");
       int n1 = sc.nextInt();
       int n2 = sc.nextInt();
       int n3 = sc.nextInt();

        if (n1 > n2){
            if (n1 > n3){
                System.out.println( "Largest Num: " + n1);
            }else{
                System.out.println("Largest Num: " + n3);
            }
        }
        else{
            System.out.println("Largest Num: " + n2);
        }
        
    }
}
