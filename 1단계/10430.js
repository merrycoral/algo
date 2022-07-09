let input = require('fs').readFileSync('../예제.txt').toString().split(' ');
//let input = require('fs').readFileSync('/dev/stdin').toString().split(' ');

let num = Number(input.length);

for (let i = 0; i <= num; i++) {
  input[i]=Number(input[i]);
}
let A = input[0];
let B = input[1];
let C = input[2];

if(C != 0) {
  //console.log(Math.floor(input[0]/input[1]));
  console.log((A+B)%C);
  console.log(((A%C) + (B%C))%C);
  console.log((A*B)%C);
  console.log(((A%C)*(B%C))%C);
}