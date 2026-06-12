// ===============================
// Sort and Reverse Strings
// ===============================

let fruits = ["Mango", "Apple", "Banana", "Orange"];

console.log("Original Strings:", fruits);

fruits.sort();
console.log("Sorted Strings:", fruits);

fruits.reverse();
console.log("Reversed Strings:", fruits);

// ===============================
// Sort and Reverse Numbers
// ===============================

let numbers = [45, 10, 78, 23, 5];

console.log("\nOriginal Numbers:", numbers);

numbers.sort((a, b) => a - b); // Ascending
console.log("Sorted Numbers:", numbers);

numbers.reverse();
console.log("Reversed Numbers:", numbers);

// ===============================
// Map an Array
// ===============================

let marks = [10, 20, 30, 40, 50];

let doubledMarks = marks.map(function(num) {
    return num * 2;
});

console.log("\nOriginal Marks:", marks);
console.log("Doubled Marks:", doubledMarks);

// ===============================
// Evaluate Variables
// ===============================

let x = 10;
let y = 20;
let z = x + y;

console.log("\nVariable Values:");
console.log("x =", x);
console.log("y =", y);
console.log("z = x + y =", z);

// Using eval() to evaluate expression
let expression = "x * y + z";

console.log("Expression:", expression);
console.log("Evaluated Result:", eval(expression));