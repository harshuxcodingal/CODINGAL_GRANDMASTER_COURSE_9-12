import java.util.Scanner;

// Application Class
class Application {

    String name;
    String email;

    Application(String name, String email) {
        this.name = name;
        this.email = email;
    }

    void display() {
        System.out.println("\n--- Application Details ---");
        System.out.println("Name  : " + name);
        System.out.println("Email : " + email);
    }
}

// Intern Hiring Class
class Intern {

    String name;
    int age;
    double cgpa;

    Intern(String name, int age, double cgpa) {
        this.name = name;
        this.age = age;
        this.cgpa = cgpa;
    }

    void checkEligibility() {

        System.out.println("\n--- Intern Hiring Result ---");
        System.out.println("Name : " + name);

        if(age >= 18 && cgpa >= 7.0) {
            System.out.println("Status : Selected");
        }
        else {
            System.out.println("Status : Not Selected");
        }
    }
}

public class Main {

    public static void applicationDemo(Scanner sc) {

        sc.nextLine();

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Email: ");
        String email = sc.nextLine();

        Application app = new Application(name, email);

        app.display();
    }

    public static void internHiringDemo(Scanner sc) {

        sc.nextLine();

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Age: ");
        int age = sc.nextInt();

        System.out.print("Enter CGPA: ");
        double cgpa = sc.nextDouble();

        Intern intern = new Intern(name, age, cgpa);

        intern.checkEligibility();
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(true) {

            System.out.println("\n===== JAVA PROJECTS =====");
            System.out.println("1. Application");
            System.out.println("2. Intern Hiring");
            System.out.println("3. Exit");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();

            switch(choice) {

                case 1:
                    applicationDemo(sc);
                    break;

                case 2:
                    internHiringDemo(sc);
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