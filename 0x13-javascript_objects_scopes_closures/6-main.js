#!/usr/bin/node
const Square = require('./6-square');

const s2 = new Square(4);
s2.charPrint();

s2.charPrint('C');

const s1 = new Square(3);
s1.charPrint('D');
s1.double();
s1.charPrint('O');
