if ('addEventListener' in document) {
    document.addEventListener('DOMContentLoaded', function() {
        FastClick.attach(document.body); // remote 300ms delay on mobile
    }, false);
}

// send a request to switch on a GPIOs and turn on a LED
function switchOn(direction) {
    fetch('http://localhost:5000/' + direction + '-on')
        .then(response => response.text())
        .then(response => console.log(response))
        .catch(error => console.log(error));
}

// send a request to switch off a GPIOs and turn off a LED
function switchOff(direction) {
    fetch('http://localhost:5000/' + direction + '-off')
        .then(response => response.text())
        .then(response => console.log(response))
        .catch(error => console.log(error));
}

// binding the buttons on the UI
['forward', 'backward', 'left', 'right'].forEach(key => {
    document.getElementById(key).addEventListener('mousedown', () => switchOn(key));
    document.getElementById(key).addEventListener('mouseup', () => switchOff(key));
});

// keep track of which keys are down
const keysDown = {
    up: false,
    down: false,
    left: false,
    right: false,
};

// mapping keys to directions
const keyDirections = {
    up: 'forward',
    down: 'backward',
    left: 'left',
    right: 'right',
};

// binding keyboard keys
['up', 'down', 'left', 'right'].forEach(key => {
    Mousetrap.bind(key, () => {
        if (!keysDown[key]) {
            keysDown[key] = true;
            switchOn(keyDirections[key]);
        }
    }, 'keydown');
    Mousetrap.bind(key, () => {
        keysDown[key] = false;
        switchOff(keyDirections[key]);
    }, 'keyup');
});
