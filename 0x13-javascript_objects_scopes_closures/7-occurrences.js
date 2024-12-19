#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  let count = 0;
  for (let element = 0; element < list.length; element++) {
    if (searchElement === list[element]) {
      count++;
    }
  }
  return count;
};
