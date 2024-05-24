#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

if (argv.length === 3) {
  request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, async function (error, resp, body) {
    if (error != null) {
      return;
    }
    if (resp.statusCode !== 200) {
      return;
    }
    const characters = JSON.parse(body).characters;

    for (let c = 0; c < characters.length; c++) {
      const doRequest = () => new Promise((resolve, reject) => request.get(characters[c], function (error, resp, body) {
        if (error !== null) {
          reject(error);
        }
        if (resp.statusCode !== 200) {
          return;
        }
        resolve(JSON.parse(body).name);
      }));

      const cName = await doRequest();

      console.log(cName);
    }
  }
  );
}
