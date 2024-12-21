#!/usr/bin/node

const myFs = require('fs');

const firstArg = myFs.readFileSync(process.argv[2]).toString();
const secondArg = myFs.readFileSync(process.argv[3]).toString();
myFs.writeFileSync(process.argv[4], firstArg + secondArg);
