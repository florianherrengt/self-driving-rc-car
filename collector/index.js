const fetch = require('node-fetch');
const fs = require('fs');

const CAMERA_ADDRESS = 'http://192.168.1.211:8080/live.jpg';
const ARDUINO_SERVER = 'http://localhost:5000'

let requestsPerSeconds = 0;

setInterval(() => {
    console.log('Requests per seconds: ' + requestsPerSeconds);
    requestsPerSeconds = 0;
}, 1000);

function getData() {
    requestsPerSeconds++;
    const date = new Date().valueOf();
    Promise.all([
        fetch(CAMERA_ADDRESS + '?' + date).then(response => {
            return new Promise(resolve => {
                const dest = fs.createWriteStream(`./data/${date}.jpg`);
                response.body.pipe(dest);
                dest.on('finish', () => resolve());
            });
        }),
        fetch(ARDUINO_SERVER + '/status').then(response => {
            return new Promise(resolve => {
                const dest = fs.createWriteStream(`./data/${date}.json`);
                response.body.pipe(dest);
                dest.on('finish', () => resolve());
            });
        })
    ])
    .then(() => getData())
    .catch(error => console.log(error))
}

getData();
