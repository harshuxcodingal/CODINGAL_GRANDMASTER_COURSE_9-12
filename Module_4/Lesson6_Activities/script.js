// Variable
let count = 0;

// DOM Manipulation
function increaseCount() {
    count++;

    document.getElementById("count").innerHTML = count;
}

// Change Heading
function changeTitle() {
    document.getElementById("title").innerHTML =
        "JavaScript DOM Example";
}