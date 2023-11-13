// Define functions for die rolls
function d2() {
    return Math.floor(Math.random() * 2) + 1;
}

function d3() {
    return Math.floor(Math.random() * 3) + 1;
}

function d4() {
    return Math.floor(Math.random() * 4) + 1;
}

function d6() {
    return Math.floor(Math.random() * 6) + 1;
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
let character = {type: "", end: 0, str: 0, ag: 0, acc: 0, int: 0, per: 0, will: 0, app: 0, caste: "", skills: [], gear: [], equipment: [], readwrite: false, math: false, bounty: false, misc: ""};

// Clear character object
function clearCharacter() {
    let character = {type: "", end: 0, str: 0, ag: 0, acc: 0, int: 0, per: 0, will: 0, app: 0, caste: "", skills: [], gear: [], equipment: [], readwrite: false, math: false, bounty: false, misc: ""};
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
function rollCharType(diff, d100, characterObj) {
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

function beginnerTypes(d100, characterObj) {
    switch (d100) {
        case 33:
            characterObj["type"] = "clone comfort";
            break;
        case 34:
            characterObj["type"] = "clone labor";
            break;
        case 35:
            characterObj["type"] = "clone military";
            break;
        case 36:
            characterObj["type"] = "bioreplica pleasure";
            break;
        case 37:
            characterObj["type"] = "bioreplica industrial";
            break;
        case 38:
            characterObj["type"] = "bioreplica clerical";
            break;
        case 39:
            characterObj["type"] = "bioreplica infiltration";
            break;
        case 40:
            characterObj["type"] = "bioreplica battle";
            break;
        case 41:
            characterObj["type"] = "transhuman";
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
            characterObj["type"] = "cyborg";
            break;
        case 56:
        case 57:
        case 58:
        case 59:
        case 60:
        case 61:
            characterObj["type"] = "bestial human";
            break;
        case 62:
        case 63:
        case 64:
        case 65:
        case 66:
        case 67:
        case 68:
            characterObj["type"] = "ghost mutant";
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
            characterObj["type"] = "mild mutant";
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
            characterObj["type"] = "typical mutant";
            break;
        case 99:
        case 0:
            characterObj["type"] = "severe mutant";
            break;
        default:
            characterObj["type"] = "pure stock";
    }
}

function experiencedTypes(d100) {

}

function masterTypes(d100) {

}

// Roll for Character base stats
function rollStats(characterObj) {
    characterObj["end"] = d100();
    var strength = d100();
    var agility = d100();
}

// What you roll is not necessarily what you get
// stat wise for TME i.e. a roll of 1 gets you 
// a base stat of d10 (see pg. 10 in the rules)
function getStats(rollValue) {
    var value = 0;
    switch (rollValue) {
        case 1:
            value = d10();
            break;
        case 2:
            value = 11;
            break;
        case 3:
            value = 12;
            break;
        case 4:
            value = 13;
            break;
        case 5:
            value = 14;
            break;
        case 6:
        case 7:
            value = 15;
            break;
        case 8:
        case 9:
            value = 16;
            break;
        case 10:
        case 11:
            value = 17;
            break;
        case 12:
        case 13:
        case 14:
            value = 18;
            break;
        case 15:
        case 16:
        case 17:
            value = 19;
            break;
        case 18:
        case 19:
        case 20:
        case 21:
            value = 20;
            break;
        case 22:
        case 23:
        case 24:
        case 25:
            value = 21;
            break;
        case 26:
        case 27:
        case 28:
        case 29:
        case 30:
            value = 22;
            break;
        case 31:
        case 32:
        case 33:
        case 34:
        case 35:
            value = 23;
            break;
        case 36:
        case 37:
            value = 24;
            break;
        case 38:
        case 39:
            value = 25;
            break;
        case 40:
        case 41:
            value = 26;
            break;
        case 42:
        case 43:
            value = 27;
            break;
        case 44:
        case 45:
            value = 28;
            break;
        
    }
    return value;
}


// Roll for Character caste
function rollCaste(){

}

// Add event listener for Generate button
document.getElementById("generateButton").addEventListener("click", function() {
   rollStats(character); 
   console.log(character);
});