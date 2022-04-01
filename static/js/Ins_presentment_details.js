function selectPackage(count) {
    resetBorders();
    resetIcons();
    resetButtons()
    let table = document.getElementsByClassName('table_hidden');
    let btns = document.querySelectorAll('.select--btn');

    table[0].children[count - 1].className = "select";

    if (count == 3) {
        let icons = document.querySelectorAll('.icon-first');
        for (var i = 0; i < icons.length; i++) {
            icons[i].children[0].children[0].children[1].style.fill = '#208f01'
        }
        btns[0].style.background = '#a6a6a6';
        btns[0].style.color = '#fff';
        console.log("Best!");


    }
    if (count == 4) {
        let icons = document.querySelectorAll('.icon-second');
        for (var i = 0; i < icons.length; i++) {
            icons[i].children[0].children[0].children[1].style.fill = '#208f01'
        }
        btns[1].style.background = '#a6a6a6';
        btns[1].style.color = '#fff';
        console.log("better!");

    }
    if (count == 5) {
        let icons = document.querySelectorAll('.icon-third');
        for (var i = 0; i < icons.length; i++) {
            icons[i].children[0].children[0].children[1].style.fill = '#208f01'
        }
        btns[2].style.background = '#a6a6a6';
        btns[2].style.color = '#fff';
        console.log("good!");

    }
    if (count == 6) {
        btns[3].style.background = '#a6a6a6';
        btns[3].style.color = '#fff';
    }


}

function resetBorders() {
    let table = document.getElementsByClassName('table_hidden');
    let nodes = table[0].children;
    for (var i = 0; i < nodes.length; i++) {
        nodes[i].classList.remove('select');
    }

}

function resetIcons() {
    let iconsFirst = document.querySelectorAll('.icon-first');
    for (var i = 0; i < iconsFirst.length; i++) {
        iconsFirst[i].children[0].children[0].children[1].style.fill = '#c5c5c5'
    }
    let iconsSecond = document.querySelectorAll('.icon-second');
    for (var i = 0; i < iconsSecond.length; i++) {
        iconsSecond[i].children[0].children[0].children[1].style.fill = '#c5c5c5'
    }
    let iconsThird = document.querySelectorAll('.icon-third');
    for (var i = 0; i < iconsThird.length; i++) {
        iconsThird[i].children[0].children[0].children[1].style.fill = '#c5c5c5'
    }

}

function resetButtons() {
    let btns = document.querySelectorAll('.select--btn');
    for (var i = 0; i < btns.length; i++) {
        btns[i].style.background = 'transparent'
        btns[i].style.color = '#000000';

    }

}


document.onload = selectPackage(4)