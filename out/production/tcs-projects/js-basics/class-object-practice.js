let person = {name: "Bob", age: 32};
var person2 = {name: "Alice", age: 26};

//console.log(person.name);

function logNames() {
    for (key in person) {
        console.log(key);
    }

}

function logValues() {
    Object.values(person).forEach(val => console.log(val));

}

logNames();
logValues();