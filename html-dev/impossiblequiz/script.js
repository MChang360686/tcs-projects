function reduceLives() {
    let lives = Number(document.getElementById("lives").innerHTML);
    return lives--;
}

function checkGameOver(num) {
    if (num == 0) {
        return true;
    } else {
        return false;
    }
}

document.getElementById("helpbutton").addEventListener('click', function () {
    var h = document.getElementById("help");
    if (h.style.display === 'none') {
        h.style.display = 'block';
    } else {
        h.style.display = 'none';
    }
});

document.getElementById("q1b1").addEventListener('click', function () {
    let lives = reduceLives();
    let gameover = checkGameOver(lives);
    if (gameover == true) {
        console.log("Game Over");
    } else {
        document.getElementById("lives").innerHTML = toString(lives);
    }
})

document.getElementById("q1b3").addEventListener('click', function () {
    var q2 = document.getElementById('q2');
    q2.style.display = 'block'
    var q1 = document.getElementById('q1');
    q1.style.display = 'none';
});