#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2], 10);
if ((argv.length - 2) === 2 || isNaN(num)) {
  console.log('Missing size');
}
for (let i = 0; i < num; i++) {
  let array = '';
  for (let j = 0; j < num; j++) {
    array = array + 'X';
  }
  console.log(array);
}
