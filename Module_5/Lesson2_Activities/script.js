// Parent Class
class Person {
    constructor(name, age) {
        // 'this' refers to the current object
        this.name = name;
        this.age = age;
    }

    display() {
        console.log("Name:", this.name);
        console.log("Age:", this.age);
    }

    // Static method belongs to the class, not objects
    static companyName() {
        console.log("Company: ABC Technologies");
    }
}

// Child Class (Inheritance)
class Student extends Person {
    constructor(name, age, course) {
        super(name, age); // Calls Parent constructor
        this.course = course;
    }

    studentInfo() {
        console.log("Course:", this.course);
    }
}

// Creating Object
let s1 = new Student("Harshal", 22, "JavaScript");

// Calling methods
s1.display();
s1.studentInfo();

// Calling Static Method
Person.companyName();