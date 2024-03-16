window.onload = function() {
    let sec = 0;
    let min = 0;
    let hrs = 0;
    let amin = document.querySelector("#minutes");
    let ahrs = document.querySelector("#hours");
    let asec = document.querySelector("#seconds");
    let startbtn = document.querySelector("#start");
    let stopbtn = document.querySelector("#stop");
    let resetbtn = document.querySelector("#reset");
    let Interval;

    function startTimer () {
        sec++;
        if (sec <= 9) {
            asec.innerHTML = '0' + sec;
        } else {
            asec.innerHTML = sec;
        }

        if (sec > 59) {
            min++;
            amin.innerHTML = (min <= 9 ? '0' : '') + min;
            sec = 0;
            asec.innerHTML = '0' + sec;
        }

        if (min > 59) {
            hrs++;
            ahrs.innerHTML = (hrs <= 9 ? '0' : '') + hrs;
            min = 0;
            amin.innerHTML = '0' + min;
        }
    };

    startbtn.onclick = () => {
        clearInterval(Interval);
        Interval = setInterval(startTimer, 1000); // 1000 milliseconds = 1 second
    };

    stopbtn.onclick = () => {
        clearInterval(Interval);
    };

    resetbtn.onclick = () => {
        clearInterval(Interval);
        sec = 0;
        min = 0;
        hrs = 0;
        asec.innerHTML = '00';
        amin.innerHTML = '00';
        ahrs.innerHTML = '00';
    };
};