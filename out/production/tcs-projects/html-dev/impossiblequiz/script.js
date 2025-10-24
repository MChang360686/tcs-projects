
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
    var q2 = document.getElementById("q2");
    var q3 = document.getElementById("q3");
    var win = document.getElementById("win");
    if (game.style.display === 'none') {
        game.style.display = 'block';
        q1.style.display = 'none';
        q2.style.display = 'none';
        q3.style.display = 'none';
    } else {
        game.style.display = 'none';
        win.style.display = 'none';
        q1.style.display = 'block';
    }
    
});

document.getElementById("q1b1").addEventListener('click', function () {
    var q1 = document.getElementById("q1")
    var g = document.getElementById("gameover");
    q1.style.display = 'none'
    g.style.display = 'block'
});

document.getElementById("q1b2").addEventListener('click', function () {
    var q1 = document.getElementById("q1")
    var g = document.getElementById("gameover");
    q1.style.display = 'none'
    g.style.display = 'block'
});

document.getElementById("q1b3").addEventListener('click', function () {
    var q2 = document.getElementById('q2');
    q2.style.display = 'block'
    var q1 = document.getElementById('q1');
    q1.style.display = 'none';
});

document.getElementById("q1b4").addEventListener('click', function () {
    var q1 = document.getElementById("q1")
    var g = document.getElementById("gameover");
    q1.style.display = 'none'
    g.style.display = 'block'
});

document.getElementById("q2b1").addEventListener('click', function () {
    var q3 = document.getElementById('q3');
    q3.style.display = 'block'
    var q2 = document.getElementById('q2');
    q2.style.display = 'none';
});

document.getElementById("q2b2").addEventListener('click', function () {
    var q2 = document.getElementById("q2")
    var g = document.getElementById("gameover");
    q2.style.display = 'none'
    g.style.display = 'block'
});

document.getElementById("q2b3").addEventListener('click', function () {
    var q2 = document.getElementById("q2")
    var g = document.getElementById("gameover");
    q2.style.display = 'none'
    g.style.display = 'block'
});

document.getElementById("q2b4").addEventListener('click', function () {
    var q2 = document.getElementById("q2")
    var g = document.getElementById("gameover");
    q2.style.display = 'none'
    g.style.display = 'block'
});

document.getElementById("q3b1").addEventListener('click', function () {
    var w = document.getElementById('win');
    w.style.display = 'block'
    var q3 = document.getElementById('q3');
    q3.style.display = 'none';
});

document.getElementById("q3b2").addEventListener('click', function () {
    var q3 = document.getElementById("q3")
    var g = document.getElementById("gameover");
    q3.style.display = 'none'
    g.style.display = 'block'
});

document.getElementById("q3b3").addEventListener('click', function () {
    var q3 = document.getElementById("q3")
    var g = document.getElementById("gameover");
    q3.style.display = 'none'
    g.style.display = 'block'
});

document.getElementById("q3b4").addEventListener('click', function () {
    var q3 = document.getElementById("q3")
    var g = document.getElementById("gameover");
    q3.style.display = 'none'
    g.style.display = 'block'
});