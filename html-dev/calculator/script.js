
var num1 = 0;
var num2 = 0;
var operator = '';

function add() {
    let equation = document.getElementById("codeInput").value;
    document.getElementById("codeInput").value = equation + "+";
    operator = '+';
}

function sub() {

}

function mult() {

}

function div() {

}

function clear() {
    if (num1 == 0){
        num1 = parseInt(document.getElementById("codeInput").value);
        document.getElementById("codeInput").value = '';
    } else if (num2 == 0) {
        num2 = parseInt(document.getElementById("codeInput").value);
        document.getElementById("codeInput").value = '';
    }
    
}

function solve() {
    document.getElementById("result").innerHTML = Number(num1) + Number(num2);
    num1 = 0;
    num2 = 0;
    operator = '';
}

document.getElementById("add").addEventListener("click", function() {
    add();
    clear();
});

document.getElementById("eq").addEventListener("click", function() {
    clear();
    solve();
});

