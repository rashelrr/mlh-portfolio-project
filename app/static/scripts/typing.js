var i = 0;
var txt = 'Hi, I\'m Rashel';
var speed = 80;

window.onload = function typeWriter() {
    if (i < txt.length) {
    document.getElementById("typed-out").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
    }
};