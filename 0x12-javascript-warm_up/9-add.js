#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const { argv } = require('process');
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  add(num1, num2);
}
