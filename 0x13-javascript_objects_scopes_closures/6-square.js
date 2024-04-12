#!/usr/bin/node
const SquareCustom = require('./5-square');
class Square extends SquareCustom {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let array = '';
        for (let j = 0; j < this.height; j++) {
          array = array + c;
        }
        console.log(array);
      }
    }
  }
}
module.exports = Square;
