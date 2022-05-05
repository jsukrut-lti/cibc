// Menu Toggle
let toggle = document.querySelector('.toggle');
let navigation = document.querySelector('.navigation');
let main = document.querySelector('.main')

toggle.onclick = () => {
    navigation.classList.toggle('active');
    main.classList.toggle('active');
}

// navigation - add active class on selected list item
let listItems = document.querySelectorAll('.navigation ul li');

function activeLink() {
    listItems.forEach((item) => {
        item.classList.remove('active');
    })
    this.classList.add('active');
}

listItems.forEach((item) => {
    item.addEventListener('click', activeLink);
})

// Header Toggle Button for Client and Rep

let toggleBtn = document.querySelectorAll('.switchBtn .toggleBtn');

function activeBtn() {
    toggleBtn.forEach((item) => {
        item.classList.remove('activeBtn');
    })
    this.classList.add('activeBtn');
}

toggleBtn.forEach((item) => {
    item.addEventListener('click', activeBtn)
})