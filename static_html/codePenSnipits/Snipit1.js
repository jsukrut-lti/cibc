var toggleButton = document.getElementById('toggleCardButton');
var card = document.getElementById('card');
var collapsableCard = new bootstrap.Collapse(card, {toggle: false});
toggleButton.addEventListener('click', function () {
    collapsableCard.toggle();
});

 var rangeInput = document.getElementById("range-input")
 var rangeValue = document.getElementById("range-value")
 var button = document.getElementById("btn")

 button.onclick = testTest

 function testTest() {
   let value = rangeInput.value
   if(value > 0 && value < 5) {
      alert("first")
      return true
   }
     alert("second")
     return false
 }

 // Print the range value to the output
 rangeInput.oninput = rangeOutput

 function rangeOutput() {
   rangeValue.innerText = rangeInput.value
 }




const labels = [
  'Income',
  'Expense W/O Ins',
  'Expense W Ins',
];

const data = {
  labels: labels,
  datasets: [
    {
      label: 'Dataset 1',
      data: [7, 10, 5,],
      backgroundColor: 'rgba(255, 0, 0, 0.2)',
    },
    {
      label: 'Dataset 2',
      data:[7, 10, 5,],
      backgroundColor: 'rgba(0, 255, 0, 0.2)',
    },
    {
      label: 'Dataset 3',
      data: [7, 10, 5,],
      backgroundColor: 'rgba(0, 0, 255, 0.2)',
    },
  ]
};



const config = {
  type: 'bar',
  data: data,
  options: {
    plugins: {
      title: {
        display: true,
        text: 'Chart.js Bar Chart - Stacked'
      },
    },
    responsive: true,
    scales: {
      x: {
        stacked: true,
      },
      y: {
        stacked: true
      }
    }
  }
};

var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, config);