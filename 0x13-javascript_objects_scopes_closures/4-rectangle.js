#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w, h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method Print
  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }

  // Method Rotate
  rotate () {
    const change = this.width;
    this.width = this.height;
    this.height = change;
  }

  // Method Double
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
