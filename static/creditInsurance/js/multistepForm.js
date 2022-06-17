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