package practical.lab3;
// WAP to create an account class with account details and methods for deposit, withdraw, abd displaying the current balance. 
import java.util.Scanner;

public class q3 {

    // Account details
    int accNumber;
    String name;
    int balance;

    // Method to store account details
    void account(Scanner Sc) {

        System.out.println("===== ENTER ACCOUNT DETAILS =====");

        System.out.print("Account Number: ");
        accNumber = Sc.nextInt();
        Sc.nextLine(); // Clear the newline

        System.out.print("Account Holder Name: ");
        name = Sc.nextLine();

        System.out.print("Current Balance: ");
        balance = Sc.nextInt();

        System.out.println("\nAccount created successfully!");
    }

    // Method to display account details
    void displayAccount() {

        System.out.println("\n===== ACCOUNT DETAILS =====");
        System.out.println("Account Number: " + accNumber);
        System.out.println("Account Holder Name: " + name);
        System.out.println("Current Balance: " + balance);
    }

    // Method to deposit money
    void deposit(Scanner Sc) {

        System.out.print("\nEnter Amount to Deposit: ");
        int amount = Sc.nextInt();

        balance = balance + amount;

        System.out.println("Amount Deposited: " + amount);
        System.out.println("Updated Balance: " + balance);
    }

    // Method to withdraw money
    void withdraw(Scanner Sc) {

        System.out.print("\nEnter Amount to Withdraw: ");
        int amount = Sc.nextInt();

        if (amount <= balance) {
            balance = balance - amount;

            System.out.println("Amount Withdrawn: " + amount);
            System.out.println("Updated Balance: " + balance);
        } else {
            System.out.println("Insufficient Balance!");
        }
    }

    // Main method
    public static void main(String[] args) {

        Scanner Sc = new Scanner(System.in);

        // Create account object
        q3 obj = new q3();

        // Store account details
        obj.account(Sc);

        int choice;

        // Menu
        do {

            System.out.println("\n===== BANK MENU =====");
            System.out.println("1. View Account Details");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");

            System.out.print("Enter your choice: ");
            choice = Sc.nextInt();

            switch (choice) {

                case 1:
                    obj.displayAccount();
                    break;

                case 2:
                    obj.deposit(Sc);
                    break;

                case 3:
                    obj.withdraw(Sc);
                    break;

                case 4:
                    System.out.println("\nThank you for using the banking system!");
                    break;
            }

        } while (choice != 4);

        Sc.close();
    }
}