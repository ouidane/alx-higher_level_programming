#!/usr/bin/node

const firstArg = process.argv[2];

if (firstArg === undefined || isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(firstArg);
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
