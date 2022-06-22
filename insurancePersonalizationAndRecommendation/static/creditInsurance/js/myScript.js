// Navigation - add active class on selected list item
let listItems = document.querySelectorAll('.sidebar .nav-links .mainLinks li');

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

// Dashboard SideNav
// let arrow = document.querySelectorAll(".arrow");
// for (var i = 0; i < arrow.length; i++) {
//     arrow[i].addEventListener("click", (e) => {
//         let arrowParent = e.target.parentElement.parentElement;
//         arrowParent.classList.toggle("showMenu");
//     });
// }

let arrow = document.querySelectorAll(".subMenu");
for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e) => {
        e.currentTarget.classList.toggle("showMenu");
    });
}

let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx.bx-menu");

// sidebarBtn.addEventListener("click", () => {
//     sidebar.classList.toggle("close");
// });


// SideBar Navigation for Mobile
function openNavMob() {
    document.getElementById("sidebarMob").style.width = "100%";
    document.getElementsByTagName('body')[0].classList.add('hidden');
}

function closeNavMob() {
    document.getElementById("sidebarMob").style.width = "0%";
    document.getElementsByTagName('body')[0].classList.remove('hidden');
}

// Select Applicant Script as per radio button selection

let radioBtns = document.querySelectorAll('.jointApplicantDetails .form-check-input[name="jointApplicant"]');
let selectBox = document.querySelector('.selectBox');
let selectBoxMultiple = document.querySelector('.selectBoxMultiple');

function selectedItem(e) {
    if(e.currentTarget.checked && e.currentTarget.value == "Yes") {
        selectBox.style.display = "none";
        selectBoxMultiple.style.display = "block"; 
    }

    else if(e.currentTarget.checked && e.currentTarget.value == "No") {
        selectBox.style.display = "block";
        selectBoxMultiple.style.display = "none";
    }
}

radioBtns.forEach(item => {
    item.addEventListener('change', selectedItem);
})



// Anecdotes - Archetype selection script

let selectBtn = document.querySelectorAll('.selectBtn');

selectBtn.forEach((ele) => {
    ele.addEventListener('click', addActivateClass);
})

function addActivateClass() {
    selectBtn.forEach((btnParent) => {
        btnParent.parentElement.classList.remove('activate');
    })
    this.parentElement.classList.add('activate');
}

// Anecdotes - Archetype Information script

let specificReaction = document.querySelectorAll('.navObjectionBlock .reactionBlock .image');

specificReaction.forEach((ele) => {
    ele.addEventListener('click', reactionActive);
})

function reactionActive(e) {
    let allTargetReaction = e.currentTarget.parentElement.children;
    let getID = e.currentTarget.id;

    $(allTargetReaction).removeClass('active');
    $('#' + getID).addClass('active');
}

// FAQ Search - Reaction
let faqSearchReaction = document.querySelectorAll('.faqSearchSectionBlock .reactionBlock .image');

faqSearchReaction.forEach((ele) => {
    ele.addEventListener('click', faqReactionActive)
})

function faqReactionActive(e) {
    let allTargetFAQReaction = e.currentTarget.parentElement.children;
    let getFAQID = e.currentTarget.id;

    $(allTargetFAQReaction).removeClass('active');
    $('#' + getFAQID).addClass('active');
}

// FAQ Search - Filter

let search = document.querySelector('#search');
let faqSearchSectionRow = document.querySelectorAll('.faqSearchSection .row');

//search.addEventListener('keyup', (e) => {
//    let filterVal = e.target.value.toLowerCase();
//
//    faqSearchSectionRow.forEach((row) => {
//        row.querySelector('.faqSearchSectionBlock .archetypeInfoDesc').innerText.toLowerCase().indexOf(filterVal) > -1 ? (row.style.display = "") : (row.style.display = "none");
//    })
//})

function exitApplication(e){
    document.location.href = "/insurance/exit/1";
}