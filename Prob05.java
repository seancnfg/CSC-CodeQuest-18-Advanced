import java.util.*;
import java.io.*;
import java.lang.*;

public class Prob05 {
	public static void main(String[] args) {
	    try {
            Scanner in = new Scanner(new File("Prob05.in.txt"));
            //Scanner in = new Scanner(System.in);
            int x = in.nextInt();

            for(int i = 0; i < x; i++){
            int a = in.nextInt();
            int z = a;
            int count = 1;
            while(a != 1) {
            	if(a % 2 == 0) {
            		a = a/2;
            		count++;
            	}else {
            		a = 3*a + 1;
            		count++;

            	}


            }

            System.out.println(z+":"+count);

            }
        } catch (Exception e) {
            e.printStackTrace();
        }
	}
}
