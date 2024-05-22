#!/usr/bin/node

const { argv } = require('process');
const file = argv[2];
const data = argv[3];
const fs = require('fs');

fs.writeFile(file, data, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
