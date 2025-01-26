
import java.util.Scanner;
public class Reversort{
    public static void main(String [] args)
    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for(int c = 0; c < T; c++)
        {
            int N = sc.nextInt();
            Integer [] array = new Integer [N];

            for(int i = 0;i < N;i++)
            {
                array[i] = sc.nextInt();
            }

            int cost = reversort(array);
            System.out.println("Case " + (c+1) + " : " + cost);
        }

        sc.close();
    }

    public static int reversort(Integer[] arr)
    {
        int cost = 0;

        for(int i = 0; i < arr.length - 1; i++)
        {
            int min_index = i;
            for(int j = i+1; j < arr.length; j++)
            {
                if(arr[j] < arr[min_index])
                {
                    min_index = j;
                }

            }

            reverse(arr, i, min_index);
            cost = cost + (min_index - i + 1);
        }

        return cost;
    }

    public static void reverse(Integer[] arr, int start, int end)
    {
        while (start < end)
        {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start ++;
            end --;
        }
    }
}