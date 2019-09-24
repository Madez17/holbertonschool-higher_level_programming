#!/usr/bin/node
class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  // Method charPrint
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    while (i < this.height) {
      console.log(c.repeat(this.width));
      i++;
    }
  }
}
module.exports = Square;
