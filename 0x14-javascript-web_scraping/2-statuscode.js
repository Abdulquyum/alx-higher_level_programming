#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const url = argv[2];

request.get(url, function (error, response) {
  if (error) {
    console.log('code:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
