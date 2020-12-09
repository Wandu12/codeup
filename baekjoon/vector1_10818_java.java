import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner sc = new Scanner(System.in);
     
        int num = sc.nextInt(); // 정수 갯수 입력
        int[] n = new int [num];
      
        for(int i=0; i<n.length; i++) {
         n[i] = sc.nextInt();
      }
      
        Arrays.sort(n);
     
        int min = n[0];
        int max = n[n.length-1];

        System.out.print(min + " " + max);

	}
}
