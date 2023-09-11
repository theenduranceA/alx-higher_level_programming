#!/usr/bin/node

/* Sript that prints a message depending on number of aruments passed */

const argscount = process.argv.length;
if (argscount === 2) {
  console.log('No argument');
} else if (argscount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
