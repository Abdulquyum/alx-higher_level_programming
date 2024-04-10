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
}
module.exports = Rectangle;
