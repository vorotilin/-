function rangeslide(value){
    document.getElementById('counterspeed').innerHTML = value;
}
    document.addEventListener('DOMContentLoaded', () => {
const input1 = document.querySelector('#counter-top');
const plus1 = document.querySelector('#plus1');
const minus1 = document.querySelector('#minus1');

plus1.addEventListener('click', function(event) {
    event.preventDefault();
    input1.value = Number(input1.value) + 1;
});

minus1.addEventListener('click', function(event) {
    event.preventDefault();
    if (Number(input1.value) > 1) {
        input1.value = Number(input1.value) - 1;
    } else {
        input1.value = 1; 
    }
});

const input2 = document.querySelector('#counter-bottom');
const plus2 = document.querySelector('#plus2');
const minus2 = document.querySelector('#minus2');

plus2.addEventListener('click', function(event) {
    event.preventDefault();
    input2.value = Number(input2.value) + 1;
});

minus2.addEventListener('click', function(event) {
    event.preventDefault();
    if (Number(input2.value) > 1) {
        input2.value = Number(input2.value) - 1;
    } else {
        input2.value = 1; 
    }
});

const startstop = document.getElementById('start-stop');
let isPlaying = false;
let intervalId;
let currentBeat = 0;

function updateBPM() {
    const counterTop = parseInt(input1.value);
    const counterBottom = parseInt(input2.value);
    const bpm = parseInt(document.getElementById('speed-range').value);
    return (60 / bpm) * (counterBottom / counterTop) * 1000;
}

function playMetronome() {
    const noteDuration = updateBPM();
    intervalId = setInterval(() => {
        const audio = new Audio(currentBeat === 0 ? '../static/sound/first-beat.mp3' : '../static/sound/click.mp3');
        audio.play();
        currentBeat = (currentBeat + 1) % parseInt(input1.value); 
    }, noteDuration);
}

function stopMetronome() {
    clearInterval(intervalId);
    currentBeat = 0; 
}

startstop.addEventListener('click', () => {
    if (isPlaying) {
        stopMetronome();
        startstop.innerText = 'Старт';
    } else {
        playMetronome();
        startstop.innerText = 'Стоп';
    }
    isPlaying = !isPlaying;
});

document.getElementById('speed-range').addEventListener('input', () => {
    if (isPlaying) {
        stopMetronome();
        playMetronome();
    }
});
});

