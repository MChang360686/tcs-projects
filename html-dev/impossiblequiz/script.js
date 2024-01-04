
document.getElementById("helpbutton").addEventListener('click', function () {
    var h = document.getElementById("help");
    if (h.style.display === 'none') {
        h.style.display = 'block';
    } else {
        h.style.display = 'none';
    }
});

document.getElementById("reset").addEventListener('click', function () {
    var game = document.getElementById("gameover");
    var q1 = document.getElementById("q1");
    if (game.style.display === 'none') {
        game.style.display = 'block';
    } else {
        game.style.display = 'none';
        q1.style.display = 'block';
    }
    
});

document.getElementById("q1b1").addEventListener('click', function () {
    var q1 = document.getElementById("")
    var g = document.getElementById("gameover");
    g.style.display = 'block'
});

document.getElementById("q1b2").addEventListener('click', function () {
    let lives = reduceLives();
    let gameover = checkGameOver(lives);
    if (gameover == true) {
        console.log("Game Over");
    } else {
        document.getElementById("lives").innerHTML = toString(lives);
    }
});

document.getElementById("q1b3").addEventListener('click', function () {
    var q2 = document.getElementById('q2');
    q2.style.display = 'block'
    var q1 = document.getElementById('q1');
    q1.style.display = 'none';
});

document.getElementById("q1b4").addEventListener('click', function () {
    let lives = reduceLives();
    let gameover = checkGameOver(lives);
    if (gameover == true) {
        console.log("Game Over");
    } else {
        document.getElementById("lives").innerHTML = toString(lives);
    }
});