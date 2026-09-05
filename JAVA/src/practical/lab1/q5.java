package practical.lab1;
// WAP to create a class car with data members brand, model, and price. Create an object and display its details.

class Car {
    String brand;
    String model;
    double price;
}

public class q5 {
    public static void main(String[] args) {
        Car c = new Car();
        c.brand = "Dodge";
        c.model = "Charger";
        c.price = 3500000;

        System.out.println("Brand: " + c.brand);
        System.out.println("Model: " + c.model);
        System.out.println("Price: " + c.price);
    }
}
