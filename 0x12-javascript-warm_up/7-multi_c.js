#!/usr/bin/node
const { argv } = require('process');
if ((argv.length - 2) === 2) {
  console.log('Missing number of occurrences');
}
let num = parseInt(argv[2], 10);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
}
while (num > 0) {
  console.log('C is fun');
  num--;
}
