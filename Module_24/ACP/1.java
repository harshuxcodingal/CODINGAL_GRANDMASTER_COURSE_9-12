import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("===== VOLUME CALCULATOR =====");
        System.out.println("1. Cube");
        System.out.println("2. Cylinder");
        System.out.println("3. Sphere");

        System.out.print("Enter Choice: ");
        int choice = sc.nextInt();

        switch(choice) {

            case 1:
                System.out.print("Enter Side: ");
                double side = sc.nextDouble();

                double cubeVolume = side * side * side;

                System.out.println("Volume of Cube = " + cubeVolume);
                break;

            case 2:
                System.out.print("Enter Radius: ");
                double radius = sc.nextDouble();

                System.out.print("Enter Height: ");
                double height = sc.nextDouble();

                double cylinderVolume = Math.PI * radius * radius * height;

                System.out.println("Volume of Cylinder = " + cylinderVolume);
                break;

            case 3:
                System.out.print("Enter Radius: ");
                double r = sc.nextDouble();

                double sphereVolume = (4.0 / 3.0) * Math.PI * r * r * r;

                System.out.println("Volume of Sphere = " + sphereVolume);
                break;

            default:
                System.out.println("Invalid Choice");
        }

        sc.close();
    }
}