#!/usr/bin/node

const fs = require('fs');
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
    if (error) {
            console.log(err)
    }
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) {
       console.log(err);
     }
    });
});
