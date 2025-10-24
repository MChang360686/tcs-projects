
function changeButtonColor() {
    document.getElementById('enterbutton').style.color = "blue";
}

function switchStatement(a) {
    switch (a) {
        case "1":
            console.log("1");
            break;
        case "2":
            console.log("2");
            break;
        case "3":
            console.log("3");
            break;
        default:
            console.log("IDK");
    }
}

var inputValue = document.getElementById("numberbar");
//document.getElementById("enterbutton").addEventListener("click", function () {switchStatement(inputValue)});


function ifElse(variable) {
    if (variable) {
        alert("True");
    } else {
        alert("False");
    }
}

function switchCase(variable) {
    switch (variable){
        case true:
            document.getElementById("text").innerHTML = "True";
            break;
        case false:
            document.getElementById("text").innerHTML = "False";
            break;
        default:
            document.getElementById("text").innerHTML = "Spaghetti";
    }
}

alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25};

function splitString() {
    var str = document.getElementById("codeInput").innerHTML;
    
    for (var i = 0; i<str.length; i++) {
        console.log(str.charAt(i));
    }
}

document.getElementById("enterbutton").addEventListener("click", function () {splitString()});