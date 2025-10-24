function d2() {
    return Math.floor(Math.random() * 2 + 1);
}

function d4() {
    return Math.floor(Math.random() * 4 + 1);
}

function d6() {
    return Math.floor(Math.random() * 6 + 1);
}

function d8() {
    return Math.floor(Math.random() * 8 + 1);
}

function d10() {
    return Math.floor(Math.random() * 10 + 1);
}

function d20() {
    return Math.floor(Math.random() * 20 + 1);
}


document.getElementById("button").addEventListener("click", function() {
    if(document.getElementById("2").checked){
        document.getElementById("results").innerHTML = d2().toString();
    } else if (document.getElementById('4').checked){
        document.getElementById("results"). innerHTML = d4().toString();
    } else if (document.getElementById('6').checked){
        document.getElementById("results"). innerHTML = d6().toString();
    } else if (document.getElementById('8').checked){
        document.getElementById("results"). innerHTML = d8().toString();
    } else if (document.getElementById('10').checked){
        document.getElementById("results"). innerHTML = d10().toString();
    } else if (document.getElementById('20').checked){
        document.getElementById("results"). innerHTML = d20().toString();
    }
});