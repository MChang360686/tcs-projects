/*
Question; how do we write a switch case with a 1000 different options?  

Even *if* we use a normal switch statement we still have 1000 items to type out and use.  And
we don't want to chain too many if-else statements together.  

I propose we reduce the number of choices by using buckets.  

First, we use a switch case to check if the random number is a "bucket" value
that marks the boundary between one bucket and the other.  IF the generated number
belongs in this group of numbers, then it should be immediately clear which bucket
this number belongs to.  If it does not, then we proceed to the next stage  

The next stage consists of using a pseudorandom weighted choice algorithm to choose
from a list of values.  The weight of an item depends on the range of the bucket
and what percent the range of the item constitutes of the bucket.  Therefore if
the first bucket is 253, and the first item is 1-9, the weight for the first
item would be 9/253 or 0.04.
*/

// Returns a pseudorandom number from 1 - 1000
function d1000() {
    return Math.floor(Math.random() * 1000) + 1;
}

function d100() {
    return Math.floor(Math.random() * 100) + 1;
}

function d10() {
    return Math.floor(Math.random() * 10) + 1;
}

// List of "bucket" numbers
let arr = [9, 20, 32, 36, 44, 52, 59, 71, 79, 89, 102]

let b1 = [253, 511, 754, 1000]
let b2 = [1, 2 , 3, 4, 5, 6, 7, 8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
let b2Weights = [.04, .04, .04, .01]

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
    } else if (num == 1) {

    } else if (num == 2) {

    } else {
        
    }
}
