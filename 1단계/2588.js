let fs = require('fs');
const { stringify } = require('querystring');
let input = fs.readFileSync('../예제.txt').toString().split('\r\n');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let numbers = [];
//console.log(input);
for (let i = 0; i < input.length; i++) {
  if (input[i] !== '') {
    numbers.push(Number(input[i].split(' ')));
  }
}
  let num1 = String(numbers[0]).split("");
  let num2 = String(numbers[1]).split("");

  console.log(num1);
  console.log(num2);

let arr3 = [];
for(let i = num2.length -1; i=0; i--) {
  let ten = 0;
  for(let i = num2.length -1; i=0; i--) {
    let a = num2[i]*num1[i];
    let one = 0;
    if(!ten === 0) {
      if(a > 9) {
        one = Number(a.substr(1, 1));
        arr3[0] = arr3[0] + one;
        ten = Number(a.substr(0, 1));
      }else{
        one = a;
        ten = 0;
        arr3[0] = arr3[0] + one;
      }
    }
    if(a > 9) {
      one = Number(a.substr(1, 1));
      ten = Number(a.substr(0, 1));
    }else{
      one = a;
      ten = 0;
    }

    arr3.unshift(one);
    arr3.unshift(ten);
   
    
    
  }
}
console.log(arr3);