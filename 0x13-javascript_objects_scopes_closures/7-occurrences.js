#!/usr/bin/node

// Function count the number of ocurrence in a list
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let anotherCount = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      anotherCount++;
    }
    i++;
  }
  return anotherCount;
};
