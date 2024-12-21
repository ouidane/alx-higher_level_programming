#!/usr/bin/node

const data = require('./101-data').dict;
const newDict = Object.entries(data).reduce((outputDict, [key, value]) => {
  outputDict[value] = outputDict[value] ? [...outputDict[value], key] : [key];
  return outputDict;
}, {});

console.log(newDict);
