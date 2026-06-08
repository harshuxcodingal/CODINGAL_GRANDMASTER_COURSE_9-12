function add() {
    let n1 = Number(document.getElementById("num1").value);
    let n2 = Number(document.getElementById("num2").value);

    document.getElementById("result").innerHTML =
        "Result: " + (n1 + n2);
}

function subtract() {
    let n1 = Number(document.getElementById("num1").value);
    let n2 = Number(document.getElementById("num2").value);

    document.getElementById("result").innerHTML =
        "Result: " + (n1 - n2);
}

function multiply() {
    let n1 = Number(document.getElementById("num1").value);
    let n2 = Number(document.getElementById("num2").value);

    document.getElementById("result").innerHTML =
        "Result: " + (n1 * n2);
}

function divide() {
    let n1 = Number(document.getElementById("num1").value);
    let n2 = Number(document.getElementById("num2").value);

    document.getElementById("result").innerHTML =
        "Result: " + (n1 / n2);
}