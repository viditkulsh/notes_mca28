package theory.arrays;

// Importing a class from ANOTHER package. Without this line you would have to
// write the fully-qualified name every time: theory.util.Stats.sum(marks)
import theory.util.Stats;

// java.util is part of the JDK, imported exactly the same way.
import java.util.Arrays;

public class ArrayDemo {

    public static void main(String[] args) {

        // 1. Declaring and initialising arrays
        System.out.println("declaration:");
        int[] marks = { 78, 85, 91, 66, 72 };          // literal initialiser
        int[] empty = new int[5];                       // defaults to all zeros
        String[] subjects = { "JAVA", "ADBMS", "RM" };

        System.out.println("  marks    = " + Arrays.toString(marks));
        System.out.println("  empty    = " + Arrays.toString(empty));
        System.out.println("  subjects = " + Arrays.toString(subjects));
        System.out.println("  marks.length = " + marks.length);   // length is a field, not a method

        // 2. Indexing — always 0-based, so the last index is length - 1
        System.out.println("\nindexing:");
        System.out.println("  first = " + marks[0]);
        System.out.println("  last  = " + marks[marks.length - 1]);

        // 3. Calling into the theory.util package
        System.out.println("\nusing theory.util.Stats:");
        System.out.println("  sum     = " + Stats.sum(marks));
        System.out.println("  average = " + Stats.average(marks));
        System.out.println("  max     = " + Stats.max(marks));
        System.out.println("  min     = " + Stats.min(marks));

        // 4. Useful java.util.Arrays helpers
        System.out.println("\njava.util.Arrays helpers:");
        int[] sorted = Arrays.copyOf(marks, marks.length);   // copy first — sort() mutates!
        Arrays.sort(sorted);
        System.out.println("  sorted   = " + Arrays.toString(sorted));
        System.out.println("  original = " + Arrays.toString(marks) + "  (unchanged)");

        // 5. Two-dimensional arrays
        System.out.println("\n2D array:");
        int[][] grid = {
            { 1, 2, 3 },
            { 4, 5, 6 },
            { 7, 8, 9 }
        };
        for (int[] row : grid) {
            for (int cell : row) {
                System.out.print("  " + cell);
            }
            System.out.println();
        }

        // 6. The classic mistake — going past the end of the array
        System.out.println("\nbounds checking:");
        try {
            System.out.println(marks[99]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("  caught ArrayIndexOutOfBoundsException: " + e.getMessage());
        }
    }
}
