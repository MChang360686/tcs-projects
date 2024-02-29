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

Heavily inspired by https://dev.to/trekhleb/weighted-random-algorithm-in-javascript-1pdc
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

let buckets = [253, 511, 754, 1000]
let b1 = [1, 2 , 3, 4, 5, 6, 7, 8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
let b1Weights = [.04, .04, .04, .01]
let b2 = [24, 44]
let b2Weights = []
let b3 = [45, 63]
let b3Weights = []
let b4 = [64, 91]
let b4Weights = []

// choose random num and find which bucket it belongs to
function check(num, buckets) {
    let arr = 0;

    for(let i = 0; i < buckets.length; i++) {
        if (num <= buckets[i]) {
            arr = num;
        }
    }

    if (arr == 253){
        //use b1
    } else if (arr == 511) {

    } else if (arr == 754) {

    } else {

    }

}


function checkB1(bucketOne, bOneWeights) {

}

function checkB2() {
    
}


function checkB3() {
    
}


function checkB4() {
    
}


