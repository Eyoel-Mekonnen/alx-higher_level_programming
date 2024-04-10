#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2], 10);
if (typeof (num) !== 'number' || typeof (argv[2]) === 'string') {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
