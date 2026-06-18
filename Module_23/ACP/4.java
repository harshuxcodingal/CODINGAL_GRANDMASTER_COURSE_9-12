import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter marks of Subject 1: ");
        int s1 = sc.nextInt();

        System.out.print("Enter marks of Subject 2: ");
        int s2 = sc.nextInt();

        System.out.print("Enter marks of Subject 3: ");
        int s3 = sc.nextInt();

        System.out.print("Enter marks of Subject 4: ");
        int s4 = sc.nextInt();

        System.out.print("Enter marks of Subject 5: ");
        int s5 = sc.nextInt();

        int total = s1 + s2 + s3 + s4 + s5;
        double percentage = total / 5.0;

        String grade;

        if (percentage >= 90) {
            grade = "A";
        } else if (percentage >= 80) {
            grade = "B";
        } else if (percentage >= 70) {
            grade = "C";
        } else if (percentage >= 60) {
            grade = "D";
        } else {
            grade = "F";
        }

        System.out.println("\n----- REPORT CARD -----");
        System.out.println("Total Marks : " + total);
        System.out.println("Percentage  : " + percentage + "%");
        System.out.println("Grade       : " + grade);

        sc.close();
    }
}