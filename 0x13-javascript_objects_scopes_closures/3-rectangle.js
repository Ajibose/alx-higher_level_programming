#!/usr/bin/node

class Rectangle {
  constructor (h, w) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    let i = 0;
    let j = 0;

    while (i < this.width) {
      str = '';
      j = 0;
      while (j < this.height) {
        str += 'X';
        j++;
      }
      console.log(str);
      i++;
    }
  }
}

module.exports = Rectangle;
