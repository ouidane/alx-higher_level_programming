#!/usr/bin/node

const firstArg = Number(process.argv[2]);
const secondArg = Number(process.argv[3]);

function add(a, b) {
  const c = a + b;
  console.log(c);
}

add(firstArg, secondArg);
