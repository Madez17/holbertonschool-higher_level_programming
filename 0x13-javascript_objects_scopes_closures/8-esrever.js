#!/usr/bin/node

// Function that reverse a list
exports.esrever = function (list) {
  const newArray = [];
  let i = list.length - 1;
  while (i >= 0) {
    newArray.push(list[i]);
    i--;
  }
  return newArray;
};
