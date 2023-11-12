// Define functions for die rolls
function d2() {
    return Math.floor(Math.random() * 2) + 1;
}

function d4() {
    return Math.floor(Math.random() * 4) + 1;
}

function d8() {
    return Math.floor(Math.random() * 8) + 1;
}

function d10() {
    return Math.floor(Math.random() * 10) + 1;
}

function d20() {
    return Math.floor(Math.random() * 20) + 1;
}

function d100() {
    return Math.floor(Math.random() * 100);
}

// Define character object to store data
let character = {type: "", end: 0, str: 0, ag: 0, acc: 0, int: 0, per: 0, will: 0, app: 0, caste: "", skills: [], gear: [], equipment: [], readwrite: false, math: false, bounty: false, misc: ""}

// Clear character object
function clearCharacter() {

}

// Clear character sheets (div)
function clearCharSheets() {

}

// Select difficulty from dropdown
function getDifficulty() {
    var diff = document.getElementsByName("difficulty");
    
    for (i = 0; i < diff.length; i++) {
        if (diff[i].checked) {
           return diff[i].value;
        }
    }

    return "difficulty not selected";

}

// Roll for Character type
function rollCharType(diff, d100) {
    switch (diff) {
        case 1:
            break;
        case 2:
            break;
        case 3:
            break;
        default:
        
    }

}

function beginnerTypes(d100) {
    switch (d100) {
        case 33:
            break;
        case 34:
            break;
        case 35:
            break;
        case 36:
            break;
        case 37:
            break;
        case 38:
            break;
        case 39:
            break;
        case 40:
            break;
        case 41:
            break;
        case 42:
        case 43:
        case 44:
        case 45:
        case 46:
        case 47:
        case 48:
        case 49:
        case 50:
        case 51:
        case 52:
        case 53:
        case 54:
        case 55:
            break;
        case 56:
        case 57:
        case 58:
        case 59:
        case 60:
        case 61:
            break;
        case 62:
        case 63:
        case 64:
        case 65:
        case 66:
        case 67:
        case 68:
            break;
        case 69:
        case 70:
        case 71:
        case 72:
        case 73:
        case 74:
        case 75:
        case 76:
        case 77:
        case 78:
        case 79:
        case 80:
        case 81:
        case 82:
        case 83:
        case 84:
        case 85:
        case 86:
        case 87:
            break;
        case 88:
        case 89:
        case 90:
        case 91:
        case 92:
        case 93:
        case 94:
        case 95:
        case 96:
        case 97:
        case 98:
            break;
        case 99:
        case 0:
            break;
        default:
    }
}

function experiencedTypes(d100) {

}

function masterTypes(d100) {

}

// Roll for Character base stats
function rollStats(characterObj) {
    var strength = d100;
}


// Roll for Character caste
function rollCaste(){

}

// Add event listener for Generate button
document.getElementById("generateButton").addEventListener("click", function() {
    
});