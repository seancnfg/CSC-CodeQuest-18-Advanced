import java.util.*;
import java.io.*;
import java.lang.*;

public class Prob00 {
	public static void main(String[] args) {
	    try {
            Scanner in = new Scanner(new File("Prob00.in.txt"));
            //Scanner in = new Scanner(System.in);
            int x = in.nextInt();
            for(int i = 0; i < x; i++){
                int a = in.nextInt();
                String dummy = in.nextLine();
                for(int j = 0; j < a; j++) {
                    String str = in.nextLine();
                    System.out.println(str);
                }

            }
        } catch (Exception e) {
            e.printStackTrace();
        }
	}
}
