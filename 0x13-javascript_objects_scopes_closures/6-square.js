#!/usr/bin/node

const Square1 = require('./5-square.js');

class Square extends Square1 {
  charPrint (c) {
    let printCh = 'X';
    if (c !== undefined) {
      printCh = c;
    }
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += printCh;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
