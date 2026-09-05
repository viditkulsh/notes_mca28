package practical.lab3;
// WAP to create a Flight class and use parameteruze constructor to initialize and display flight details.

class Flight {
    int flightNo;
    String airline;
    String source;
    String destination;
    double fare;

    // Parameterized constructor
    Flight(int flightNo, String airline, String source, String destination, double fare) {
        this.flightNo = flightNo;
        this.airline = airline;
        this.source = source;
        this.destination = destination;
        this.fare = fare;
    }

    void display() {
        System.out.println("Flight Number: " + flightNo);
        System.out.println("Airline: " + airline);
        System.out.println("From: " + source);
        System.out.println("To: " + destination);
        System.out.println("Fare: " + fare);
        System.out.println();
    }
}

public class q4 {
    public static void main(String[] args) {
        Flight f1 = new Flight(101, "Oceanic Airlines", "Sydney", "Los Angeles", 45000);
        Flight f2 = new Flight(815, "Air India", "Pune", "Delhi", 6500);

        f1.display();
        f2.display();
    }
}
