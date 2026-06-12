

// let and const keywords
let studentName = "Harshal";
const passingMarks = 40;

// Different Data Types
let age = 20;                // Number
let isStudent = true;        // Boolean
let city = "Pune";           // String
let marks = null;            // Null
let subject;                 // Undefined

console.log("=== Data Types ===");
console.log("Name:", studentName, "-", typeof studentName);
console.log("Age:", age, "-", typeof age);
console.log("Is Student:", isStudent, "-", typeof isStudent);
console.log("City:", city, "-", typeof city);
console.log("Marks:", marks, "-", typeof marks);
console.log("Subject:", subject, "-", typeof subject);

// Conditional Statements
let score = 75;

console.log("\n=== Conditional Statements ===");

if (score >= 90) {
    console.log("Grade A");
} else if (score >= 75) {
    console.log("Grade B");
} else if (score >= passingMarks) {
    console.log("Grade C");
} else {
    console.log("Fail");
}

// Generate Random Numbers using While Loop
console.log("\n=== Random Numbers using While Loop ===");

let count = 1;

while (count <= 5) {
    let randomNumber = Math.floor(Math.random() * 100) + 1;
    console.log("Random Number", count + ":", randomNumber);
    count++;
}