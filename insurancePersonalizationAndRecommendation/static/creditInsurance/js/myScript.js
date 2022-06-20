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

selectBox.addEventListener('change', () => {
    if(div.classList.contains('d-block') == true){
        error.classList.remove('d-block');
    }
    error.classList.add('d-none');
})

selectBoxMultiple.addEventListener('change', () => {
    if(div.classList.contains('d-block') == true){
        error.classList.remove('d-block');
    }
    error.classList.add('d-none');
})

function selectedItem(e) {
    if(e.currentTarget.checked && e.currentTarget.value == "Yes") {
        selectBox.style.display = "none";
        selectBoxMultiple.style.display = "block"; 
    }

    else if(e.currentTarget.checked && e.currentTarget.value == "No") {
        selectBox.style.display = "block";
        selectBoxMultiple.style.display = "none";
    }
    if(div.classList.contains('d-block') == true){
        error.classList.remove('d-block');
    }
    error.classList.add('d-none');
}

radioBtns.forEach(item => {
    item.addEventListener('change', selectedItem);
})

// Exit Assessment - Show Objection as per radio button selection

let exitAssessmentReason = document.querySelectorAll('.exitReason .form-check-input[name="exitAssessmentReason"]');
let obejctionData = document.querySelector('.obejctionData');

function reasonChange(e) {
    if(e.currentTarget.checked && e.currentTarget.value == "coverage") {
        obejctionData.innerHTML = `
        <p>Is your existing insurance enough to cover your debt and look after your family's immediate and long-term needs?</p>
        <p>Does your existing insurance cover both you and your co-borrower/guarantor?</p>
        <p class="mb-0">Have you considered if you leave your employer or lose your job, that any group coverage you have through your employer may terminate, meaning you and your family could be left without coverage?</p>`; 
    }
    else if(e.currentTarget.checked && e.currentTarget.value == "expensive") {
        obejctionData.innerHTML = `
        <p>I agree it is an additional expense. Without a plan, though, have you considered what would happen if you could no longer afford to make your regular payments on your [new borrowing product]</p>
 
        <p>My main priority right now is to help you understand the value/importance of having a plan that protects your financial future, whether or not you choose to take CIBC's optional creditor's insurance</p> 
        
        <p class="mb-0">[Note: If a quote has not yet been provided] May I provide you with a quote to help you decide if any of these protection plans are within your budget?</p>`;
    }
    else if(e.currentTarget.checked && e.currentTarget.value == "noTime") {
        obejctionData.innerHTML = `<p>Content Not Available</p>`;
    }
    else if(e.currentTarget.checked && e.currentTarget.value == "interested") {
        obejctionData.innerHTML = `
        <p>Ok, I appreciate that. My main priority right now is to help you understand the value/importance of having a plan that protects your financial future, whether or not you choose to take CIBC's optional creditor's insurance.</p>
        
        <p class="mb-0">The benefit of CIBC creditor insurance is that it can help to pay down or payoff your debt, leaving your other insurance/savings/assets available to support your family when you are not able to and preserve your family wealth.</p>`;
    }
    else if(e.currentTarget.checked && e.currentTarget.value == "think") {
        obejctionData.innerHTML = `
        <p>Ok, I appreciate that. My main priority right now is to help you understand the value/importance of having a plan that protects your financial future , whether or not you choose to take CIBC's optional creditor's insurance.</p>
        
        <p>I'll be happy to share some information for your consideration, [provide client with Creditor insurance product summary to review].</p>

        <p class="mb-0">I would like you to take the time to research your protection needs. Look at the CIBC Creditor Insurance product summaries with the different coverages we offer, talk to friends or family and even do some research online on different types of insurance offerings out there. One of my main goals is to help you understand the value of protecting your future, whether or not you choose to take CIBC's optional insurance.</p>`;
    }
    else if(e.currentTarget.checked && e.currentTarget.value == "laterDate") {
        obejctionData.innerHTML = `<p>Content Not Available</p>`;
    }
    obejctionData.style.display = "block";
}

exitAssessmentReason.forEach(reason => {
    reason.addEventListener('change', reasonChange);
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