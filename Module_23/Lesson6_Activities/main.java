import java.util.Scanner;

// Method Overloading
class Calculator {

    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
}

// Parent Class
class Animal {

    void sound() {
        System.out.println("Animal makes a sound");
    }
}

// Method Overriding
class Dog extends Animal {

    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}

// Super Keyword
class Person {

    String name = "Harshal";
}

class Student extends Person {

    String name = "Rahul";

    void display() {
        System.out.println("Child Name : " + name);
        System.out.println("Parent Name: " + super.name);
    }
}

// Access Specifiers
class AccessDemo {

    public String publicVar = "Public";
    private String privateVar = "Private";
    protected String protectedVar = "Protected";
    String defaultVar = "Default";

    void display() {
        System.out.println("Public    : " + publicVar);
        System.out.println("Private   : " + privateVar);
        System.out.println("Protected : " + protectedVar);
        System.out.println("Default   : " + defaultVar);
    }
}

public class Main {

    public static void overloadDemo() {

        Calculator c = new Calculator();

        System.out.println("Addition of 2 numbers: "
                + c.add(10, 20));

        System.out.println("Addition of 3 numbers: "
                + c.add(10, 20, 30));
    }

    public static void overrideDemo() {

        Dog d = new Dog();
        d.sound();
    }

    public static void superDemo() {

        Student s = new Student();
        s.display();
    }

    public static void accessDemo() {

        AccessDemo a = new AccessDemo();
        a.display();
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(true) {

            System.out.println("\n===== OOP CONCEPTS =====");
            System.out.println("1. Overload");
            System.out.println("2. Override");
            System.out.println("3. Super");
            System.out.println("4. Access");
            System.out.println("5. Exit");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();

            switch(choice) {

                case 1:
                    overloadDemo();
                    break;

                case 2:
                    overrideDemo();
                    break;

                case 3:
                    superDemo();
                    break;

                case 4:
                    accessDemo();
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