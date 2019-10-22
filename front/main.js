removeAllChildren = (div) => {
    while (div.firstChild) {
        div.removeChild(div.firstChild);
    };
};

getPositiveRequest = (keyword) => {
    let positiveDiv = document.querySelector(".positive-headlines")
    let request = new XMLHttpRequest

    request.open('GET', `http://127.0.0.1:5000/reddit/positive?keyword=${keyword}`, true);
    request.onload = function () {
        let data = JSON.parse(this.response);
        console.log(data);
        for (index in data) {
            let header = document.createElement("h4");
            header.innerText = data[index]["headline"];
            positiveDiv.appendChild(header);
        };
    };
    
    request.send();
};

getNegativeRequest = (keyword) => {
    let negativeDiv = document.querySelector(".negative-headlines")
    let request = new XMLHttpRequest

    request.open('GET', `http://127.0.0.1:5000/reddit/negative?keyword=${keyword}`, true);
    request.onload = function () {
        let data = JSON.parse(this.response);
        console.log(data);
        for (index in data) {
            let header = document.createElement("h4");
            header.innerText = data[index]["headline"];
            negativeDiv.appendChild(header);
        };
    };
    
    request.send();
};

const searchBtn = document.querySelector("#search-btn");

searchBtn.addEventListener("click", () => {
    document.querySelectorAll(".responses > div > div").forEach(div => {
        removeAllChildren(div);
    });
    
    const input = document.querySelector("#search");
    console.log(input.value);
    getPositiveRequest(input.value);
    getNegativeRequest(input.value);
});
