/*
Question; how do we write a switch case with a 1000 different options?  

Even *if* we use a normal switch statement we still have 1000 items to type out and use.  And
we don't want to chain too many if-else statements together.  

I propose we reduce the number of choices by using buckets.  First we use a binary search to
determine what bucket a number belongs in.  Each bucket is marked by a single value; if the
value we are looking for is LESS THAN a value A but greater than the value B that marks the previous
bucket then the value is in the bucket of value A.

THEN once we figure out what bucket an item is contained in, we can use a switch case on either a string
or number
*/

// Returns a pseudorandom number from 0 - 999
function d1000() {
    return Math.floor(Math.random() * 1000);
}

// Make a list of 1000 items (0 - 999)
function makeList() {
    let newList = [];
    for (let i = 0; i < 1000; i++) {
        newList.push(i);
    }
    return newList;
}

// binary search function
function binSearch(item, list) {
    let index = list.length / 2;
    console.log(index);
}

let numList = [0, 1, 2, 3, 4, 5];
binSearch(3, numList);
console.log(makeList());