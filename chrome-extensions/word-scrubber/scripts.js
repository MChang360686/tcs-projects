
document.getElementById("scrubButton").addEventListener("click", function() {
    var word = document.getElementById('wordBox').innerHTML.split(' ');
    console.log(word);
    for (let i = 0; i < word.length(); i++) {
        console.log(word[i]);
    }
});