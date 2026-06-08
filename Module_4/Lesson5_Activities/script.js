
let student = {
    name: "Harshal",
    age: 25,
    course: "JavaScript"
};

console.log("Student Object:");
console.log(student);


console.log("\nMath Object Examples:");
console.log("PI =", Math.PI);
console.log("Square Root of 81 =", Math.sqrt(81));
console.log("2 Power 5 =", Math.pow(2, 5));
console.log("Random Number =", Math.random());

// ===============================
// ARRAY IN JS
// ===============================

let fruits = ["Apple", "Mango", "Banana"];

console.log("\nOriginal Array:");
console.log(fruits);

// ===============================
// ARRAY METHODS
// ===============================

// push() - Add element at end
fruits.push("Orange");

// pop() - Remove last element
fruits.pop();

// unshift() - Add element at beginning
fruits.unshift("Grapes");

// shift() - Remove first element
fruits.shift();

console.log("\nArray After Methods:");
console.log(fruits);

// ===============================
// CALL STACK
// ===============================

function first() {
    console.log("First Function Started");
    second();
    console.log("First Function Ended");
}

function second() {
    console.log("Second Function Started");
    third();
    console.log("Second Function Ended");
}

function third() {
    console.log("Third Function Executed");
}

console.log("\nCall Stack Example:");
first();