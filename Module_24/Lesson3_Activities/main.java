import java.util.Scanner;

// Interface
interface MyInterface {

    void start();
    void stop();
}

// Vehicle Class implementing Interface
class Vehicle implements MyInterface {

    public void start() {
        System.out.println("Vehicle Started");
    }

    public void stop() {
        System.out.println("Vehicle Stopped");
    }

    void display() {
        System.out.println("This is a Vehicle");
    }
}

// Bike Class
class Bike implements MyInterface {

    public void start() {
        System.out.println("Bike Started");
    }

    public void stop() {
        System.out.println("Bike Stopped");
    }
}

// Car Class
class Car implements MyInterface {

    public void start() {
        System.out.println("Car Started");
    }

    public void stop() {
        System.out.println("Car Stopped");
    }
}

public class Main {

    public static void interfaceDemo() {

        Vehicle v = new Vehicle();

        System.out.println("\n--- My Interface Demo ---");
        v.start();
        v.stop();
    }

    public static void vehicleDemo() {

        Bike b = new Bike();
        Car c = new Car();

        System.out.println("\n--- Bike ---");
        b.start();
        b.stop();

        System.out.println("\n--- Car ---");
        c.start();
        c.stop();
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(true) {

            System.out.println("\n===== JAVA PROJECTS =====");
            System.out.println("1. My Interface");
            System.out.println("2. Vehicle");
            System.out.println("3. Exit");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();

            switch(choice) {

                case 1:
                    interfaceDemo();
                    break;

                case 2:
                    vehicleDemo();
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