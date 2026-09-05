package practical.lab1;
// WAP to create a class students with data members name and roll number. Create an object, assign values, and display the details.

class Student {
    String name;
    int rollNo;
}

public class q3 {
    public static void main(String[] args) {
        Student s = new Student();
        s.name = "Monica Geller";
        s.rollNo = 12;

        System.out.println("Student Name: " + s.name);
        System.out.println("Roll Number: " + s.rollNo);
    }
}
