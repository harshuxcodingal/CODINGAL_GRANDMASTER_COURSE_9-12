

let numString = "100";

console.log("Original Value:", numString);
console.log("Original Type:", typeof numString);

// String to Number
let number = Number(numString);

console.log("Converted Value:", number);
console.log("Converted Type:", typeof number);

// ===================================
// Search and Replace String
// ===================================

let sentence = "I love JavaScript. JavaScript is easy.";

console.log("\nOriginal String:");
console.log(sentence);

// Search
console.log("Position of JavaScript:", sentence.indexOf("JavaScript"));

// Replace
let newSentence = sentence.replace(/JavaScript/g, "JS");

console.log("After Replace:");
console.log(newSentence);

// ===================================
// Arrow Function
// ===================================

const square = (n) => n * n;

console.log("\nSquare of 5:", square(5));

// ===================================
// Error Handling in JavaScript
// ===================================

try {
    let age = -5;

    if (age < 0) {
        throw new Error("Age cannot be negative");
    }

    console.log("Age:", age);

} catch (error) {
    console.log("\nError Caught:");
    console.log(error.message);

} finally {
    console.log("Program execution completed.");
}