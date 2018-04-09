import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;


public class Main {
	static HashMap<Integer, Set<Integer>> sum;

	static boolean tryallother(HashSet<Integer> test, int ttt, int[] s) {
		for(int i=0; i<s.length; i++) {
			int val = ttt;
			if(test.contains(s[i])==false) {
				test.add(s[i]);
				val += s[i];
				if(sum.containsKey(val)) {
					if(! test.equals(sum.get(val))) {
						//System.out.println("Duplicate for sum : " + String.valueOf(val));
						return true;
					}
				}
				else {
					sum.put(val, new HashSet<Integer>(test));
					if(tryallother(test, val, s))
						return true;
				}
				
				val -= s[i];
				test.remove(s[i]);
			}
		}
		return false;
	}
	
	static void printSet(Set<Integer> t) {
		if(t!=null) {
		for(Iterator<Integer> i = t.iterator(); i.hasNext();) {
			int a = (int) i.next();
			System.out.print(a);
			if(i.hasNext())
				System.out.print(" ");
		}
		System.out.println();
		}
	}
	
	static int calc(Set<Integer> t) {
		int r = 0;
		if(t!=null) {
		for(Iterator<Integer> i = t.iterator(); i.hasNext();) {
			int a = (int) i.next();
			r +=a ;
		}
		}
		return r;
	}
	
	public static void main(String [] args) {
		Scanner in = new Scanner(System.in);
		int T = in.nextInt();
		Pb: for(int x=0; x<T; x++) {
			int N = in.nextInt();
			int[] s = new int[N];
			
			sum = new HashMap<Integer, Set<Integer>>();
			for(int i=0; i<N; i++) {
				s[i] = in.nextInt();
				HashSet<Integer> temp = new HashSet<Integer>();
				temp.add(s[i]);
				sum.put(s[i], temp);
				//printSet(temp);
			}
			
			System.out.println("Case #" + String.valueOf(x+1) + ":");
			
			HashSet<Integer> test;
			for(int i=0; i<N; i++) {
				test = new HashSet<Integer>();
				test.add(s[i]);
				int val = s[i];
				if(tryallother(test, val, s)) {
						int w = calc(test);
						//System.out.println(w);
						printSet(test);
						printSet(sum.get(w));
						continue Pb;
				}
			}
			System.out.println("Impossible");
		}
	}
}