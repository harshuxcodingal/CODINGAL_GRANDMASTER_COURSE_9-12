import java.util.Scanner;

// Parent Class
class HillStation {

    void location() {
        System.out.println("Hill Station Location");
    }

    void famousFor() {
        System.out.println("Famous Attraction");
    }
}

// Child Class 1
class Manali extends HillStation {

    void location() {
        System.out.println("Manali is in Himachal Pradesh");
    }

    void famousFor() {
        System.out.println("Famous for Snow and Adventure Sports");
    }
}

// Child Class 2
class Mussoorie extends HillStation {

    void location() {
        System.out.println("Mussoorie is in Uttarakhand");
    }

    void famousFor() {
        System.out.println("Famous for Hills and Waterfalls");
    }
}

// Child Class 3
class Gulmarg extends HillStation {

    void location() {
        System.out.println("Gulmarg is in Jammu & Kashmir");
    }

    void famousFor() {
        System.out.println("Famous for Skiing");
    }
}

// Objects Demo
class Student {

    String name;
    int rollNo;

    Student(String name, int rollNo) {
        this.name = name;
        this.rollNo = rollNo;
    }

    void display() {
        System.out.println("\nStudent Details");
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollNo);
    }
}

public class Main {

    public static void objectsDemo() {

        Student s1 = new Student("Harshal", 101);
        Student s2 = new Student("Rahul", 102);

        s1.display();
        s2.display();
    }

    public static void hillStationDemo() {

        HillStation h1 = new Manali();
        HillStation h2 = new Mussoorie();
        HillStation h3 = new Gulmarg();

        System.out.println("\n--- Manali ---");
        h1.location();
        h1.famousFor();

        System.out.println("\n--- Mussoorie ---");
        h2.location();
        h2.famousFor();

        System.out.println("\n--- Gulmarg ---");
        h3.location();
        h3.famousFor();
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(true) {

            System.out.println("\n===== JAVA PROJECTS =====");
            System.out.println("1. Objects");
            System.out.println("2. Hill Station");
            System.out.println("3. Exit");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();

            switch(choice) {

                case 1:
                    objectsDemo();
                    break;

                case 2:
                    hillStationDemo();
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