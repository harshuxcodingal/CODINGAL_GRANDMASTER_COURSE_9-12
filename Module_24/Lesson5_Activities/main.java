import java.util.Scanner;

public class Main {

    // Magic 1 - Reverse Number
    public static void magic1(Scanner sc) {

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        int reverse = 0;
        int temp = num;

        while(temp != 0) {
            int digit = temp % 10;
            reverse = reverse * 10 + digit;
            temp = temp / 10;
        }

        System.out.println("Original Number : " + num);
        System.out.println("Reversed Number : " + reverse);
    }

    // Magic 2 - Palindrome Check
    public static void magic2(Scanner sc) {

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        int reverse = 0;
        int temp = num;

        while(temp != 0) {
            int digit = temp % 10;
            reverse = reverse * 10 + digit;
            temp = temp / 10;
        }

        if(num == reverse) {
            System.out.println(num + " is a Palindrome Number");
        } else {
            System.out.println(num + " is Not a Palindrome Number");
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(true) {

            System.out.println("\n===== MAGIC PROGRAMS =====");
            System.out.println("1. Magic 1");
            System.out.println("2. Magic 2");
            System.out.println("3. Exit");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();

            switch(choice) {

                case 1:
                    magic1(sc);
                    break;

                case 2:
                    magic2(sc);
                    break;

                case 3:
                    System.out.println("Thank You!");
                    sc.close();
                    System.exit(0);

                default:
                    System.out.println("Invalid Choice!");
            }
        }
    }
}