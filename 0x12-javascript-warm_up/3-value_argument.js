#!/usr/bin/node

const args = process.argv.forEach((val, index) => {
  if (index === 1) {
    console.log('No hay');
  }
  else if (index > 1) {
    console.log(val);
  }
} );
