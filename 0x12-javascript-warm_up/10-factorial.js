#!/usr/bin/node
function factorial (a) {
  if (a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
const { argv } = require('process');
const num1 = argv[2];
if (isNaN(num1)) {
  console.log('1');
} else {
  const num2 = factorial(num1);
  console.log(num2);
}
