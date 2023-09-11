#!/usr/bin/node

/*Script that prints My number: <first argument converted in integer>*/

const arg = process.argv[2];
if (isNaN(Number(arg))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(arg, 10)}`);
}
