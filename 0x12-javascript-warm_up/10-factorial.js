#!/usr/bin/node

const factNumber = parseInt(process.argv[2]);

function factorial (factNumber) {
  if (!factNumber) {
    return (1);
  }
  return factNumber * factorial(factNumber - 1);
}
console.log(factorial(factNumber));
