
let student = {
    name: "Harshal",
    age: 22,
    course: "JavaScript"
};

// Convert Object to JSON
let jsonData = JSON.stringify(student);

console.log("JSON String:");
console.log(jsonData);

// Convert JSON back to Object
let objectData = JSON.parse(jsonData);

console.log("\nObject from JSON:");
console.log(objectData);

// ===================================
// Callback Function
// ===================================

function greet(name, callback) {
    console.log("\nHello " + name);
    callback();
}

function message() {
    console.log("Welcome to JavaScript!");
}

greet("Harshal", message);

// ===================================
// Promise (Asynchronous)
// ===================================

function checkResult(marks) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (marks >= 40) {
                resolve("Pass");
            } else {
                reject("Fail");
            }
        }, 2000); // 2 seconds delay
    });
}

// ===================================
// Async / Await
// ===================================

async function getResult() {
    try {
        console.log("\nChecking Result...");

        let result = await checkResult(75);

        console.log("Result:", result);

    } catch (error) {
        console.log("Error:", error);
    }
}

getResult();