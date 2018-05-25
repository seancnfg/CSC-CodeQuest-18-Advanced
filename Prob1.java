import java.util.*;
import java.io.*;
import java.lang.*;

public class Prob02 {
	public static void main(String[] args) {
	    try {
            Scanner in = new Scanner(new File("Prob00.in.txt"));
            //Scanner in = new Scanner(System.in);
            int x = in.nextInt();
            String[] vowels = new String[]{"a","e","i","o","u"};
            for(int i = 0; i < x; i++){
            	int vCheck = 0;

            	String str = in.nextLine();
            	String[] words = str.split(" ");
            	for(int j = 0; j < words.length;j++) {
            		for(int k = 0; k<vowels.length;k++) {
	            		if(words[j].contains(vowels[k])) {
	            			vCheck ++;
	            		}

            		}
            	}
            	System.out.println(vCheck);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
	}
}
