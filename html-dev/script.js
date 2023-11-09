
function changeButtonColor() {
    document.getElementById('enterbutton').style.color = "blue";
}

document.getElementById("enterbutton").addEventListener("click", switchCase(true));


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