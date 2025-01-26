import java.util.*;

public class NumberGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt(); // Number of test cases

        // Golden ratio
        double golden = (1 + Math.sqrt(5)) / 2;

        for (int j = 1; j <= T; j++) {

            // Read input
            int a1 = scanner.nextInt();
            int a2 = scanner.nextInt();
            int b1 = scanner.nextInt();
            int b2 = scanner.nextInt();

            int ans = 0;

            for (int b = b1; b <= b2; b++) {
                int lowerThreshold = (int) Math.floor(golden * b);
                int upperThreshold = (int) Math.floor((golden - 1) * b);

                if (lowerThreshold < a1 || upperThreshold > a2) {
                    // All games are winning if thresholds are completely out of range
                    ans += (a2 - a1 + 1);
                } else {
                    // Count explicitly the number of winning games
                    ans += Math.max(0, a2 - lowerThreshold);
                    ans += Math.max(0, upperThreshold - a1);
                }
            }

            System.out.println("Case #" + j + ": " + ans);
        }

        scanner.close();
    }
}