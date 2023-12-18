/*
Question; how do we write a switch case with a 1000 different options?  

Even *if* we use a normal switch statement we still have 1000 items to type out and use.  And
we don't want to chain too many if-else statements together.  

I propose we reduce the number of choices by using buckets.  

First, we use a switch case to check if the random number is a "bucket" value
that marks the boundary between one bucket and the other.  IF the generated number
belongs in this group of numbers, then it should be immediately clear which bucket
this number belongs to.  If it does not, then we proceed to the next stage  

The next stage consists of using a binary search to determine what bucket a number belongs in.  
If the number is less than the bucket value at the centerpoint, we make a new centerpoint and
compare the bucket value at that centerpoint.

THEN once we figure out what bucket an item is contained in, we can use a switch case on either a string
or number to assign a specific value
*/

// Returns a pseudorandom number from 1 - 1000
function d1000() {
    return Math.floor(Math.random() * 1000) + 1;
}

function d100() {
    return Math.floor(Math.random() * 100) + 1;
}

// List of "bucket" numbers
let arr = [9, 20, 32, 36, 44, 52, 59, 71, 79, 89, 102]

// switch case
function check(array, num) {
    for(let i = 0; i < array.length; i++) {
        if (num == array[i]) {
            return num;
        }
    }
}

// binary search function
function binSearch(num, array) {
    let index = array.length / 2;
    if (num == array[index]) {
        return num;
    }
}
