import java.util.Arrays;
import java.util.Scanner;

public class TroubleSort {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int tcase = sc.nextInt();

        for(int i = 0; i < tcase; i++) {

            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int j = 0; j < n; j++) {
                arr[j] = sc.nextInt();
            }

            int oddSize = (n + 1) / 2;
            int evenSize = n / 2;
            int[] odd = new int[oddSize];
            int[] even = new int[evenSize];

            int oddIndex = 0, evenIndex = 0;
            for(int j = 0; j < n; j++) {
                if(j % 2 == 0) {
                    even[evenIndex++] = arr[j];
                } else {
                    odd[oddIndex++] = arr[j];
                }
            }

            Arrays.sort(even);
            Arrays.sort(odd);

            int[] sorted = new int[n];
            oddIndex = 0;
            evenIndex = 0;
            for(int j = 0; j < n; j++) {
                if(j % 2 == 0) {
                    sorted[j] = even[evenIndex++];
                } else {
                    sorted[j] = odd[oddIndex++];
                }
            }

            int flag = -1;
            for (int j = 0; j < n - 1; j++) {
                if(sorted[j] > sorted[j + 1]) {
                    flag = j;
                    break;
                }
            }

            if (flag == -1) {
                System.out.println("Case #" + (i + 1) + ": OK");
            } else {
                System.out.println("Case #" + (i + 1) + ": " + flag);
            }
        }
        sc.close();
    }
}