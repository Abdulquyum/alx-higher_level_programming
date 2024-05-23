#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const fs = require('fs');
const url = argv[2];
const file = argv[3];

request
  .get(url)
  .on('error', function (err) {
    console.error(err);
  })
  .pipe(fs.createWriteStream(file, 'utf8'));
