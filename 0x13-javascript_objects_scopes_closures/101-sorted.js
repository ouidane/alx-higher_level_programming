#!/usr/bin/node
const data = require('./101-data').dict;

const entries = Object.entries(data);
const values = Object.values(data);
const uniqueValues = [...new Set(values)];
const result = {};

for (const i in uniqueValues) {
  const keysList = [];
  for (const j in entries) {
    if (entries[j][1] === uniqueValues[i]) {
      keysList.unshift(entries[j][0]);
    }
  }
  result[uniqueValues[i]] = keysList;
}
console.log(result);
