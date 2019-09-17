#!/usr/bin/node

const parameter = process.argv[2];
if (parameter === undefined) {
  console.log('No hay');
} else {
  console.log(process.argv[2]);
}
