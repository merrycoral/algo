let fs = require('fs');
let input = fs.readFileSync('../예제.txt').toString().split(' ');

let num = Number(input.length);
let answerStr = '';

let num1 = '';
let num2 = '';

for (let i = 0; i <= num; i++) {
  //console.log(input[i]);
}
if(input[1] != 0) {
  answerStr = input[0]/input[1]
  console.log(answerStr);
}
/*
let input = require('fs').readFileSync('../예제.txt').toString().split(' ');
//let input = require('fs').readFileSync('../예제.txt').toString().split('\n');
let count = Number(input);
let answerStr = '';

for(let i = 1; i <= count; i++){
    console.log(input[0]);
    //let num = input[i].split(" ");
    //answerStr += Number(num[0]) + Number(num[1]) + "\n";
}



//console.log(answerStr);
console.log(count);
console.log(input[0]);
*/