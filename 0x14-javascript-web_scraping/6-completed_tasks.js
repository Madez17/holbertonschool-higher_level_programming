#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body);
    const dict = {};

    for (let i = 0; i < list.length; i++) {
      if (list[i].completed === true) {
        const user = list[i].userId;
        if (user in dict) {
          dict[user]++;
        } else {
          dict[user] = 1;
        }
      }
    }
    console.log(dict);
  }
});
