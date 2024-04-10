#!/usr/bin/node

const Sqr = require('./5-square');

class Square extends Sqr {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      let prt = '';
      for (let a = 0; a < this.height; a++) {
        for (let b = 0; b < this.width; b++) {
          prt += c;
        }
        console.log(prt);
        prt = '';
      }
    } else {
      let prt = '';
      for (let a = 0; a < this.height; a++) {
        for (let b = 0; b < this.width; b++) {
          prt += 'X';
        }
        console.log(prt);
        prt = '';
      }
    }
  }
}
module.exports = Square;
