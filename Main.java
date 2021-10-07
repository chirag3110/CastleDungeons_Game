import java.util.Scanner;
import java.util.ArrayList;
class Main {
  public static void main(String[] args) {
    Scanner scn=new Scanner(System.in);
    String s1="ell";
    String s2="ell";
    System.out.print(s1==s2);
    ArrayList<Integer> a = new ArrayList<>();
    a.add(5);
    a.add(6);
    a.add(1,4);
    for(int item: a)
    {
      System.out.println(item);
    }
  }
}