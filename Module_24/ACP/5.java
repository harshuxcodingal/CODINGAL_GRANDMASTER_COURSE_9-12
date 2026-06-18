import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.println("\n===== NAME CATCHER =====");
        System.out.println("Name: " + name);
        System.out.println("Number of Characters: " + name.length());

        sc.close();
    }
}