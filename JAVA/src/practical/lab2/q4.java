package practical.lab2;
// Q4 WAP to check whether a given number is positive, negative, or odd.

import java.util.Scanner;

public class q4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        if (num > 0) {
            System.out.println(num + " is positive.");
        } else if (num < 0) {
            System.out.println(num + " is negative.");
        } else {
            System.out.println("The number is zero.");
        }

        if (num % 2 != 0) {
            System.out.println(num + " is odd.");
        } else {
            System.out.println(num + " is even.");
        }

        sc.close();
    }
}
