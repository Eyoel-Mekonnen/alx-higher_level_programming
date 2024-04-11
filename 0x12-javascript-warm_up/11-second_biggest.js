#!/usr/bin/node
const { argv } = require('process');
if (argv.length === 2) {
  console.log('0');
}
const array = [];
for (let i = 2; i < argv.length; i++) {
  let value = parseInt(argv[i]);
  if (argv.length === 3 && !isNaN(value)) {
    value = value - 1;
    console.log(value);
  } else if (!isNaN(value)) {
    array.push(value);
  }
}
if (array.length !== 0) {
  array.sort((a, b) => a - b);
  console.log(array[(array.length) - 2]);
}
