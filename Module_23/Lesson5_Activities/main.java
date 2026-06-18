import java.util.Scanner;

// Student Class
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

// Animal Class
class Animal {

    void sound() {
        System.out.println("Animals make sounds.");
    }
}

// Mammal Class (Inheritance)
class Mammal extends Animal {

    void sound() {
        System.out.println("Mammals give birth to young ones.");
    }
}

// Age Class
class Age {

    int birthYear;

    Age(int birthYear) {
        this.birthYear = birthYear;
    }

    void calculateAge() {
        int currentYear = 2025;
        int age = currentYear - birthYear;

        System.out.println("Age = " + age);
    }
}

public class Main {

    public static void studentDemo(Scanner sc) {

        sc.nextLine();

        System.out.print("Enter Student Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Roll Number: ");
        int roll = sc.nextInt();

        Student s = new Student(name, roll);
        s.display();
    }

    public static void animalDemo() {

        Animal a = new Animal();
        a.sound();
    }

    public static void mammalDemo() {

        Mammal m = new Mammal();
        m.sound();
    }

    public static void ageDemo(Scanner sc) {

        System.out.print("Enter Birth Year: ");
        int year = sc.nextInt();

        Age a = new Age(year);
        a.calculateAge();
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while (true) {

            System.out.println("\n===== JAVA PROJECTS =====");
            System.out.println("1. Students");
            System.out.println("2. Animals");
            System.out.println("3. Mammals");
            System.out.println("4. Age");
            System.out.println("5. Exit");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();

            switch (choice) {

                case 1:
                    studentDemo(sc);
                    break;

                case 2:
                    animalDemo();
                    break;

                case 3:
                    mammalDemo();
                    break;

                case 4:
                    ageDemo(sc);
                    break;

                case 5:
                    System.out.println("Thank You!");
                    sc.close();
                    System.exit(0);

                default:
                    System.out.println("Invalid Choice!");
            }
        }
    }
}