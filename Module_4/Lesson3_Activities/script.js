
// String Methods
let name = "codingal";

console.log("Original Name:", name);
console.log("Uppercase:", name.toUpperCase());
console.log("Length:", name.length);

console.log("----------------");

// Array Methods
let fruits = ["Apple", "Banana", "Mango"];

fruits.push("Orange"); // Add item

console.log("Fruits:", fruits);

console.log("----------------");

// Test Methods
let marks = [80, 90, 70, 95, 85];

// every() method
let allPassed = marks.every(function(mark){
    return mark >= 35;
});

console.log("All Students Passed:", allPassed);

// some() method
let topper = marks.some(function(mark){
    return mark > 90;
});

console.log("Any Topper Present:", topper);

console.log("----------------");

// Loops in JS

console.log("For Loop");

for(let i = 1; i <= 5; i++){
    console.log(i);
}

console.log("----------------");

console.log("While Loop");

let count = 1;

while(count <= 5){
    console.log(count);
    count++;
}

console.log("----------------");

// Switch Statement

let day = 3;

switch(day){

    case 1:
        console.log("Monday");
        break;

    case 2:
        console.log("Tuesday");
        break;

    case 3:
        console.log("Wednesday");
        break;

    case 4:
        console.log("Thursday");
        break;

    case 5:
        console.log("Friday");
        break;

    default:
        console.log("Invalid Day");
}