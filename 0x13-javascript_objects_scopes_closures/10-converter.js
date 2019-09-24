#!/usr/bin/node

// Function convert a number of a base 10 to another
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
