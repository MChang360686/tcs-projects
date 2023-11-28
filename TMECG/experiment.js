/*
Question; how do we write a switch case with a 1000 options?

Even *if* we use a normal switch statement we still have 1000 items to type out and use

I propose we reduce the number of choices by using buckets.  First we use a binary search to
determine what bucket a number belongs in.  Each bucket has subcategories.
*/

// Returns a pseudorandom number from 0 - 999
function d1000() {
    return Math.floor(Math.random() * 1000);
}

// binary search function
