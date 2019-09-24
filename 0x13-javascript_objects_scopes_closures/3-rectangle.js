#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w, h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method
  print () {
    let i = 0;
    while (i < this.height) {
      console.log('x'.repeat(this.width));
      i++;
    }
  }
}

module.exports = Rectangle;
