import java.util.Scanner;

class EnggReversort
{
    public static void main(String [] args)
    {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
         for(int i = 0; i < T; i ++)
         {
            int N = sc.nextInt();
            int C = sc.nextInt();

            if (C < (N - 1) && C > (N * (N - 1)/2) - 1)
            {
                System.out.println("Case #" + i + ": IMPOSSIBLE");
            }
            else
            {
               
                String result = ConstructArray(N, C, 1);
                System.out.println("Case #" + i + ": " + result);
            }
         }

         sc.close();
    }

    public static String ConstructArray(int N, int C, int M)
    {
        if (N == 1)
        {
            return String.valueOf(M);
        }
        else 
        {
            if ((C - 1) >= (N - 2) && (C - 1) <= (N * (N - 1) / 2) - 1) 
            {
                return M + " " + ConstructArray(N - 1, C - 1, M + 1);
            }
            else 
            {
                int delta = C - (N * (N - 1) / 2) + 1;
                String smallerArray = ConstructArray(N - 1, C - delta, M + 1);

                String[] smallArr = smallerArray.split(" ");
                String[] newArr = new String[N];

            
                newArr[0] = String.valueOf(M);
                System.arraycopy(smallArr, 0, newArr, 1, smallArr.length);

            
            for (int i = 0, j = delta - 1; i < j; i++, j--) {
                String temp = newArr[i];
                newArr[i] = newArr[j];
                newArr[j] = temp;
            }

            
            return String.join(" ", newArr);
            }
        }
    }
}