package practical;
import java.util.Scanner;
public class lab3_27aug {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
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
       /*System.out.println("Input Value:");
       int n1 = sc.nextInt();
       int n2 = sc.nextInt();
       int n3 = sc.nextInt();
       int largest = n1;

        if (n1 >= n2 && n1 >= n3){
            largest = n1;
            System.out.println("Largest Num: n1");
        } else if (n2 >= n1 && n2 >= n3){
            largest = n2;
            System.out.println("Largest Num: n2");
        } else {
            largest = n3;
            System.out.println("Largest Num: n3");
        }
        System.out.println("Largest Num: " + largest);*/

        //Q6 Write a Java program to check whether a given number is prime or not.
        System.out.println("Input Value:");
        int num = sc.nextInt();
        boolean isPrime = true;
        if (num <= 1) {
            isPrime = false;
        } else {
            for (int i = 2; i <= Math.sqrt(num); i++) {
                if (num % i == 0) {
                    isPrime = false;
                    break;
                }
            }
        }
        if (isPrime) {
            System.out.println(num + " is a prime number.");
        } else {
            System.out.println(num + " is not a prime number.");
        }

        //Q7. Write a Java program to accept a number and calculate its factorial.
        /*System.out.println("Input Value:");
        int num = sc.nextInt();
        long factorial = 1;
        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }
        System.out.println("Factorial of " + num + " is: " + factorial);*/

        //Q8. Write a Java program to accept n and print the first n Fibonacci numbers.
        System.out.println("Input Value:");
        int n = sc.nextInt();
        int f1 = 0, f2 = 1, f3;
        System.out.print("First " + n + " Fibonacci numbers: ");
        for (int i = 0; i < n; i++) {
            System.out.print(f1 + " ");
            f3 = f1 + f2;
            f1 = f2;
            f2 = f3;
        }
        System.out.println();
    }
}
