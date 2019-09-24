#!/usr/bin/node

// Write a File
const fs = require('fs');
const data = process.argv[3];

fs.writeFile(process.argv[2], data, (err) => {
  if (err) console.log(err);
});
