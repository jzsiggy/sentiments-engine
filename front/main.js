removeAllChildren = (div) => {
    while (div.firstChild) {
        div.removeChild(div.firstChild);
    };
};

parseRedditInfo = (keyword) => {
    let positiveDiv = document.querySelector(".positive-headlines")
    let negativeDiv = document.querySelector(".negative-headlines")
    let request = new XMLHttpRequest

    request.open('GET', `http://127.0.0.1:5000/reddit?keyword=${keyword}`, true);
    request.onload = function () {
        let data = JSON.parse(this.response);
        console.log(data);
        for (index in data) {
            let link = document.createElement("a");
            link.setAttribute("href", data[index]["url"])
            let header = document.createElement("h4");
            header.innerText = data[index]["title"];
            link.appendChild(header);
            if (data[index]["polarity"] > 0.4) {  
                positiveDiv.appendChild(link);
            } else if (data[index]["polarity"] < -0.4) {
                negativeDiv.appendChild(link);
            };
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
    parseRedditInfo(input.value);
});
