function sum() {
    let total = 0;

    for (let i = 0; i < arguments.length; i++) {
        total += arguments[i];
    }

    console.log("Sum =", total);
}

sum(10, 20, 30, 40);