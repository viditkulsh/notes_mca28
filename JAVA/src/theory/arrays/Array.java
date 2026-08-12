package theory.arrays;

// NOTE: this file is now Array.java (capital A) to match `public class Array`.
// As array.java it compiled only via `java array.java`; `javac` rejected it with
// "class Array is public, should be declared in a file named Array.java".
public class Array {
    public static void main(String[] args) {
        // 1. declare an array of integers
        int[] numbers = new int[5];

        // 2. assign values to the array elements
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;

        // 3. access and print the array elements
        System.out.println("Array elements:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("  numbers[" + i + "] = " + numbers[i]);
        }

        // 4. calculate the sum of the array elements
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        System.out.println("Sum of array elements: " + sum);
    }
}
