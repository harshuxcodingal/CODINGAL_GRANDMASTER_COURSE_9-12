import java.util.Scanner;
import java.util.Random;

public class Main {

    public static void calculator(Scanner sc) {

        System.out.print("Enter first number: ");
        double num1 = sc.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = sc.nextDouble();

        System.out.println("\nResults:");
        System.out.println("Addition = " + (num1 + num2));
        System.out.println("Subtraction = " + (num1 - num2));
        System.out.println("Multiplication = " + (num1 * num2));

        if(num2 != 0)
            System.out.println("Division = " + (num1 / num2));
        else
            System.out.println("Division by zero is not allowed.");
    }

    public static void mindRiddler(Scanner sc) {

        Random random = new Random();

        int secretNumber = random.nextInt(10) + 1;

        System.out.println("\nGuess a number between 1 and 10:");
        int guess = sc.nextInt();

        if(guess == secretNumber) {
            System.out.println("Congratulations! Correct Answer.");
        }
        else {
            System.out.println("Wrong Guess!");
            System.out.println("Correct Number was: " + secretNumber);
        }
    }

    public static void maggieCalculator(Scanner sc) {

        int pricePerPacket = 15;

        System.out.print("\nEnter number of Maggie packets: ");
        int packets = sc.nextInt();

        int totalCost = packets * pricePerPacket;

        System.out.println("Total Cost = Rs. " + totalCost);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(true) {

            System.out.println("\n===== FUN EXPLORING =====");
            System.out.println("1. Calcii");
            System.out.println("2. Mind Riddler");
            System.out.println("3. Maggie");
            System.out.println("4. Exit");

            System.out.print("Choose an option: ");
            int choice = sc.nextInt();

            switch(choice) {

                case 1:
                    calculator(sc);
                    break;

                case 2:
                    mindRiddler(sc);
                    break;

                case 3:
                    maggieCalculator(sc);
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