// The package declaration MUST be the first statement in the file,
// and it MUST match this file's folder path relative to the source root:
//     src/theory/loops/Loop.java  ->  package theory.loops;
package theory.loops;

public class Loop {

    public static void main(String[] args) {

        // 1. for loop — use when the number of iterations is known up front
        System.out.println("for loop:");
        for (int i = 1; i <= 5; i++) {
            System.out.println("  i = " + i);
        }

        // 2. while loop — checks the condition BEFORE each pass,
        //    so the body may run zero times
        System.out.println("\nwhile loop:");
        int n = 5;
        while (n > 0) {
            System.out.println("  n = " + n);
            n--;
        }

        // 3. do-while loop — checks the condition AFTER each pass,
        //    so the body always runs at least once
        System.out.println("\ndo-while loop:");
        int count = 10;
        do {
            System.out.println("  runs once even though count = " + count + " fails the test");
            count++;
        } while (count < 5);

        // 4. enhanced for ("for-each") — iterates an array without an index
        System.out.println("\nfor-each loop:");
        int[] marks = { 78, 85, 91, 66, 72 };
        int total = 0;
        for (int mark : marks) {
            System.out.println("  mark = " + mark);
            total += mark;
        }
        System.out.println("  average = " + (total / marks.length));

        // 5. break and continue — alter the normal flow of a loop
        System.out.println("\nbreak and continue:");
        for (int i = 1; i <= 10; i++) {
            if (i % 2 != 0) {
                continue;   // skip the rest of this pass, go to i++
            }
            if (i > 8) {
                break;      // exit the loop entirely
            }
            System.out.println("  even number = " + i);
        }

        // 6. nested loops — a multiplication table
        System.out.println("\nnested loops:");
        for (int row = 1; row <= 3; row++) {
            for (int col = 1; col <= 3; col++) {
                System.out.print("  " + (row * col));
            }
            System.out.println();
        }
    }
}
