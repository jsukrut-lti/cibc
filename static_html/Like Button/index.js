
function loadData(input) {
    var btn = document.getElementById("btn_" + input);
    var xhttp = new XMLHttpRequest();

   xhttp.open('GET', 'https://mokhtar93.github.io/data.json');
    xhttp.onload = function () {
        if (xhttp.status >= 200 && xhttp.status < 400) {
            var ourData = JSON.parse(xhttp.responseText);
            renderHTML(ourData, input);
            btn.className = "hide-me"
        } else {
            console.log("We connected to the server, but it returned an error.");
        }
    };

    xhttp.onerror = function () {
        console.log("Connection error");
    };
    xhttp.send();
}

function renderHTML(data, index) {
    var newdata = data.data[index - 1];
    var handlers = newdata.handlers;
    var container = document.getElementById('container_' + index);

    for (let i = 0; i < handlers.length; i++) {
        var parentNode = document.createElement("tr");

        let newNode = document.createElement("th");
        newNode.scope = 'row';
        newNode.innerHTML = `<img class="icon-height"   src="assets/sad.svg"  onclick="react('${i+ 1}' , '${index}', 'Sad') "> <img class="icon-height"   src="assets/meh.svg"  onclick="react('${i+ 1}' , '${index}', 'Neutral')" > <img class="icon-height"   src="assets/happy.svg"  onclick="react('${i+ 1}' , '${index}', 'Happy')" >`;
        parentNode.appendChild(newNode)

        let newNodeSecond = document.createElement("td");
        newNodeSecond.innerText = handlers[i].handlerName;
        parentNode.appendChild(newNodeSecond)

        let newNodeThird = document.createElement("td");
        newNodeThird.innerText = handlers[i].handlerPercentage;
        parentNode.appendChild(newNodeThird)

        container.appendChild(parentNode);

    }

}


function react(concern, handle, response) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log("success");

        } else {
            console.log("We connected to the server, but it returned an error.");
        }
        xhttp.open('POST', `http://localhost:8080/?concern='${concern}'&section=xyz&handle=${handle}&Response=${response}`, true);
        xhttp.send();

        xhttp.onerror = function () {
            console.log("Connection error");
        };
    };
}