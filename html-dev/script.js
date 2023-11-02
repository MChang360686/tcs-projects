
function changeButtonColor() {
    document.getElementById('enterbutton').style.color = "blue";
}

document.getElementById("enterbutton").addEventListener("click", changeButtonColor);

document.getElementById("showpicture").addEventListener("click", function() {
    var image = document.getElementById("image");
    image.style.visilbility = "hidden";
})