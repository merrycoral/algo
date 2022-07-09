let fs = require('fs');
let input = fs.readFileSync('../예제.txt').toString().split('\r\n');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let numbers = [];
//console.log(input);
for (let i = 0; i < input.length; i++) {
  if (input[i] !== '') {
    numbers.push(input[i].split(' '));
  }
}
//console.log(numbers);
for (let i = 0; i < numbers.length; i++){
  let num1 = Number(numbers[i]);
  let num2 = Number(numbers[i]);

  console.log(num1 + num2);
  console.log(num1);
  console.log(num2);
}