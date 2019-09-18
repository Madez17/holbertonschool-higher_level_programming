#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else if (process.argv[2] > 0) {
  let i = 0;
  while (i < process.argv[2]) {
    console.log('x'.repeat(process.argv[2]));
    i++;
  }
}
