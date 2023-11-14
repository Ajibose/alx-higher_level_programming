#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;

    while (i < this.height) {
      let str = '';
      j = 0;
      while (j < this.width) {
        str += 'X';
        j++;
      }
      console.log(str);
      i++;
    }
  }
}

module.exports = Rectangle;
