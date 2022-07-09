let fs = require('fs');
let input = fs.readFileSync('../예제.txt').toString().split(' ');

let num = Number(input.length);

for (let i = 0; i <= num; i++) {
  input[i]=Number(input[i]);
}
console.log(input[0]+input[1]);
console.log(input[0]-input[1]);
console.log(input[0]*input[1]);
if(input[1] != 0) {
  console.log(Math.floor(input[0]/input[1]));
  console.log(input[0]%input[1]);
}