import java.util.Scanner;

class Employee {

    String name;
    int id;
    double salary;

    Employee(String name, int id, double salary) {
        this.name = name;
        this.id = id;
        this.salary = salary;
    }

    void display() {
        System.out.println("\nEmployee Details");
        System.out.println("Name   : " + name);
        System.out.println("ID     : " + id);
        System.out.println("Salary : " + salary);
    }
}

class Counter {

    static int count = 0;

    Counter() {
        count++;
    }

    static void displayCount() {
        System.out.println("\nObjects Created: " + count);
    }
}

public class Main {

    // Employee
    public static void employeeDemo(Scanner sc) {

        sc.nextLine();

        System.out.print("Enter Employee Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Employee ID: ");
        int id = sc.nextInt();

        System.out.print("Enter Salary: ");
        double salary = sc.nextDouble();

        Employee emp = new Employee(name, id, salary);

        emp.display();
    }

    // Static Counter
    public static void staticCounterDemo() {

        new Counter();
        new Counter();
        new Counter();

        Counter.displayCount();
    }

    // Shabd (Word Counter)
    public static void shabdDemo(Scanner sc) {

        sc.nextLine();

        System.out.print("Enter a sentence: ");
        String sentence = sc.nextLine();

        String[] words = sentence.trim().split("\\s+");

        System.out.println("Number of Words: " + words.length);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(true) {

            System.out.println("\n===== JAVA PROJECTS =====");
            System.out.println("1. Employee");
            System.out.println("2. Static Counter");
            System.out.println("3. Shabd");
            System.out.println("4. Exit");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();

            switch(choice) {

                case 1:
                    employeeDemo(sc);
                    break;

                case 2:
                    staticCounterDemo();
                    break;

                case 3:
                    shabdDemo(sc);
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