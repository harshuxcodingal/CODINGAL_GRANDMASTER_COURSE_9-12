import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        try {

            System.out.print("Enter first number: ");
            int a = sc.nextInt();

            System.out.print("Enter second number: ");
            int b = sc.nextInt();

            int result = a / b;

            int[] arr = {10, 20, 30};

            System.out.println("Array Element: " + arr[5]);

            System.out.println("Result: " + result);

        }
        catch (ArithmeticException | ArrayIndexOutOfBoundsException e) {

            System.out.println("Exception Caught: " + e);
        }

        finally {

            System.out.println("Program Finished.");
            sc.close();
        }
    }
}