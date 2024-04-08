#!/usr/bin/node
const { argv } = require('process');
if ((argv.length - 2) === 0) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
