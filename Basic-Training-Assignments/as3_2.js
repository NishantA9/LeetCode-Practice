if (true) {
    var x = 10;  // Function-scoped
    let y = 20;  // Block-scoped
}
console.log(x);  // 10 (accessible)
console.log(y);  // ReferenceError: y is not defined
