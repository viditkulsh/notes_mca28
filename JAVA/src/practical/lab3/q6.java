package practical.lab3;
// WAP to demonstrate the user of the final keyword with a final variable and a final method.

class Show {
    // final variable - its value cannot be changed
    final String NAME = "Friends";

    // final method - it cannot be overridden by a subclass
    final void display() {
        System.out.println("Show Name: " + NAME);
    }
}

class Episode extends Show {
    void episodeInfo() {
        // NAME = "Seinfeld"; // error: cannot assign a value to final variable
        System.out.println("Episode: The One With The Final Keyword");
    }
}

public class q6 {
    public static void main(String[] args) {
        Episode e = new Episode();
        e.display();     // inherited final method
        e.episodeInfo();
    }
}
