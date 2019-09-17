#!/usr/bin/node

const parameter = process.argv.length;

if (parameter > 3) {
  console.log((process.argv[2]) + ' is ' + (process.argv[3]))
}
else if (parameter === 3) {
  console.log((process.argv[2]) + ' is ' + "undefined")
}
else if (parameter < 3) {
  console.log("No a number")
}
