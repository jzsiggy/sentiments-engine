async function getFeedFromSource(endpoint, keyword) {
    const response = await fetch(`${endpoint}?keyword=${keyword}`, {});
    const json = await response.json();
    return json;
}

async function getFullFeed(keyword) {
    const sources = [
        "http://127.0.0.1:5000/reddit",
        "http://127.0.0.1:5000/guardian",
        "http://127.0.0.1:5000/nyt",
        // "http://127.0.0.1:5000/crypto-panic"
    ]
    
    let promises = []

    sources.forEach(async function (source) {
        promise = getFeedFromSource(source, keyword);
        promises.push(promise)
    });

    return Promise.all(promises)
    .then(data => data)
};

removeAllChildren = (div) => {
    while (div.firstChild) {
        div.removeChild(div.firstChild);
    };
};

const searchBtn = document.querySelector("#search-btn");

searchBtn.addEventListener("click", async function() {
    const input = document.querySelector("#search");
    let data = await getFullFeed(input.value)
    populate(data);
});

let populate = (data) => {
    const resultsDiv = document.querySelector(".results")
    removeAllChildren(resultsDiv);
    data.forEach(source => {
        for (index in source) {
            console.log(source[index])
        };
    });
};
