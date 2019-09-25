#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    let cont = 0;
    for (let i = 0; i < film.results.length; i++) {
      for (let n = 0; n < film.results[i].characters.length; n++) {
        if (film.results[i].characters[n].includes('/18/')) {
          cont++;
        }
      }
    }
    console.log(cont);
  }
});
