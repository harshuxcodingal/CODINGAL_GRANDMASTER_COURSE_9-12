import java.util.Scanner;

public class Main {

    // Ten10
    public static void ten10() {

        System.out.println("\nNumbers from 1 to 10:");

        for(int i = 1; i <= 10; i++) {
            System.out.println(i);
        }
    }

    // Hello User
    public static void helloUser(Scanner sc) {

        sc.nextLine(); // clear buffer

        System.out.print("\nEnter your name: ");
        String name = sc.nextLine();

        System.out.println("Hello, " + name + "!");
        System.out.println("Welcome to Java Programming.");
    }

    // Grading System
    public static void gradingSystem(Scanner sc) {

        System.out.print("\nEnter marks: ");
        int marks = sc.nextInt();

        if(marks >= 90) {
            System.out.println("Grade A");
        }
        else if(marks >= 80) {
            System.out.println("Grade B");
        }
        else if(marks >= 70) {
            System.out.println("Grade C");
        }
        else if(marks >= 60) {
            System.out.println("Grade D");
        }
        else {
            System.out.println("Grade F");
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(true) {

            System.out.println("\n===== JAVA MINI PROJECTS =====");
            System.out.println("1. Ten10");
            System.out.println("2. Hello User");
            System.out.println("3. Grading System");
            System.out.println("4. Exit");

            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();

            switch(choice) {

                case 1:
                    ten10();
                    break;

                case 2:
                    helloUser(sc);
                    break;

                case 3:
                    gradingSystem(sc);
                    break;

                case 4:
                    System.out.println("Thank You!");
                    sc.close();
                    System.exit(0);

                default:
                    System.out.println("Invalid Choice!");
            }
        }
    }
}