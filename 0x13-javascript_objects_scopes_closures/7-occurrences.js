#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let b = 0;
  for (let a = 0; a < list.length; a++) {
    if (list[a] === searchElement) {
      b += 1;
    }
  }
  return b;
};
