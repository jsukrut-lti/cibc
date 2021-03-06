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



function exitApplication(e){
    document.location.href="/insurance/exit/{{ exit_id }}";
}




//session development
var timer;
function myTimeout () {
    console.log('new timeout started!!')
    clearTimeout(timer)
    timer = setTimeout(checkSession, 100000);
};
myTimeout();

function checkSession (){
    console.log('success');
    console.log('timer', timer);
    var retVal = confirm("Session timeout!! Do you want to continue ?");
    if (retVal == true) {
        console.log('session extended');
        myTimeout ();
    } else {
        console.log('click cancel');
        clearTimeout(timer);
        window.location = window.location.protocol + "//" + window.location.host + '/insurance/exit';
    }

};


document.onclick = function (){
    myTimeout();
};

$(document).ready(function (){
        var validNavigation = false;


//         Attach the event submit for all forms in the page
        $("form").bind("submit", function() {
          validNavigation = true;
        });

//         Attach the event click for all inputs in the page
        $("input[type=submit]").bind("click", function() {
          validNavigation = true;
        });

//         Attach the event button for all inputs in the page
        $("a[role=button]").bind("click", function() {
          validNavigation = true;
        });

        window.onbeforeunload = function() {
            if (!validNavigation) {
                saveDB();
            } else {
                validNavigation = false;
            }
        };

  });


function saveDB() {

        var formData = new FormData();
  		// sending update Insurance discussion call.
        formData.append('csrfmiddlewaretoken', csrf_token);
        const url = window.location.protocol+"//"+window.location.host+'/insurance/save_session'
        navigator.sendBeacon(url, formData);
}