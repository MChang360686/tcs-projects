document.getElementById('button1').addEventListener('click', function() {
    let a = document.getElementById('a').innerHTML;
    let b = document.getElementById('b').innerHTML;
    let c = document.getElementById('c').innerHTML;

    if (a**2 + b**2 == c**2) {
        document.getElementById('result').innerHTML = "This is a right triangle";
    }

});