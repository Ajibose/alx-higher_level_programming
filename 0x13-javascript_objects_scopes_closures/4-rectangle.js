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

  rotate () {
    const tempVal = this.height;
    this.height = this.width;
    this.width = tempVal;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
