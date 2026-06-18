import java.util.Scanner;

// Get Set Class
class Student {

    private String name;
    private int age;

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}

// Area Class
class Area {

    double calculateArea(double side) {
        return side * side;
    }

    double calculateArea(double length, double breadth) {
        return length * breadth;
    }

    double calculateTriangleArea(double base, double height) {
        return 0.5 * base * height;
    }
}

public class Main {

    public static void getSetDemo(Scanner sc) {

        sc.nextLine();

        Student s = new Student();

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Age: ");
        int age = sc.nextInt();

        s.setName(name);
        s.setAge(age);

        System.out.println("\nStudent Details");
        System.out.println("Name: " + s.getName());
        System.out.println("Age : " + s.getAge());
    }

    public static void areaDemo(Scanner sc) {

        Area a = new Area();

        System.out.println("\n1. Square");
        System.out.println("2. Rectangle");
        System.out.println("3. Triangle");

        System.out.print("Enter Choice: ");
        int choice = sc.nextInt();

        switch(choice) {

            case 1:
                System.out.print("Enter Side: ");
                double side = sc.nextDouble();

                System.out.println("Area of Square = "
                        + a.calculateArea(side));
                break;

            case 2:
                System.out.print("Enter Length: ");
                double length = sc.nextDouble();

                System.out.print("Enter Breadth: ");
                double breadth = sc.nextDouble();

                System.out.println("Area of Rectangle = "
                        + a.calculateArea(length, breadth));
                break;

            case 3:
                System.out.print("Enter Base: ");
                double base = sc.nextDouble();

                System.out.print("Enter Height: ");
                double height = sc.nextDouble();

                System.out.println("Area of Triangle = "
                        + a.calculateTriangleArea(base, height));
                break;

            default:
                System.out.println("Invalid Choice");
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(true) {

            System.out.println("\n===== JAVA PROJECTS =====");
            System.out.println("1. Get Set");
            System.out.println("2. Area");
            System.out.println("3. Exit");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();

            switch(choice) {

                case 1:
                    getSetDemo(sc);
                    break;

                case 2:
                    areaDemo(sc);
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