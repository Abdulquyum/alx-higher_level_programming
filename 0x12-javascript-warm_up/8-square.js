#!/usr/bin/node

const { argv } = require('process');

const arg = parseInt(argv[2]);
let s = '';

if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    for (let i = 0; i < arg; i++) {
      s += 'X';
    }
    console.log(s);
    s = '';
  }
} else {
  console.log('Missing size');
}
