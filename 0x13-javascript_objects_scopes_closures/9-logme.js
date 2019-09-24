#!/usr/bin/node

// Function print the number of arguments
let i = 0;
exports.logMe = function (item) {
  console.log(i + ':' + item);
  i++;
};
