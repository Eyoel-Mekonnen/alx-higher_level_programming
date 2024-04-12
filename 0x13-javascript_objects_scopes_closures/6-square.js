#!/usr/bin/node
const SquareCustom = require('./5-square');
class Square extends SquareCustom {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        let array = '';
        for (let j = 0; j < this.size; j++) {
          array = array + c;
        }
        console.log(array);
      }
    }
  }
}
module.exports = Square;
