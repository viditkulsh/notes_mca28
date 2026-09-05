package practical.lab2;
// Q3 WAP to accept a number and check whether it is even or odd.

import java.util.Scanner;

public class q3 {
    public static void main(String[] args) {
        System.out.println("Enter num: ");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        if (num % 2 == 0) {
            System.out.println(num + " is even.");
        } else {
            System.out.println(num + " is odd.");

        }
    }
}