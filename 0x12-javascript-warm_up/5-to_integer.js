#!/usr/bin/node

const { argv } = require('process');

const a = parseInt(argv[2]);

if (!isNaN(a)) {
  console.log('My number: ' + a);
} else {
  console.log('Not a number');
}
