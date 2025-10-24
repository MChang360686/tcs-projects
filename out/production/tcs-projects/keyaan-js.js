
function switchStatement(a) {
    switch (a) {
        case 1:
            console.log("option 1");
            break;
        case 2:
            console.log("option 2");
            break;
        case 3:
            console.log("option 3");
            break;
        default:
            console.log("IDK")
    }
}

//switchStatement(1)

function addNums(a, b) {
    console.log(a + b);
}

//arrow function
let sum = (a, b)  => console.log(a + b);

/*
addNums(1, 2);
sum(1, 2);
*/

const cars = ["acura", "toyota", "volkswagen"];

function readCars(arr) {
    for (let i = 0; i < arr.length; i++) {
        console.log(arr[i]);
    }
}

readCars(cars);


