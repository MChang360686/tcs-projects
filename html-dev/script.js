
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
document.getElementById("enterbutton").addEventListener("click", function () {switchStatement(inputValue)});


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