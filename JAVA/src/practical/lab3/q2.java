package practical.lab3;
// WAP to create a Product class with product name and price, and use methods with arguments to calculate the discount and final price.
import java.util.Scanner;
public class q2 {
    void prod(Scanner Sc){
        System.out.println("Enter Prod Name:");
        String nam = Sc.nextLine();
        System.out.println("Enter Prod Price:");
        int price = Sc.nextInt();

        discount(nam, price);

    }
    void discount(String nam, int price){
        System.out.println("Price after 5% Discount is:");
        System.out.println(price - (price * 5/100));
    }
    public static void main(String[] args) {
        Scanner Sc = new Scanner(System.in);
        q2 obj = new q2();
        try {
            obj.prod(Sc);
        } finally {
            Sc.close();
        }
    }
}
