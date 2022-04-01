var partner_box = document.getElementById('partner_box');
var partner_card = document.getElementById('partner_card');
var partner_collapsableCard = new bootstrap.Collapse(partner_card, {toggle: false});

partner_box.addEventListener('click', function () {
     //boxText = partner_box.getElementById('text');
     //boxText.class = "options--boxText-selected";
     // = "options--box-selected";
      if (partner_box.getAttribute("class") == "options--box" ){
        partner_box.setAttribute("class","options--box-selected")
        partner_collapsableCard.toggle();
      } else{
         partner_box.setAttribute("class","options--box")
        partner_collapsableCard.toggle();
      }
      console.log(partner_box.getAttribute("class") );

});


var children_box = document.getElementById('children_box');
var children_card = document.getElementById('children_card');
var children_collapsableCard = new bootstrap.Collapse(children_card, {toggle: false});

children_box.addEventListener('click', function () {
     //boxText = partner_box.getElementById('text');
     //boxText.class = "options--boxText-selected";
     // = "options--box-selected";
      if (children_box.getAttribute("class") == "options--box" ){
        children_box.setAttribute("class","options--box-selected")
        children_collapsableCard.toggle();
      } else{
         children_box.setAttribute("class","options--box")
        children_collapsableCard.toggle();
      }
      console.log(partner_box.getAttribute("class") );

});



var older_box = document.getElementById('older_box');
var older_card = document.getElementById('older_card');
var older_collapsableCard = new bootstrap.Collapse(older_card, {toggle: false});

older_box.addEventListener('click', function () {
     //boxText = partner_box.getElementById('text');
     //boxText.class = "options--boxText-selected";
     // = "options--box-selected";
      if (older_box.getAttribute("class") == "options--box" ){
        older_box.setAttribute("class","options--box-selected")
        older_collapsableCard.toggle();
      } else{
         older_box.setAttribute("class","options--box")
        older_collapsableCard.toggle();
      }
      console.log(older_box.getAttribute("class") );

});


var otherLoved_box = document.getElementById('otherLoved_box');
var otherLoved_card = document.getElementById('otherLoved_card');
var otherLoved_collapsableCard = new bootstrap.Collapse(otherLoved_card, {toggle: false});

otherLoved_box.addEventListener('click', function () {
     //boxText = partner_box.getElementById('text');
     //boxText.class = "options--boxText-selected";
     // = "options--box-selected";
      if (otherLoved_box.getAttribute("class") == "options--box" ){
        otherLoved_box.setAttribute("class","options--box-selected")
        otherLoved_collapsableCard.toggle();
      } else{
         otherLoved_box.setAttribute("class","options--box")
        otherLoved_collapsableCard.toggle();
      }
      console.log(otherLoved_box.getAttribute("class") );

});
