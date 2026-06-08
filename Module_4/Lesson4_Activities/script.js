

let student = {
    name: "Harshal",
    age: 25,
    course: "JavaScript"
};


console.log("Student Name:", student.name);     // Dot notation
console.log("Student Age:", student["age"]);    // Bracket notation

// Adding a new property
student.city = "Nashik";

console.log("Updated Object:", student);

// ===============================
// BUILT-IN MATH OBJECT
// ===============================

console.log("PI Value:", Math.PI);
console.log("Square Root of 64:", Math.sqrt(64));
console.log("Power 2^5:", Math.pow(2, 5));
console.log("Random Number:", Math.random());
console.log("Maximum Value:", Math.max(10, 20, 30));
console.log("Minimum Value:", Math.min(10, 20, 30));

// ===============================
// ARGUMENTS OBJECT
// ===============================

function addNumbers() {
    let sum = 0;

    for (let i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }

    console.log("Sum =", sum);
}

addNumbers(10, 20, 30, 40);

// ===============================
// DISPLAY FINAL OBJECT DETAILS
// ===============================

console.log("Student Details:");
for (let key in student) {
    console.log(key + " : " + student[key]);
}