#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
