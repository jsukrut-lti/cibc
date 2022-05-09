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

sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");
});


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


// Questionnaire - add active class on selected list item
let questionnaireItems = document.querySelectorAll('.questionnaireSection ul li');
let questionnaireSectionObjection = document.querySelector('.questionnaireSectionObjection');

function addActive(e) {
    let currentItem = e.currentTarget.innerText;
    questionnaireSectionObjection.style.display = "block";

    questionnaireItems.forEach((item) => {
        item.classList.remove('active');
    })
    this.classList.add('active');

    if(currentItem <= 5) {
        questionnaireSectionObjection.innerText = `Thank you for sharing that.  I'd like to ask you some additional questions to see if there is an opportunity to help you feel more confident about your plan.`;
    }

    else if(currentItem <= 8) {
        questionnaireSectionObjection.innerText = `Thank you for sharing that. I'm glad you have thought about this. I'd like to ask you a few more questions to see if there is an opportunity to compliment the plan you have in place.`;
    }

    else {
        questionnaireSectionObjection.innerText = `Thank you for sharing that.  I am very happy to hear that you have thought about this before. I'd like to ask you a few questions to ensure that the changes we are working on today don't impact your existing plan.`;
    }
}

questionnaireItems.forEach((item) => {
    item.addEventListener('click', addActive);
})


// Multi Step Form For Client Page

var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tabContent");
  x[n].classList.add('active');

  //... and fix the Previous/Next buttons:
//   if (n == 0) {
//     document.getElementById("prevBtn").style.display = "none";
//   } else {
//     document.getElementById("prevBtn").style.display = "inline";
//   }

//   if (n == (x.length - 1)) {
//     document.getElementById("nextBtn").innerHTML = "Submit";
//   } else {
//     document.getElementById("nextBtn").innerHTML = "Next";
//   }
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tabContent");
  
  // Hide the current tab:
//   x[currentTab].style.display = "none";
  x[currentTab].classList.remove('active');
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

let subMenuItems = document.querySelectorAll('.subMenu ul.sub-menu li a');
    tabContentList = document.querySelectorAll('.tabContent');
    i = 0;
    myArr = new Array();

    for (let key in tabContentList) {
        myArr[tabContentList[key].id] = i;
        i++;
    }

function hideTab() {
    tabContentList.forEach(item => {
        item.classList.remove('active');
    })
}

subMenuItems.forEach(sideItems => {
    sideItems.addEventListener("click", (e) => {
        hideTab();
        let text = e.currentTarget.innerText.toLowerCase().replace(' ','');
        document.querySelector('#' + text).classList.add('active');
        currentTab = myArr[e.currentTarget.innerText.toLowerCase().replace(' ','')];
    })
})
