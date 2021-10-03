/*https://codeforces.com/problemset/problem/705/A*/

public class Hulk
{

    public static void main(String[] args) 
    { 
        int m,i;
        Scanner sc = new Scanner(System.in);
        m = sc.nextInt();
        for (i = 0; i < m; i++) 
        {
            if (i % 2 == 0) 
            {
                System.out.print("I hate ");
            } 
            else 
            {
                System.out.print("I love ");
            }
            if (i != (m - 1)) 
            {
                System.out.print("that ");
                System.out.println();
            }
            else
            {
                System.out.print("it ");
                System.out.print();
            }
        }
    }
}
