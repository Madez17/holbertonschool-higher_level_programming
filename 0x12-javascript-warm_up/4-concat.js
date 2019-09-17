#!/usr/bin/node

const parameter = process.argv.length;

if (process.argv[2]) {
  console.log((process.argv[2]) + ' is ' + (process.argv[3]));
} else if (parameter === 3) {
  console.log((process.argv[2]) + ' is ' + 'undefined');
} else if (process.argv[2] === undefined) {
  console.log('undefined' + ' is ' + 'indefined');
}
