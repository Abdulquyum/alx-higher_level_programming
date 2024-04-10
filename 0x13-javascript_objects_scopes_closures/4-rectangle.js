#!/usr/bin/node

class Rectangle {
  width;
  height;
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let iterate = '';
    for (let a = 0; a < this.height; a++) {
      for (let b = 0; b < this.width; b++) {
        iterate += 'X';
      }
      console.log(iterate);
      iterate = '';
    }
  }

  rotate () {
    const dupWidth = this.width;
    this.width = this.height;
    this.height = dupWidth;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
