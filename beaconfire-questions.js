let a = '567'
let b = '--5--67'

function StringChallenge(str) { 

    // code goes here  
    let result = '';
    
    // do the first pass
    for (let i = 0; i < str.length; i++) {
      let current = parseInt(str[i]);
      let next = parseInt(str[i+1]);
  
      result += current;
  
      // check if concurrently odd
      if (current % 2 == 1 && next % 2 == 1) {
        result += "-";
      }
    }
  
    //console.log(result)
  
    str = result;
    result = '';
  
    // now add two -- on both sides of each chunk
    for (let j = 0; j < str.length; j++) {
      let current = str[j];
      let next = str[j+1];
  
      if (parseInt(current) % 2 == 1) {
        result += '--' + current + '--';
      } else if (parseInt(current) % 2 == 0) {
        result += current;
      } else if (current == '-') {
        result += current;
      }
      
  
    }
  
    //console.log(result);
  
    return result; 
  
  }
     
// keep this function call here 
console.log(StringChallenge(a));