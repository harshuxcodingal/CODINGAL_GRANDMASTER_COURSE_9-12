
// Global Variable
let school = "Coding School";

// Function with Parameters
function studentInfo(name, age) {
    console.log("Name:", name);
    console.log("Age:", age);
}

// Calling Function
studentInfo("Harshal", 25);

console.log("----------------");

// Function with Optional Parameter
function greet(name, message = "Welcome to JavaScript") {
    console.log("Hello " + name);
    console.log(message);
}

// Calling with one argument
greet("Sai");

console.log("----------------");

// Calling with both arguments
greet("Harshal", "Have a great day!");

console.log("----------------");

// Scope of Variables
function showScope() {

    // Local Variable
    let city = "Nashik";

    console.log("School:", school); // Global Variable
    console.log("City:", city);      // Local Variable
}

showScope();

console.log("----------------");

// Function Expression
const multiply = function(a, b) {
    return a * b;
};

let result = multiply(10, 5);

console.log("Multiplication =", result);

console.log("----------------");

// Another Function
function add(num1, num2) {
    return num1 + num2;
}

console.log("Addition =", add(20, 30));