package theory.util;

/**
 * A helper class living in a DIFFERENT package from the code that uses it.
 *
 * Note the two `public` keywords below — they are not decoration:
 *   - `public class`  makes the class visible outside package theory.util
 *   - `public static` makes each method visible outside the package
 * Drop either one and theory.arrays.ArrayDemo will fail to compile.
 */
public class Stats {

    public static int sum(int[] values) {
        int total = 0;
        for (int value : values) {
            total += value;
        }
        return total;
    }

    public static double average(int[] values) {
        if (values.length == 0) {
            return 0.0;
        }
        return (double) sum(values) / values.length;
    }

    public static int max(int[] values) {
        int highest = values[0];
        for (int value : values) {
            if (value > highest) {
                highest = value;
            }
        }
        return highest;
    }

    public static int min(int[] values) {
        int lowest = values[0];
        for (int value : values) {
            if (value < lowest) {
                lowest = value;
            }
        }
        return lowest;
    }
}
