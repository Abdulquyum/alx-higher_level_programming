#!/usr/bin/node

const { argv } = require('process');

const arr = [];
if (argv.length < 4) {
  console.log('0');
} else {
  for (let a = 2; a < argv.length; a++) {
    arr.push(argv[a]);
  }
  arr.sort();
  console.log(arr[arr.length - 2]);
}
