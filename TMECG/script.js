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
            beginnerTypes(d100, characterObj);
            break;
        case 2:
            break;
        case 3:
            break;
        default:
            beginnerTypes(d100, characterObj);
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
    characterObj["end"] = getStats(d100());
    characterObj["str"] = getStats(d100());
    characterObj["ag"] = getStats(d100());
    characterObj["acc"] = getStats(d100());
    characterObj["int"] = getStats(d100());
    characterObj["per"] = getStats(d100());
    characterObj["will"] = getStats(d100());
    characterObj["app"] = getStats(d100());
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
        case 46:
        case 47:
            value = 29;
            break;
        case 48:
        case 49:
            value = 30;
            break;
        case 50:
        case 51:
            value = 31;
            break;
        case 52:
        case 53:
            value = 32;
            break;
        case 54:
        case 55:
            value = 33;
            break;
        case 56:
        case 57:
            value = 34;
            break;
        case 58:
        case 59:
            value = 35;
            break;
        case 60:
        case 61:
            value = 36;
            break;
        case 62:
        case 63:
            value = 37;
            break;
        case 64:
        case 65:
            value = 38;
            break;
        case 66:
        case 67:
            value = 39;
            break;
        case 68:
        case 69:
            value = 40;
            break;
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
        case 88:
        case 89:
        case 90:
            value = 40 + d20();
            break;
        case 91:
        case 92:
        case 93:
        case 94:
        case 95:
        case 96:
            value = 60 + d20();
            break;
        case 97:
        case 98:
        case 99:
            value = 80 + d20();
            break;
        case 0:
            value = 100 + d20();
            break;
    }
    return value;
}


// Roll for Character caste
function rollCaste(characterType, d100) {
    var caste = "";
    switch (characterType) {
        case "pure stock":
            caste = getPureStockCaste(d100);
            break;
        case "clone comfort":
            caste = getCloneComfortCaste(d100);
            break;
        case "clone labor":
            caste = getCloneLaborCaste(d100);
            break;
        case "clone military":
            caste = getCloneMilitaryCaste(d100);
            break;
        case "bioreplica pleasure":
            caste = getBioreplicaPleasureCaste(d100);
            break;
        case "bioreplica industrial":
            caste = getBioreplicaIndustrialCaste(d100);
            break;
        case "bioreplica clerical":
            caste = getBioreplicaClericalCaste(d100);
            break;
        case "bioreplica infiltration":
            caste = getBioreplicaInfiltrationCaste(d100);
            break;
        case "bioreplica battle":
            caste = getBioreplicaBattleCaste(d100)
            break;
        case "transhuman":
            caste = getTranshumanCaste(d100);
            break;
        case "cyborg":
            caste = getCyborgCaste(d100);
            break;
        case "ghost mutant":
            caste = getGhostMutantCaste(d100);
            break;
        case "mild mutant":
        case "typical mutant":
        case "severe mutant":
        case "freakish horror mutant":
            caste = getMutantCaste(d100);
            break;
        case "bestial human":
            caste = getBestialHumanCaste(d100);
            break;
    }
    return caste;
}

function getPureStockCaste(d100) {
    switch (d100) {

    }
}

function getCloneComfortCaste(d100) {

}

function getCloneLaborCaste(d100) {

}

function getCloneMilitaryCaste(d100) {

}

function getBioreplicaPleasureCaste(d100) {

}

function getBioreplicaIndustrialCaste(d100) {

}

function getBioreplicaClericalCaste(d100) {

}

function getBioreplicaInfiltrationCaste(d100) {

}

function getBioreplicaBattleCaste(d100) {

}

function getTranshumanCaste(d100) {

}

function getCyborgCaste(d100) {

}

function getGhostMutantCaste(d100) {

}

function getMutantCaste(d100) {

}

function getBestialHumanCaste(d100) {

}

function characterTypeBonus(characterObj) {
    var type = characterObj["type"];
    switch (type) {

    }
}

// Get skill rolls based off of caste
function skills(characterObj){
    switch (characterObj["caste"]) {
        case "slave labor":
            break;
    }
}

function rollCriminalSkills(d100) {
    
}

function rollWarriorSkills(d100) {

}

function rollEducatedSkills(d100) {

}

function rollMiscSkills(d100) {

}

function rollTechnicalSkill(d10){
    var techSkill = "";
    switch (d10) {
        case 1:
            techSkill = "bio tech";
            break;
        case 2:
            techSkill = "chemical tech";
            break;
        case 3:
        case 4:
            techSkill = "computer tech";
            break;
        case 5:
        case 6:
            techSkill = "electrical tech";
            break;
        case 7:
        case 8:
            techSkill = "mechanical tech";
            break;
        case 9:
        case 10:
            techSkill = "robotics tech";
            break;
    }
    return techSkill;
}

// Add event listener for Generate button
document.getElementById("generateButton").addEventListener("click", function() {
   rollStats(character); 
   console.log(character);
});