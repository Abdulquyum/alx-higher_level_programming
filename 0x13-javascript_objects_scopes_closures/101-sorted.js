#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = Object.entries(dict).map(({key, value}) => ({key: [value]}));
console.log(newDict);
