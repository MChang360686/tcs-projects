function add() {
    let var1 = document.getElementById("codeInput").value;
    let var2 = document.getElementById("codeInput2").value;
    return Number(var1) + Number(var2);
}

function sub() {
    let var1 = document.getElementById("codeInput").value;
    let var2 = document.getElementById("codeInput2").value;
    return Number(var1) - Number(var2);
}

function mult() {

}

function div() {

}

function percentage() {
    let var1 = document.getElementById("codeInput").value;
    let var2 = document.getElementById("codeInput2").value;
    return (Number(var1) / Number(var2)) * 100;
}

function fraction(){
    let var1 = document.getElementById("codeInput").value;
    let var2 = document.getElementById("codeInput2").value;
    return var1 + '/' + var2;
}

function clear() {
    document.getElementById("codeInput").value = '';
    document.getElementById("codeInput2").value = '';
}


document.getElementById("add").addEventListener("click", function() {
    var sum = add();
    console.log(sum);
    document.getElementById("result").innerHTML = sum;
    clear();
});

document.getElementById("sub").addEventListener("click", function() {
    var sum = sub();
    console.log(sum);
    document.getElementById("result").innerHTML = sum;
    clear();
});

document.getElementById("mult").addEventListener("click", function() {
    
});

document.getElementById("percent").addEventListener("click", function() {
    var sum = percentage();
    console.log(sum);
    document.getElementById("result").innerHTML = sum;
    clear();
});

document.getElementById("fraction").addEventListener("click", function() {
    var sum = fraction();
    console.log(sum);
    document.getElementById("result").innerHTML = sum;
    clear();
});

document.getElementById("div").addEventListener("click", function() {
    
});

