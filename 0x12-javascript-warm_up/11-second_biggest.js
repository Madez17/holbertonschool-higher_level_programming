#!/usr/bin/node

if (process.argv.length > 3) {
  let numbers = process.argv.slice(2);
  numbers = numbers.sort(function(num1, num2) {
    return num2 - num1;
  });
  console.log(numbers[1]);
} else {
  console.log(0);
}
