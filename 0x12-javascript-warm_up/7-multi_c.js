#!/usr/bin/node

/* A script that prints x times “C is fun” */

const argscount = process.argv[2];
if (isNaN(argscount, 10)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(argscount); i++) {
    console.log('C is fun');
  }
}
