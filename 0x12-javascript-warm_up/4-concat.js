#!/usr/bin/node
const { argv } = require('process');

if (argv[2] === undefined) {
  process.stdout.write('undefined');
} else if (argv[2] !== undefined) {
  process.stdout.write(argv[2]);
}
process.stdout.write(' is ');
if (argv[3] !== undefined) {
  process.stdout.write(argv[3]);
  process.stdout.write('\n');
} else if (argv[3] === undefined) {
  process.stdout.write('undefined');
  process.stdout.write('\n');
}
