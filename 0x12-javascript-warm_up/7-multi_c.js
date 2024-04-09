#!/usr/bin/node

const { argv } = require('process');

let i;
const a = parseInt(argv[2]);
if (!isNaN(a)) {
  for (i = 0; i < a; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
